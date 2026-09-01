/* sensor_console.h — Laboratory 1 register console
 * Target sensor: ST ISM330DHCXTR (iNEMO 6-axis IMU), datasheet DS13012 Rev 6.
 * The console itself is part-agnostic: it knows no register addresses.
 *
 * INSTRUCTOR FIRMWARE. Build once, flash every board before the session.
 * Students never compile anything in Laboratory 1; they drive the sensor from a
 * serial terminal and do every conversion themselves.
 *
 * Design rule, and the reason this file exists:
 *   THE CONSOLE PRINTS RAW CODES. IT NEVER PRINTS ENGINEERING UNITS.
 * Converting a code to milli-g using a sensitivity read from a datasheet is
 * learning outcome Lab1.4. If the firmware did it, the lab would teach nothing.
 */
#ifndef SENSOR_CONSOLE_H
#define SENSOR_CONSOLE_H

#include <stdint.h>

/* Set to 1 for the serial console, or 0 for debugger Watch/Live Watch. */
#define SENSOR_CONSOLE_USE_UART 0

/* Bus scan range — 7-bit addresses. 0x08..0x77 are the generally usable ones. */
#define SCAN_FIRST_ADDR 0x08
#define SCAN_LAST_ADDR  0x77

/* Default 7-bit address the console talks to.
 *
 * For the ISM330DHCX the datasheet gives SAD = 110101x: 0x6A with SDO/SA0 tied to
 * ground, 0x6B with SDO/SA0 tied to VDDIO. Breakout boards differ in how they strap
 * that pin, so this is only a starting guess — students change it at runtime with
 * `addr`, and `scan` tells them the truth. Nothing here is compiled in as an
 * assumption about the wiring.
 *
 * Note for the demonstrator: the ISM330DHCX's WHO_AM_I VALUE is also 0x6B, which is
 * the same number as one of its possible ADDRESSES. Students conflate the two every
 * year. They are unrelated. */
#define DEFAULT_ADDR_7BIT 0x6A

#if !SENSOR_CONSOLE_USE_UART
typedef struct {
    uint8_t device_count;
    uint8_t address;
    uint8_t who_am_i;
    uint8_t ctrl1_xl;
    uint8_t ctrl1_xl_request;
    uint8_t raw_bytes[6];
    int16_t raw_x;
    int16_t raw_y;
    int16_t raw_z;
    uint32_t sample_count;
    uint8_t i2c_status;       /* 0=OK, 1=error, 2=busy, 3=timeout */
} sensor_watch_t;

extern volatile sensor_watch_t sensor_watch;
#endif

void console_init(void);      /* initialize the selected mode */
void console_poll(void);      /* call continuously from the main loop */

#endif /* SENSOR_CONSOLE_H */
