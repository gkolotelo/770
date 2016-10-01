/**
 * @file hmi.c
 * @author Guilherme Kairalla Kolotelo
 * @author Bruno de Souza Ferreira
 * @version 1.1
 * @date 20 Jun 2016
 * @date 27 Sep 2016
 * @brief File containing the methods for the interaction with a host device via a serial connection.
 */



/* System includes */
#include "fsl_clock_manager.h"
#include "fsl_port_hal.h"
#include "fsl_smc_hal.h"
#include "fsl_debug_console.h"
#include "fsl_gpio_driver.h"

/* Project includes */
#include "hal/target_definitions.h"
#include "hmi.h"
#include "hal/controller/controller.h"

void hmi_initHmi()
{
	PORT_Type *hmiEnPortBase = g_portBase[HMI_UART_PORT_INSTANCE];
    /* LPSCI0 */
    CLOCK_SYS_EnablePortClock(HMI_UART_PORT_INSTANCE);
    /* UART0_RX */
    PORT_HAL_SetMuxMode(hmiEnPortBase, HMI_UART_PIN_RX, HMI_UART_PIN_ALT);
    /* UART0_TX */
    PORT_HAL_SetMuxMode(hmiEnPortBase, HMI_UART_PIN_TX, HMI_UART_PIN_ALT);

    /* Select different clock source for LPSCI */
    CLOCK_SYS_SetLpsciSrc(HMI_UART_INSTANCE, kClockLpsciSrcPllFllSel);

    /* Initialize the debug console */
    DbgConsole_Init(HMI_UART_INSTANCE, HMI_UART_BAUD, kDebugConsoleLPSCI);
}

///**
// * Method name:         hmi_receive
// * Method description:  Receives and interprets data sent from the host device.
// * Input params:        n/a
// * Output params:       n/a
// */
//void hmi_receive()
//{
//    /* Check if there are characters on buffer */
//    if(0 == UART0_BRD_S1_RDRF(HMI_UART_BASE)) return;
//    char uiReceiveCommand;
//    int iReceiveNumber;
//    SCANF("%c%d", &uiReceiveCommand, &iReceiveNumber);
//    //PRINTF("Received: %c%d\r\n", uiReceiveCommand, iReceiveNumber);
//    switch(uiReceiveCommand)
//    {
//        case 'P':
//        case 'p':
//            iReceiveNumber = abs(iReceiveNumber);
//            controller_setKp(&pidData, ((double)iReceiveNumber/10000));
//            break;
//        case 'I':
//        case 'i':
//            iReceiveNumber = abs(iReceiveNumber);
//            controller_setKi(&pidData, ((double)iReceiveNumber/10000));
//            break;
//        case 'D':
//        case 'd':
//            iReceiveNumber = abs(iReceiveNumber);
//            controller_setKd(&pidData, ((double)iReceiveNumber/10000));
//            break;
//        case 'V':
//        case 'v':
//            iReceiveNumber = abs(iReceiveNumber);
//            dReferenceVelocity = iReceiveNumber;
//            break;
//        default:
//            break;
//    }
//}


void hmi_transmitNewLine()
{
	PRINTF("\r\n");
}

void hmi_transmitS(char* string)
{
    PRINTF("%s\r\n", string);
}

void hmi_transmitSCS(char* string1, char id, char* string2)
{
    PRINTF("%s%c%s\r\n", string1, id, string2);
}

void hmi_transmitSIS(char* string1, int id, char* string2)
{
    PRINTF("%s%d%s\r\n", string1, id, string2);
}

void hmi_transmitSCSF(char* string1, char id, char* string2, float reading)
{
    PRINTF("%s%c%s%f\r\n", string1, id, string2, reading);
}

void hmi_transmitSISI(char* string1, int id, char* string2, int reading)
{
    PRINTF("%s%d%s%d\r\n", string1, id, string2, reading);
}
