/* lab2_capture.c — Laboratory 2 capture console (instructor firmware)
 *
 * See lab2_capture.h for the design rules. In short: raw codes and
 * milliseconds out, no units, no statistics.
 *
 * Timing. Timestamps come from HAL_GetTick(), which is 1 ms. That is too
 * coarse to resolve the jitter of a single sample, and it is entirely
 * sufficient for what stage 4 asks, which is the MEAN interval over a long
 * capture: 2000 samples over ~20 s resolves the mean to about 0.5 us, so a
 * 2 % rate error shows up unmistakably. Using a 1 MHz timer instead would need
 * a CubeMX change and give the student nothing extra to learn. If you later
 * want per-sample jitter, add a free-running TIM at 1 MHz and swap now_ms()
 * for it; nothing else in this file needs to change.
 */
#include "main.h"          /* CubeMX: HAL, hi2c1, huart2 */
#include "lab2_capture.h"
#include "lab2_config.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

extern I2C_HandleTypeDef hi2c1;
extern UART_HandleTypeDef huart2;

#define BUS      (&hi2c1)
#define TMO      100u
#define LINE_MAX 64

static uint8_t g_addr7 = LAB2_ADDR_7BIT;
static char    line[LINE_MAX];
static uint8_t line_len;

/* ------------------------------------------------------------------ plumbing */
static void put(const char *s)
{
    HAL_UART_Transmit(&huart2, (uint8_t *)s, strlen(s), 500);
}

static uint32_t now_ms(void) { return HAL_GetTick(); }

static int hex(const char *s, uint32_t *out)      /* accepts 0x42, 42, 0X42 */
{
    char *end;
    if (!s || !*s) return 0;
    *out = (uint32_t)strtoul(s, &end, 16);
    return end != s;
}

static HAL_StatusTypeDef rd(uint8_t reg, uint8_t *buf, uint16_t n)
{
    return HAL_I2C_Mem_Read(BUS, (uint16_t)(g_addr7 << 1), reg,
                            I2C_MEMADD_SIZE_8BIT, buf, n, TMO);
}

static HAL_StatusTypeDef wr(uint8_t reg, uint8_t val)
{
    return HAL_I2C_Mem_Write(BUS, (uint16_t)(g_addr7 << 1), reg,
                             I2C_MEMADD_SIZE_8BIT, &val, 1, TMO);
}

static void fail(void)
{
    char b[224];
    snprintf(b, sizeof b,
             "ERROR: no reply from 0x%02X.\r\n"
             "       Check: pull-ups present? SDA/SCL not swapped? address right?\r\n"
             "       `scan` lists what is actually answering on the bus.\r\n",
             g_addr7);
    put(b);
}

/* Read CTRL1_XL back rather than trusting what we think we wrote. */
static int read_ctrl1(uint8_t *out)
{
    return rd(REG_CTRL1_XL, out, 1) == HAL_OK;
}

/* --------------------------------------------------------------- decoding */
/* ODR_XL code -> Hz, as an integer in tenths so 12.5 Hz survives. */
static uint16_t odr_tenths(uint8_t ctrl1)
{
    switch ((ctrl1 >> 4) & 0x0F) {
    case 0x0: return 0;          /* power-down */
    case 0x1: return 125;        /* 12.5 Hz */
    case 0x2: return 260;
    case 0x3: return 520;
    case 0x4: return 1040;
    case 0x5: return 2080;
    case 0x6: return 4160;
    case 0x7: return 8330;
    default:  return 0xFFFF;     /* higher rates exist; this lab does not use them */
    }
}

/* FS_XL code -> micro-g per LSB, so the student can check their own figure but
 * still has to apply it themselves. NOT ascending: 01 is +/-16 g. */
static uint16_t fs_ug_per_lsb(uint8_t ctrl1)
{
    switch ((ctrl1 >> 2) & 0x03) {
    case 0x0: return 61;         /* +/-2 g  */
    case 0x1: return 488;        /* +/-16 g */
    case 0x2: return 122;        /* +/-4 g  */
    default:  return 244;        /* +/-8 g  */
    }
}

static void print_cfg(void)
{
    uint8_t c1 = 0, c3 = 0, c8 = 0, who = 0;
    char b[512];
    uint16_t t;

    if (!read_ctrl1(&c1)) { fail(); return; }
    (void)rd(REG_CTRL3_C,  &c3,  1);
    (void)rd(REG_CTRL8_XL, &c8,  1);
    (void)rd(REG_WHO_AM_I, &who, 1);
    t = odr_tenths(c1);

    snprintf(b, sizeof b,
        "\r\n  WHO_AM_I  0x%02X   (expected 0x%02X)\r\n"
        "  CTRL1_XL  0x%02X   ODR code %X -> %u.%u Hz | FS code %X -> %u ug/LSB"
        " | LPF2_XL_EN %u\r\n"
        "  CTRL8_XL  0x%02X   (the LPF2 bandwidth selection lives here -"
        " check your datasheet revision)\r\n"
        "  CTRL3_C   0x%02X   (IF_INC is bit 2; it is set out of reset)\r\n"
        "  compiled-in LAB2_CTRL1_XL = 0x%02X %s\r\n\r\n",
        who, WHO_AM_I_EXPECTED,
        c1, (c1 >> 4) & 0x0F, t / 10u, t % 10u,
        (c1 >> 2) & 0x03, fs_ug_per_lsb(c1), (c1 >> 1) & 1u,
        c8, c3, (unsigned)LAB2_CTRL1_XL,
        (c1 == (uint8_t)LAB2_CTRL1_XL)
            ? "(matches the sensor - good)"
            : "(DIFFERS from the sensor: you changed it at runtime with `odr`/`lpf`)");
    put(b);
}

