/* lab2_capture.h — Laboratory 2 capture console
 * Target sensor: ST ISM330DHCXTR (iNEMO 6-axis IMU), datasheet DS13012 Rev 6.
 *
 * Laboratory 2 is "sampling, noise and filtering". Its job is to let a student
 * measure, on real silicon, the three things Lecture 3 asserted:
 *
 *   1. The noise you get depends on the BANDWIDTH you chose, not on the number
 *      of bits you bought. Sigma should scale as sqrt(ODR).
 *   2. A requested sample rate is not the achieved sample rate. A polling loop
 *      with a delay in it runs slow, always in the same direction.
 *   3. Filtering afterwards buys noise back at the price of bandwidth and
 *      delay — and buys nothing at all against an alias.
 *
 * DESIGN RULES, inherited from the Laboratory 1 console and kept deliberately:
 *
 *   THIS FIRMWARE PRINTS RAW CODES AND MILLISECONDS. NEVER ENGINEERING UNITS.
 * Converting a code to milli-g with a sensitivity read off a datasheet is a
 * learning outcome (Lab1.4, retested here). If the firmware did it, the lab
 * would teach nothing.
 *
 *   THIS FIRMWARE COMPUTES NO STATISTICS.
 * No mean, no standard deviation, no filtering. Those are the analysis the
 * student does in a spreadsheet, and they are outcomes Lab2.2 to Lab2.4. The
 * one number it does report is the elapsed time of a capture, because a
 * stopwatch cannot resolve it and the point of stage 4 depends on it.
 *
 * WHAT THE STUDENT WRITES: one constant, in lab2_config.h. Nothing here.
 */
#ifndef LAB2_CAPTURE_H
#define LAB2_CAPTURE_H

void lab2_init(void);      /* configure the sensor, print the banner */
void lab2_poll(void);      /* call from the main loop */

#endif /* LAB2_CAPTURE_H */
