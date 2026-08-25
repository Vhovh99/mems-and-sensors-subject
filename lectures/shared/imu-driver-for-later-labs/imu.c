/* imu.c — Laboratory 1 starter driver (bus handling complete)
 *
 * You are not asked to modify this file. Read it: it is the reference for how a
 * register-level sensor driver is structured, and you will write one from scratch
 * in Laboratory 7.
 */
#include "main.h"   /* CubeMX-generated: pulls in the HAL and hi2c1 */
#include "imu.h"
#include <math.h>

/* Provided by your CubeMX-generated project. If your I2C peripheral is not I2C1,
 * change this one line to match. */
extern I2C_HandleTypeDef hi2c1;
#define IMU_BUS   (&hi2c1)
#define IMU_TMO   100u          /* ms — generous; a healthy bus answers in <1 ms */

static bool read_regs(uint8_t reg, uint8_t *buf, uint16_t n)
{
    return HAL_I2C_Mem_Read(IMU_BUS, IMU_ADDR_HAL, reg,
                            I2C_MEMADD_SIZE_8BIT, buf, n, IMU_TMO) == HAL_OK;
}

static bool write_reg(uint8_t reg, uint8_t val)
{
    return HAL_I2C_Mem_Write(IMU_BUS, IMU_ADDR_HAL, reg,
                             I2C_MEMADD_SIZE_8BIT, &val, 1, IMU_TMO) == HAL_OK;
}

bool imu_probe(uint8_t *id_out)
{
    uint8_t id = 0;
    if (!read_regs(IMU_REG_WHO_AM_I, &id, 1))
        return false;                      /* bus fault: wiring, address, power */
    if (id_out) *id_out = id;
    return id == IMU_WHO_AM_I_VALUE;       /* wrong part, or wrong register     */
}

bool imu_configure(void)
{
    uint8_t common = 0;

    /* Read-modify-write: never clobber bits you do not own. */
    if (!read_regs(IMU_REG_CTRL_COMMON, &common, 1))            return false;
    if (!write_reg(IMU_REG_CTRL_COMMON, common | IMU_AUTO_INCREMENT_BIT))
                                                                return false;
    if (!write_reg(IMU_REG_CTRL_ACCEL, IMU_CTRL_ACCEL_VALUE))   return false;

    HAL_Delay(20);   /* let the first conversion complete before anyone reads it */
    return true;
}

bool imu_read(imu_sample_t *out)
{
    uint8_t b[6];

    /* ONE burst of six bytes. Six separate reads would let the X value come from
     * one sample and the Z value from the next — a torn reading that looks fine. */
    if (!read_regs(IMU_REG_OUT_ACCEL, b, sizeof b))
        return false;

    /* Low byte first, then cast to int16_t so two's complement survives.
     * Casting to int or uint16_t here is the classic bug: a downward tilt then
     * reads as roughly +64000 instead of about -1000. */
    out->raw_x = (int16_t)(((uint16_t)b[1] << 8) | (uint16_t)b[0]);
    out->raw_y = (int16_t)(((uint16_t)b[3] << 8) | (uint16_t)b[2]);
    out->raw_z = (int16_t)(((uint16_t)b[5] << 8) | (uint16_t)b[4]);

    /* Codes are not physics until multiplied by a number from the datasheet. */
    out->mg_x = out->raw_x * IMU_SENS_MG_PER_LSB;
    out->mg_y = out->raw_y * IMU_SENS_MG_PER_LSB;
    out->mg_z = out->raw_z * IMU_SENS_MG_PER_LSB;

    out->magnitude_mg = sqrtf(out->mg_x * out->mg_x +
                              out->mg_y * out->mg_y +
                              out->mg_z * out->mg_z);
    return true;
}

float imu_mg_to_ms2(float mg) { return (mg / 1000.0f) * STANDARD_GRAVITY; }
