/* sensor_console.h — Laboratory 1 register console
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

/* Bus scan range — 7-bit addresses. 0x08..0x77 are the generally usable ones. */
#define SCAN_FIRST_ADDR 0x08
#define SCAN_LAST_ADDR  0x77

/* Default 7-bit address the console talks to. Students may change it at runtime
 * with the `addr` command; nothing here is compiled in as an assumption. */
#define DEFAULT_ADDR_7BIT 0x6A

void console_init(void);      /* print the banner */
void console_poll(void);      /* call from the main loop; non-blocking-ish */

#endif /* SENSOR_CONSOLE_H */
