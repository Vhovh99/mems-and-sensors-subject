/* sensor_console.c — Laboratory 1 register console (instructor firmware)
 *
 * A serial command interface to any I2C register-mapped sensor. Deliberately
 * generic: it knows nothing about which part is on the bench, so the students
 * must supply every address and every value from the datasheet.
 */
#include "main.h"          /* CubeMX: HAL, hi2c1, huart2 */
#include "sensor_console.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

extern I2C_HandleTypeDef hi2c1;
extern UART_HandleTypeDef huart2;

#define BUS      (&hi2c1)
#define TMO      100u

static uint8_t g_addr7 = DEFAULT_ADDR_7BIT;

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

#if SENSOR_CONSOLE_USE_UART

#define LINE_MAX 64

static char line[LINE_MAX];
static uint8_t line_len;

/* ------------------------------------------------------------------ plumbing */
static void put(const char *s)
{
    HAL_UART_Transmit(&huart2, (uint8_t *)s, strlen(s), 200);
}

static int hex(const char *s, uint32_t *out)      /* accepts 0x40, 40, 0X40 */
{
    char *end;
    if (!s || !*s) return 0;
    *out = (uint32_t)strtoul(s, &end, 16);
    return end != s;
}

static void fail(HAL_StatusTypeDef st)
{
    char b[224];
    snprintf(b, sizeof b,
             "ERROR: no reply from 0x%02X (%s).\r\n"
             "       Check: pull-ups present? SDA/SCL not swapped? address right?\r\n"
             "       Try `scan` to see what is actually on the bus.\r\n",
             g_addr7, st == HAL_BUSY ? "bus busy - usually a missing pull-up"
                                     : "no acknowledge");
    put(b);
}

/* ------------------------------------------------------------------ commands */
static void cmd_scan(void)
{
    char b[64];
    int found = 0;
    put("Scanning 0x08..0x77 ...\r\n");
    for (uint8_t a = SCAN_FIRST_ADDR; a <= SCAN_LAST_ADDR; a++) {
        if (HAL_I2C_IsDeviceReady(BUS, (uint16_t)(a << 1), 2, 10) == HAL_OK) {
            snprintf(b, sizeof b, "  device found at 7-bit address 0x%02X\r\n", a);
            put(b); found++;
        }
    }
    if (!found)
        put("  nothing answered.\r\n"
            "  Either the bus cannot work at all (no pull-up, SDA/SCL swapped,\r\n"
            "  no power at the sensor) or nothing is connected.\r\n");
    else {
        snprintf(b, sizeof b, "  %d device(s). Console is talking to 0x%02X.\r\n",
                 found, g_addr7);
        put(b);
    }
}

static void cmd_read(uint8_t reg, uint16_t n)
{
    uint8_t buf[16]; char b[96];
    HAL_StatusTypeDef st;
    if (n > sizeof buf) n = sizeof buf;
    st = rd(reg, buf, n);
    if (st != HAL_OK) { fail(st); return; }
    for (uint16_t i = 0; i < n; i++) {
        snprintf(b, sizeof b, "  0x%02X = 0x%02X   (%3u)   %c%c%c%c%c%c%c%c\r\n",
                 reg + i, buf[i], buf[i],
                 (buf[i] & 0x80) ? '1':'0', (buf[i] & 0x40) ? '1':'0',
                 (buf[i] & 0x20) ? '1':'0', (buf[i] & 0x10) ? '1':'0',
                 (buf[i] & 0x08) ? '1':'0', (buf[i] & 0x04) ? '1':'0',
                 (buf[i] & 0x02) ? '1':'0', (buf[i] & 0x01) ? '1':'0');
        put(b);
    }
}

static void cmd_write(uint8_t reg, uint8_t val)
{
    char b[80]; uint8_t back = 0;
    if (wr(reg, val) != HAL_OK) { fail(HAL_ERROR); return; }
    HAL_Delay(10);
    if (rd(reg, &back, 1) == HAL_OK) {
        snprintf(b, sizeof b, "  wrote 0x%02X to 0x%02X, reads back 0x%02X %s\r\n",
                 val, reg, back, (back == val) ? "" : "  <-- DIFFERENT, why?");
        put(b);
    }
}