/* ------------------------------------------------------------------ commands */
static void cmd_scan(void)
{
    char b[48];
    int found = 0;
    put("  scanning 0x08..0x77 ...\r\n");
    for (uint8_t a = 0x08; a <= 0x77; a++) {
        if (HAL_I2C_IsDeviceReady(BUS, (uint16_t)(a << 1), 1, 5) == HAL_OK) {
            snprintf(b, sizeof b, "    device at 0x%02X\r\n", a);
            put(b);
            found++;
        }
    }
    put(found ? "  done.\r\n" : "  nothing answered - check wiring and pull-ups.\r\n");
}

/* The capture. Streams as it goes; buffers nothing. */
static void cmd_cap(uint16_t n)
{
    uint8_t  b6[6];
    char     b[80];
    uint32_t t0, t_end, span_ms;
    uint8_t  c1 = 0;

    if (n == 0 || n > LAB2_MAX_SAMPLES) n = LAB2_DEFAULT_N;

    if (!read_ctrl1(&c1)) { fail(); return; }
    if (((c1 >> 4) & 0x0F) == 0) {
        put("  the accelerometer is powered down (ODR code 0000).\r\n"
            "  set a rate first:  odr 4      (104 Hz)\r\n");
        return;
    }

    /* A header the spreadsheet can import directly, and a comment line that
     * records the configuration so a saved capture is self-describing. Students
     * lose track of which file was which otherwise, every single year. */
    snprintf(b, sizeof b, "# CTRL1_XL=0x%02X n=%u\r\n", c1, n);
    put(b);
    put("n,t_ms,raw_x,raw_y,raw_z\r\n");

    t0 = now_ms();
    for (uint16_t i = 1; i <= n; i++) {
        if (rd(REG_OUTX_L_A, b6, 6) != HAL_OK) {
            put("READ_FAILED - capture abandoned\r\n");
            return;
        }
        snprintf(b, sizeof b, "%u,%lu,%d,%d,%d\r\n",
                 i, (unsigned long)(now_ms() - t0),
                 (int)(int16_t)(((uint16_t)b6[1] << 8) | b6[0]),
                 (int)(int16_t)(((uint16_t)b6[3] << 8) | b6[2]),
                 (int)(int16_t)(((uint16_t)b6[5] << 8) | b6[4]));
        put(b);
    }
    t_end = now_ms();
    span_ms = t_end - t0;

    /* The only arithmetic this firmware does, and only because a stopwatch
     * cannot: mean interval in microseconds, and the rate it implies. Both are
     * integer; the student compares them with the ODR they asked for. */
    if (n >= 2 && span_ms > 0) {
        uint32_t mean_us = (span_ms * 1000u) / (uint32_t)(n - 1);
        uint32_t rate_mHz = mean_us ? (1000000000u / mean_us) : 0u;
        snprintf(b, sizeof b,
                 "# elapsed_ms=%lu samples=%u mean_interval_us=%lu\r\n",
                 (unsigned long)span_ms, n, (unsigned long)mean_us);
        put(b);
        snprintf(b, sizeof b,
                 "# achieved_rate=%lu.%03lu Hz  <- compare with the ODR you set\r\n",
                 (unsigned long)(rate_mHz / 1000u), (unsigned long)(rate_mHz % 1000u));
        put(b);
    }
    put("# end. Units: codes and milliseconds. Convert them yourself.\r\n");
}

/* Runtime ODR change, so the sweep in stage 3 costs no rebuilds. Preserves
 * FS and the LPF2 bit — a student changing the rate does not expect the range
 * to move underneath them. */
static void cmd_odr(uint32_t code)
{
    uint8_t c1 = 0, nv;
    char b[96];

    if (code > 0x6) {
        put("  odr takes a code 0..6:  0 off · 1 12.5 · 2 26 · 3 52 · 4 104"
            " · 5 208 · 6 416 Hz\r\n");
        return;
    }
    if (!read_ctrl1(&c1)) { fail(); return; }
    nv = (uint8_t)((c1 & 0x0F) | ((uint8_t)code << 4));
    if (wr(REG_CTRL1_XL, nv) != HAL_OK) { fail(); return; }
    if (!read_ctrl1(&c1)) { fail(); return; }
    snprintf(b, sizeof b, "  CTRL1_XL now 0x%02X  (wrote 0x%02X)\r\n", c1, nv);
    put(b);
    if (c1 != nv) put("  ! readback differs from what was written.\r\n");
}

