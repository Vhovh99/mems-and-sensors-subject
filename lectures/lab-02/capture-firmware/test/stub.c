/* stub.c — a simulated ISM330DHCX on a simulated bus, for host testing.
 *
 * Models the parts of the device this lab depends on: WHO_AM_I, the CTRL1_XL
 * register with its ODR/FS/LPF2 fields, CTRL3_C's reset value, and an
 * accelerometer whose noise scales as sqrt(bandwidth) exactly as the datasheet
 * says it should. That last property is what makes the test worth having: it
 * lets us check that a capture really does show sigma growing with ODR.
 */
#include "main.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

I2C_HandleTypeDef hi2c1;
UART_HandleTypeDef huart2;

#define SENSOR_ADDR7 0x6A
static uint8_t reg_ctrl1 = 0x00;      /* power-down out of reset */
static uint8_t reg_ctrl3 = 0x04;      /* IF_INC already set */
static uint8_t reg_ctrl8 = 0x00;

static uint32_t g_tick = 0;
static double   g_noise_ug_rt_hz = 100.0;   /* datasheet max */

/* input the test feeds in, in mg, per axis */
double sim_true_mg[3] = { 0.0, 0.0, 1000.0 };

static double odr_hz(void)
{
    switch ((reg_ctrl1 >> 4) & 0x0F) {
    case 1: return 12.5; case 2: return 26; case 3: return 52;
    case 4: return 104;  case 5: return 208; case 6: return 416;
    case 7: return 833;  default: return 0;
    }
}

static double ug_per_lsb(void)
{
    switch ((reg_ctrl1 >> 2) & 0x03) {
    case 0: return 61; case 1: return 488; case 2: return 122; default: return 244;
    }
}

static double gauss(void)
{
    double u1 = (rand() + 1.0) / (RAND_MAX + 2.0), u2 = (rand() + 1.0) / (RAND_MAX + 2.0);
    return sqrt(-2.0 * log(u1)) * cos(2.0 * 3.14159265358979323846 * u2);
}

uint32_t HAL_GetTick(void) { return g_tick; }

/* Every register read costs 202 us of simulated bus time, and a capture loop
 * has nothing else in it — so the achieved rate comes out below the ODR, which
 * is the effect stage 4 asks the student to measure. */
static void advance_for_read(void)
{
    static uint32_t frac_us = 0;
    double f = odr_hz();
    uint32_t step_us = 202 + (f > 0 ? (uint32_t)(1e6 / f) : 0);
    frac_us += step_us;
    g_tick += frac_us / 1000u;
    frac_us %= 1000u;
}

HAL_StatusTypeDef HAL_I2C_Mem_Read(I2C_HandleTypeDef *h, uint16_t a, uint16_t reg,
                                   uint16_t sz, uint8_t *buf, uint16_t n, uint32_t t)
{
    (void)h; (void)sz; (void)t;
    if ((a >> 1) != SENSOR_ADDR7) return HAL_ERROR;
    if (reg == 0x0F && n >= 1) { buf[0] = 0x6B; return HAL_OK; }
    if (reg == 0x10 && n >= 1) { buf[0] = reg_ctrl1; return HAL_OK; }
    if (reg == 0x12 && n >= 1) { buf[0] = reg_ctrl3; return HAL_OK; }
    if (reg == 0x17 && n >= 1) { buf[0] = reg_ctrl8; return HAL_OK; }
    if (reg == 0x28 && n >= 6) {
        double f = odr_hz();
        if (f == 0) { memset(buf, 0, 6); return HAL_OK; }
        /* bandwidth = ODR/2, halved again when LPF2 is enabled */
        double bw = f / 2.0;
        if ((reg_ctrl1 >> 1) & 1) bw /= 2.0;
        double sigma_mg = g_noise_ug_rt_hz * sqrt(bw) / 1000.0;
        double lsb_mg = ug_per_lsb() / 1000.0;
        for (int ax = 0; ax < 3; ax++) {
            double v = sim_true_mg[ax] + sigma_mg * gauss();
            long code = lround(v / lsb_mg);
            if (code > 32767) code = 32767;
            if (code < -32768) code = -32768;
            buf[2 * ax]     = (uint8_t)(code & 0xFF);
            buf[2 * ax + 1] = (uint8_t)((code >> 8) & 0xFF);
        }
        advance_for_read();
        return HAL_OK;
    }
    return HAL_ERROR;
}

HAL_StatusTypeDef HAL_I2C_Mem_Write(I2C_HandleTypeDef *h, uint16_t a, uint16_t reg,
                                    uint16_t sz, uint8_t *buf, uint16_t n, uint32_t t)
{
    (void)h; (void)sz; (void)n; (void)t;
    if ((a >> 1) != SENSOR_ADDR7) return HAL_ERROR;
    if (reg == 0x10) { reg_ctrl1 = buf[0]; return HAL_OK; }
    if (reg == 0x17) { reg_ctrl8 = buf[0]; return HAL_OK; }
    return HAL_ERROR;
}

HAL_StatusTypeDef HAL_I2C_IsDeviceReady(I2C_HandleTypeDef *h, uint16_t a,
                                        uint32_t tries, uint32_t t)
{
    (void)h; (void)tries; (void)t;
    return ((a >> 1) == SENSOR_ADDR7) ? HAL_OK : HAL_ERROR;
}

HAL_StatusTypeDef HAL_UART_Transmit(UART_HandleTypeDef *h, uint8_t *p, uint16_t n, uint32_t t)
{
    (void)h; (void)t;
    fwrite(p, 1, n, stdout);
    return HAL_OK;
}

/* The test drives commands from stdin, one per line. */
HAL_StatusTypeDef HAL_UART_Receive(UART_HandleTypeDef *h, uint8_t *p, uint16_t n, uint32_t t)
{
    (void)h; (void)n; (void)t;
    int c = getchar();
    if (c == EOF) exit(0);
    *p = (uint8_t)c;
    return HAL_OK;
}