/* Six output bytes -> three int16. RAW ONLY. Conversion is the student's job. */
static void cmd_dump(uint8_t reg)
{
    uint8_t b6[6]; char b[224];
    int16_t x, y, z;
    if (rd(reg, b6, 6) != HAL_OK) { fail(HAL_ERROR); return; }
    x = (int16_t)(((uint16_t)b6[1] << 8) | b6[0]);
    y = (int16_t)(((uint16_t)b6[3] << 8) | b6[2]);
    z = (int16_t)(((uint16_t)b6[5] << 8) | b6[4]);
    snprintf(b, sizeof b,
             "  bytes : %02X %02X  %02X %02X  %02X %02X   (low byte first)\r\n"
             "  int16 : X=%6d   Y=%6d   Z=%6d\r\n"
             "  -> multiply by the sensitivity for YOUR configured range.\r\n",
             b6[0], b6[1], b6[2], b6[3], b6[4], b6[5], x, y, z);
    put(b);
}

static void cmd_log(uint8_t reg, uint16_t n, uint16_t period_ms)
{
    uint8_t b6[6]; char b[64];
    put("n,raw_x,raw_y,raw_z\r\n");
    for (uint16_t i = 1; i <= n; i++) {
        if (rd(reg, b6, 6) != HAL_OK) { put("READ_FAILED\r\n"); return; }
        snprintf(b, sizeof b, "%u,%d,%d,%d\r\n", i,
                 (int16_t)(((uint16_t)b6[1] << 8) | b6[0]),
                 (int16_t)(((uint16_t)b6[3] << 8) | b6[2]),
                 (int16_t)(((uint16_t)b6[5] << 8) | b6[4]));
        put(b);
        HAL_Delay(period_ms);
    }
    put("# end. Units: none - these are raw codes.\r\n");
}

static void help(void)
{
    put("\r\nCommands (all values in hex unless noted):\r\n"
        "  scan               list every device that answers on the bus\r\n"
        "  addr <a>           talk to 7-bit address <a>        e.g. addr 6B\r\n"
        "  r <reg>            read one register, shown in hex, decimal, binary\r\n"
        "  r <reg> <n>        read <n> consecutive registers (n decimal, max 16)\r\n"
        "  w <reg> <val>      write a register, then read it back\r\n"
        "  dump <reg>         read 6 bytes from <reg>, assemble 3 signed 16-bit\r\n"
        "  log <reg> <n> <ms> stream <n> samples every <ms> ms as CSV (decimal)\r\n"
        "  help               this list\r\n\r\n"
        "This console never prints milli-g, m/s^2 or any engineering unit.\r\n"
        "Converting codes to units using the datasheet is your job.\r\n\r\n");
}

/* ------------------------------------------------------------------ dispatch */
static void execute(char *s)
{
    char *tok[4] = {0};
    int n = 0;
    uint32_t a = 0, b_ = 0, c = 0;

    for (char *p = strtok(s, " \t"); p && n < 4; p = strtok(NULL, " \t")) tok[n++] = p;
    if (n == 0) return;

    if      (!strcmp(tok[0], "help") || !strcmp(tok[0], "?")) help();
    else if (!strcmp(tok[0], "scan")) cmd_scan();
    else if (!strcmp(tok[0], "addr") && n >= 2 && hex(tok[1], &a)) {
        g_addr7 = (uint8_t)a;
        char m[64];
        snprintf(m, sizeof m, "  now talking to 7-bit 0x%02X (HAL uses 0x%02X)\r\n",
                 g_addr7, (uint8_t)(g_addr7 << 1));
        put(m);
    }
    else if (!strcmp(tok[0], "r") && n >= 2 && hex(tok[1], &a))
        cmd_read((uint8_t)a, (n >= 3) ? (uint16_t)atoi(tok[2]) : 1);
    else if (!strcmp(tok[0], "w") && n >= 3 && hex(tok[1], &a) && hex(tok[2], &b_))
        cmd_write((uint8_t)a, (uint8_t)b_);
    else if (!strcmp(tok[0], "dump") && n >= 2 && hex(tok[1], &a))
        cmd_dump((uint8_t)a);
    else if (!strcmp(tok[0], "log") && n >= 4 && hex(tok[1], &a)) {
        b_ = (uint32_t)atoi(tok[2]); c = (uint32_t)atoi(tok[3]);
        cmd_log((uint8_t)a, (uint16_t)b_, (uint16_t)(c ? c : 50));
    }
    else put("  ? unknown or malformed command - type `help`\r\n");
}

