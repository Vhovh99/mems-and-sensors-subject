/* main_lab1.c — Laboratory 1
 *
 * Drop the body of main() into your CubeMX project's main.c, after
 * MX_I2C1_Init(). Keep the generated clock and peripheral init as it is.
 *
 * Expected first-run behaviour: the probe FAILS, because imu.h is full of 0xFF.
 * That is the starting point, not a bug.
 */
#include "main.h"   /* CubeMX-generated: HAL_Delay, huart2 */
#include "imu.h"
#include <stdio.h>

#define SAMPLE_COUNT   200
#define SAMPLE_PERIOD  50      /* ms — 20 Hz logging; the sensor's ODR is separate */

void lab1_run(void)
{
    uint8_t id = 0;
    imu_sample_t s;

    printf("\r\n--- Lab 1: datasheet to data ---\r\n");

    /* ---------------------------------------------------------- Claim 1 */
    if (!imu_probe(&id)) {
        printf("IMU: WHO_AM_I = 0x%02X  (expected 0x%02X)  -> FAIL\r\n",
               id, IMU_WHO_AM_I_VALUE);
        printf("Stop here. Work down the troubleshooting table IN ORDER.\r\n");
        return;                     /* refuse to report numbers we cannot trust */
    }
    printf("IMU: WHO_AM_I = 0x%02X  (expected 0x%02X)  -> OK\r\n",
           id, IMU_WHO_AM_I_VALUE);

    if (!imu_configure()) {
        printf("IMU: configuration write FAILED\r\n");
        return;
    }
    printf("IMU: configured, sensitivity = %.4f mg/LSB\r\n", IMU_SENS_MG_PER_LSB);

    /* ---------------------------------------------------------- Claim 2 */
    printf("\r\nn,raw_x,raw_y,raw_z,mg_x,mg_y,mg_z,magnitude_mg,z_ms2\r\n");

    for (int n = 1; n <= SAMPLE_COUNT; n++) {
        if (!imu_read(&s)) { printf("%d,READ_FAILED\r\n", n); continue; }

        printf("%d,%d,%d,%d,%.1f,%.1f,%.1f,%.1f,%.3f\r\n",
               n, s.raw_x, s.raw_y, s.raw_z,
               s.mg_x, s.mg_y, s.mg_z, s.magnitude_mg,
               imu_mg_to_ms2(s.mg_z));

        /* The plausibility check, in the firmware rather than in your head. */
        if (n == 1) {
            if (s.magnitude_mg < 800.0f || s.magnitude_mg > 1200.0f)
                printf("# WARNING magnitude %.0f mg is not ~1000 mg."
                       " Check the sensitivity against the configured range.\r\n",
                       s.magnitude_mg);
        }
        HAL_Delay(SAMPLE_PERIOD);
    }
    printf("--- %d samples, units in header ---\r\n", SAMPLE_COUNT);
}
