/* imu.h — Laboratory 1 starter driver
 * MEMS and Sensors · Datasheet-to-data bring-up
 *
 * The bus handling below is complete and working. What is MISSING is every value
 * that comes out of the datasheet. That is your job, and it is the point of the lab:
 * a driver is only correct with respect to a document somebody read.
 *
 * Fill in every 0xFF marked TODO from your pre-lab section B.
 * Do not copy them from another team — the breakouts on the benches are not all
 * strapped to the same address.
 */
#ifndef IMU_H
#define IMU_H

#include <stdint.h>
#include <stdbool.h>

/* ---------------------------------------------------------------- addressing
 * The datasheet gives a 7-bit address. ST's HAL wants it shifted left by one.
 * Fill in the 7-bit value; the shift is done for you.
 */
#define IMU_ADDR_7BIT      0xFF    /* TODO pre-lab B4: 7-bit I2C address        */
#define IMU_ADDR_HAL       (IMU_ADDR_7BIT << 1)

/* ---------------------------------------------------------------- registers */
#define IMU_REG_WHO_AM_I   0xFF    /* TODO pre-lab B5: device-ID register      */
#define IMU_WHO_AM_I_VALUE 0xFF    /* TODO pre-lab B5: value it must return    */
#define IMU_REG_CTRL_ACCEL 0xFF    /* TODO pre-lab B6: accel control register  */
#define IMU_REG_CTRL_COMMON 0xFF   /* TODO pre-lab 2.2: register holding the
                                    *      auto-increment bit                  */
#define IMU_REG_OUT_ACCEL  0xFF    /* TODO pre-lab B10: first output register  */

/* ------------------------------------------------------- configuration value
 * ONE byte that sets both the output data rate and the full-scale range.
 * Build it from the register map — do not guess the range encoding, and note
 * that it may not count upwards in the order you expect (handout, final section).
 */
#define IMU_CTRL_ACCEL_VALUE 0xFF  /* TODO pre-lab C5 + B7/B8                  */

/* Bit that makes a multi-byte read auto-increment the register pointer, so one
 * burst returns one coherent sample instead of bytes from different samples. */
#define IMU_AUTO_INCREMENT_BIT 0xFF /* TODO pre-lab 2.2                        */

/* ---------------------------------------------------------------- scaling
 * mg per LSB for the range you configured above. From the sensitivity table.
 * If this does not match the configured range, every number downstream is wrong
 * by a factor of 2, 4 or 8 — and it will still look entirely plausible.
 */
#define IMU_SENS_MG_PER_LSB  0.0f  /* TODO pre-lab B9                          */

#define STANDARD_GRAVITY 9.80665f  /* m/s^2 — for the SI conversion            */

/* ---------------------------------------------------------------- interface */
typedef struct {
    int16_t raw_x, raw_y, raw_z;   /* codes straight off the wire   */
    float   mg_x,  mg_y,  mg_z;    /* converted, milli-g            */
    float   magnitude_mg;          /* sqrt(x^2+y^2+z^2) — the check  */
} imu_sample_t;

bool imu_probe(uint8_t *id_out);          /* Claim 1: is it there, is it right? */
bool imu_configure(void);                 /* range + ODR + auto-increment       */
bool imu_read(imu_sample_t *out);         /* one burst, assembled and scaled    */
float imu_mg_to_ms2(float mg);

#endif /* IMU_H */