void console_init(void)
{
    put("\r\n=====================================================\r\n"
        " MEMS & Sensors - Laboratory 1 - register console\r\n"
        " Raw codes only. You do the conversions.\r\n"
        "=====================================================\r\n");
    help();
    put("> ");
}

void console_poll(void)
{
    uint8_t ch;
    if (HAL_UART_Receive(&huart2, &ch, 1, 10) != HAL_OK) return;

    if (ch == '\r' || ch == '\n') {
        put("\r\n");
        line[line_len] = '\0';
        if (line_len) execute(line);
        line_len = 0;
        put("> ");
    } else if ((ch == '\b' || ch == 127) && line_len) {
        line_len--; put("\b \b");
    } else if (line_len < LINE_MAX - 1 && ch >= ' ') {
        line[line_len++] = (char)ch;
        HAL_UART_Transmit(&huart2, &ch, 1, 20);      /* echo */
    }
}

#else

#define WHO_AM_I_REG 0x0F
#define CTRL1_XL_REG 0x10
#define OUTX_L_A_REG 0x28
#define SAMPLE_PERIOD_MS 50u

volatile sensor_watch_t sensor_watch = {
    .ctrl1_xl_request = 0x40       /* ±2 g, 104 Hz */
};

void console_init(void)
{
    for (uint8_t a = SCAN_FIRST_ADDR; a <= SCAN_LAST_ADDR; a++) {
        if (HAL_I2C_IsDeviceReady(BUS, (uint16_t)(a << 1), 2, 10) == HAL_OK) {
            sensor_watch.device_count++;
            if (a == 0x6A || a == 0x6B)
                sensor_watch.address = a;
        }
    }

    if (!sensor_watch.address) {
        sensor_watch.i2c_status = HAL_ERROR;
        return;
    }

    g_addr7 = sensor_watch.address;
    sensor_watch.i2c_status = rd(WHO_AM_I_REG, (uint8_t *)&sensor_watch.who_am_i, 1);
    if (sensor_watch.i2c_status == HAL_OK)
        sensor_watch.i2c_status = rd(CTRL1_XL_REG, (uint8_t *)&sensor_watch.ctrl1_xl, 1);
}

void console_poll(void)
{
    static uint32_t last_sample;
    uint8_t raw[6];

    if (!sensor_watch.address)
        return;

    if (sensor_watch.ctrl1_xl != sensor_watch.ctrl1_xl_request) {
        sensor_watch.i2c_status = wr(CTRL1_XL_REG, sensor_watch.ctrl1_xl_request);
        if (sensor_watch.i2c_status == HAL_OK) {
            HAL_Delay(10);
            sensor_watch.i2c_status = rd(CTRL1_XL_REG, (uint8_t *)&sensor_watch.ctrl1_xl, 1);
        }
    }

    if (HAL_GetTick() - last_sample < SAMPLE_PERIOD_MS)
        return;
    last_sample = HAL_GetTick();

    sensor_watch.i2c_status = rd(OUTX_L_A_REG, raw, sizeof raw);
    if (sensor_watch.i2c_status != HAL_OK)
        return;

    for (uint8_t i = 0; i < sizeof raw; i++)
        sensor_watch.raw_bytes[i] = raw[i];
    sensor_watch.raw_x = (int16_t)(((uint16_t)raw[1] << 8) | raw[0]);
    sensor_watch.raw_y = (int16_t)(((uint16_t)raw[3] << 8) | raw[2]);
    sensor_watch.raw_z = (int16_t)(((uint16_t)raw[5] << 8) | raw[4]);
    sensor_watch.sample_count++;
}

#endif
