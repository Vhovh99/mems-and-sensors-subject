/* main_console.c — Laboratory 1 console: what to add to CubeMX's main.c
 *
 * INSTRUCTOR FIRMWARE. Build once, flash all boards.
 *
 *   #include "sensor_console.h"
 *
 *   int main(void) {
 *       HAL_Init();
 *       SystemClock_Config();
 *       MX_GPIO_Init();
 *       MX_I2C1_Init();
 *       MX_USART2_UART_Init();
 *
 *       console_init();
 *       while (1) {
 *           console_poll();
 *       }
 *   }
 *
 * Nothing else is required. No printf retargeting: the console writes through
 * HAL_UART_Transmit directly, so there is no _write() or syscalls.c to configure.
 */
