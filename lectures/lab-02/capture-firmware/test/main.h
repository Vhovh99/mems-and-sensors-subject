/* main.h — HAL stub, host build only. Never compiled for the target.
 *
 * Just enough of the CubeMX/HAL surface for lab2_capture.c to compile and run
 * on a PC against a simulated ISM330DHCX, so the firmware can be tested
 * without a board. See test/README.md.
 */
#ifndef MAIN_H_STUB
#define MAIN_H_STUB
#include <stdint.h>
#include <stddef.h>

typedef enum { HAL_OK = 0, HAL_ERROR, HAL_BUSY, HAL_TIMEOUT } HAL_StatusTypeDef;
typedef struct { int dummy; } I2C_HandleTypeDef;
typedef struct { int dummy; } UART_HandleTypeDef;

#define I2C_MEMADD_SIZE_8BIT 1

uint32_t          HAL_GetTick(void);
HAL_StatusTypeDef HAL_UART_Transmit(UART_HandleTypeDef *h, uint8_t *p, uint16_t n, uint32_t t);
HAL_StatusTypeDef HAL_UART_Receive(UART_HandleTypeDef *h, uint8_t *p, uint16_t n, uint32_t t);
HAL_StatusTypeDef HAL_I2C_Mem_Read(I2C_HandleTypeDef *h, uint16_t a, uint16_t reg,
                                   uint16_t sz, uint8_t *buf, uint16_t n, uint32_t t);
HAL_StatusTypeDef HAL_I2C_Mem_Write(I2C_HandleTypeDef *h, uint16_t a, uint16_t reg,
                                    uint16_t sz, uint8_t *buf, uint16_t n, uint32_t t);
HAL_StatusTypeDef HAL_I2C_IsDeviceReady(I2C_HandleTypeDef *h, uint16_t a,
                                        uint32_t tries, uint32_t t);
#endif
