/* lab2_config.h — Laboratory 2 · THE FILE YOU EDIT
 * ============================================================================
 *
 * This is the whole of your authorship in Laboratory 2: ONE constant, changed
 * once, rebuilt, reflashed. That is the point. Lab 2 is not about writing
 * firmware — it is about owning the toolchain, so that in Laboratory 3 the
 * build is not the reason your measurement failed.
 *
 * Everything else about the capture — how many samples, which ODR, whether the
 * second low-pass filter is on — you set at runtime from the serial console.
 * That is deliberate: three rebuilds would cost bench time and teach nothing
 * the first rebuild did not.
 *
 * ---------------------------------------------------------------------------
 * WHAT THE CONSTANT IS
 *
 * LAB2_CTRL1_XL is the byte written to the accelerometer's CTRL1_XL register at
 * start-up. On the ISM330DHCX that one byte carries three of the decisions from
 * Lecture 3 (DS13012 Rev 6, and VERIFY IT against the revision in your hand):
 *
 *     bits 7:4   ODR_XL      output data rate
 *     bits 3:2   FS_XL       full-scale range
 *     bit  1     LPF2_XL_EN  the second low-pass filter — 0 after reset
 *     bit  0     -           must be written 0
 *
 * ODR_XL           FS_XL                    Useful whole bytes, FS = +/-2 g:
 *   0010 =  26 Hz    00 = +/-2 g              0x20   26 Hz, LPF2 off
 *   0011 =  52 Hz    01 = +/-16 g             0x30   52 Hz, LPF2 off
 *   0100 = 104 Hz    10 = +/-4 g              0x40  104 Hz, LPF2 off  <- ships
 *   0101 = 208 Hz    11 = +/-8 g              0x42  104 Hz, LPF2 ON
 *   0110 = 416 Hz                             0x50  208 Hz, LPF2 off
 *                                             0x60  416 Hz, LPF2 off
 *
 * Note that FS_XL does NOT ascend: 01 is +/-16 g, not +/-4 g. Read the table;
 * do not infer it. Every number you compute afterwards depends on it.
 *
 * ---------------------------------------------------------------------------
 * WHAT YOU DO IN STAGE 1
 *
 * The board arrives flashed with 0x40 — 104 Hz, +/-2 g, and the anti-alias
 * filter OFF, which is the configuration Lecture 3 spent twenty minutes on.
 *
 *   1. Capture stationary data as shipped, and write down the standard
 *      deviation. (Handout stage 2.)
 *   2. Change the line below from 0x40 to 0x42 — LPF2_XL_EN = 1.
 *   3. Rebuild. Reflash. The banner will print the new value; if it still says
 *      0x40 you flashed the old binary, which is itself worth knowing.
 *   4. Capture again. The standard deviation should FALL, because you have
 *      narrowed the bandwidth without changing the sample rate.
 *
 * That last sentence is the whole of Lecture 3 in one measurement you made
 * yourself. Do not skip writing down both numbers.
 */
#ifndef LAB2_CONFIG_H
#define LAB2_CONFIG_H

/* ==========================================================================
 *  >>>  CHANGE THIS ONE LINE IN STAGE 1, AND NOTHING ELSE IN THIS FILE  <<<
 * ========================================================================== */

#define LAB2_CTRL1_XL   0x40

/* ==========================================================================
 *  Below here is instructor configuration. Leave it alone.
 * ========================================================================== */

/* 7-bit I2C address. 0x6A with SA0/SDO to ground, 0x6B with it to VDDIO.
 * Breakout boards strap that pin differently, so the console's `scan` command
 * is the authority, not this line. */
#define LAB2_ADDR_7BIT      0x6A

/* Register map — ISM330DHCX, DS13012 Rev 6. Verify against your revision. */
#define REG_WHO_AM_I        0x0F
#define REG_CTRL1_XL        0x10
#define REG_CTRL3_C         0x12
#define REG_CTRL8_XL        0x17
#define REG_OUTX_L_A        0x28
#define WHO_AM_I_EXPECTED   0x6B      /* NB: also one of the bus addresses. */

/* Largest capture the firmware will accept in one go. A capture is streamed as
 * it is taken, never buffered, so this limit is about the student's patience
 * and their terminal's scrollback, not about RAM. 4000 samples at 104 Hz is
 * about 38 s, which is long enough for a stable standard deviation. */
#define LAB2_MAX_SAMPLES    4000

/* Default number of samples when `cap` is given no argument. */
#define LAB2_DEFAULT_N      2000

#endif /* LAB2_CONFIG_H */