static void cmd_lpf(int on)
{
    uint8_t c1 = 0, nv;
    char b[96];

    if (!read_ctrl1(&c1)) { fail(); return; }
    nv = on ? (uint8_t)(c1 | 0x02) : (uint8_t)(c1 & (uint8_t)~0x02);
    if (wr(REG_CTRL1_XL, nv) != HAL_OK) { fail(); return; }
    if (!read_ctrl1(&c1)) { fail(); return; }
    snprintf(b, sizeof b, "  LPF2_XL_EN = %u   CTRL1_XL now 0x%02X\r\n",
             (c1 >> 1) & 1u, c1);
    put(b);
    put(on ? "  bandwidth narrowed. Expect the standard deviation to fall.\r\n"
           : "  no anti-alias filter now. This is the reset default.\r\n");
}

static void help(void)
{
    put("\r\nLaboratory 2 - capture console. Values in hex unless noted.\r\n"
        "  cap [n]        capture n samples as CSV (decimal, default 2000)\r\n"
        "  odr <code>     0 off · 1 12.5 · 2 26 · 3 52 · 4 104 · 5 208 · 6 416 Hz\r\n"
        "  lpf on|off     LPF2_XL_EN - the second low-pass filter\r\n"
        "  cfg            show WHO_AM_I, CTRL1_XL decoded, CTRL8_XL, CTRL3_C\r\n"
        "  scan           list every device answering on the bus\r\n"
        "  addr <a>       talk to 7-bit address <a>          e.g. addr 6B\r\n"
        "  help           this list\r\n\r\n"
        "This console prints raw codes and milliseconds. It computes no mean,\r\n"
        "no standard deviation and no filter - those are your analysis.\r\n\r\n");
}

/* ------------------------------------------------------------------ dispatch */
static void execute(char *s)
{
    char *tok[3] = {0};
    int n = 0;
    uint32_t a = 0;

    for (char *p = strtok(s, " \t"); p && n < 3; p = strtok(NULL, " \t")) tok[n++] = p;
    if (n == 0) return;

    if      (!strcmp(tok[0], "help") || !strcmp(tok[0], "?")) help();
    else if (!strcmp(tok[0], "cfg"))  print_cfg();
    else if (!strcmp(tok[0], "scan")) cmd_scan();
    else if (!strcmp(tok[0], "cap"))
        cmd_cap((n >= 2) ? (uint16_t)atoi(tok[1]) : LAB2_DEFAULT_N);
    else if (!strcmp(tok[0], "odr") && n >= 2)
        cmd_odr((uint32_t)strtoul(tok[1], NULL, 16));
    else if (!strcmp(tok[0], "lpf") && n >= 2 && !strcmp(tok[1], "on"))  cmd_lpf(1);
    else if (!strcmp(tok[0], "lpf") && n >= 2 && !strcmp(tok[1], "off")) cmd_lpf(0);
    else if (!strcmp(tok[0], "addr") && n >= 2 && hex(tok[1], &a)) {
        char b[48];
        g_addr7 = (uint8_t)(a & 0x7F);
        snprintf(b, sizeof b, "  now talking to 0x%02X\r\n", g_addr7);
        put(b);
    }
    else put("  ? unknown or malformed command - type `help`\r\n");
}

/* ------------------------------------------------------------------- public */
void lab2_init(void)
{
    char b[320];
    uint8_t c1 = 0;

    put("\r\n\r\n=== MEMS & Sensors - Laboratory 2 - sampling, noise, filtering ===\r\n");
    snprintf(b, sizeof b,
             "    firmware built with LAB2_CTRL1_XL = 0x%02X\r\n",
             (unsigned)LAB2_CTRL1_XL);
    put(b);

    /* Apply the compiled-in configuration. If this write fails the sensor is
     * not talking, and saying so now saves ten minutes of confusion later. */
    if (wr(REG_CTRL1_XL, (uint8_t)LAB2_CTRL1_XL) != HAL_OK) {
        put("    could not configure the sensor.\r\n");
        fail();
    } else if (read_ctrl1(&c1) && c1 != (uint8_t)LAB2_CTRL1_XL) {
        snprintf(b, sizeof b,
                 "    ! wrote 0x%02X but read back 0x%02X\r\n",
                 (unsigned)LAB2_CTRL1_XL, c1);
        put(b);
    }

    put("    If the value above is not the one you edited, you are running the\r\n"
        "    old binary. Rebuild, reflash, and press reset.\r\n");
    help();
    print_cfg();
}

void lab2_poll(void)
{
    uint8_t ch;

    if (HAL_UART_Receive(&huart2, &ch, 1, 10) != HAL_OK) return;

    if (ch == '\r' || ch == '\n') {
        put("\r\n");
        line[line_len] = '\0';
        execute(line);
        line_len = 0;
        put("> ");
    } else if ((ch == '\b' || ch == 0x7F) && line_len) {
        line_len--;
        put("\b \b");
    } else if (ch >= ' ' && ch < 0x7F && line_len < LINE_MAX - 1) {
        line[line_len++] = (char)ch;
        HAL_UART_Transmit(&huart2, &ch, 1, 50);   /* echo */
    }
}
