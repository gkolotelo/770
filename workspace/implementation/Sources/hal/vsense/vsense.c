/**
 * @file vsense.c
 * @author Guilherme Kairalla Kolotelo
 * @author Bruno de Souza Ferreira
 * @version 1.0
 * @date 30 Sep 2016
 * @date 07 Oct 2016
 * @brief File containing the methods for interacting with for interacting with the sense resistors.
 * @details Vsense systems utilizes two resistor divider networks to convert the battery voltage (vesense1)
 * and sense resistor voltage (vsense2) and acquire using the ADC. The battery voltage is used to set the
 * the maximum PWM for the motor according to a user define maximum motor voltage. The voltage differential
 * on the sense resistor allows computation of the system current and power usage at any given time.
 */

/* System includes */
#include <MKL25Z4.h>
#include "fsl_clock_manager.h"
#include "fsl_gpio_driver.h"
#include "fsl_gpio_hal.h"

/* Project includes */
#include "vsense.h"
#include "hal/target_definitions.h"
#include "hal/adc/adc.h"
#include "hal/util/util.h"

/**
 * @brief Sets up pin configuration for voltage sense.
 * 
 */
void vsense_initVsense()
{
	PORT_Type* vPortBase;
	CLOCK_SYS_EnablePortClock(VSENSE1_PORT_INSTANCE);
	vPortBase = g_portBase[VSENSE1_PORT_INSTANCE];
	PORT_HAL_SetMuxMode(vPortBase, VSENSE1_PIN_NUMBER, VSENSE_PORT_ALT);

	CLOCK_SYS_EnablePortClock(VSENSE2_PORT_INSTANCE);
	vPortBase = g_portBase[VSENSE1_PORT_INSTANCE];
	PORT_HAL_SetMuxMode(vPortBase, VSENSE2_PIN_NUMBER, VSENSE_PORT_ALT);
}

/**
 * @brief Returns raw ADC reading from VSense1 pin.
 *
 * @return Raw ADC reading from VSense1 pin
 */
uint16_t vsense_getRawV1()
{
	adc_startConversion(VSENSE1_CH_NUMBER);
	for(int i = 0; i < ADC_10MS_MULTIPLE_WAIT_PERIOD; i++) util_genDelay10ms();
	if(adc_isAdcDone()) return adc_getValue();
	else return 0;
}

/**
 * @brief Returns raw ADC reading from VSense2 pin.
 *
 * @return Raw ADC reading from VSense2 pin
 */
uint16_t vsense_getRawV2()
{
	adc_startConversion(VSENSE2_CH_NUMBER);
	for(int i = 0; i < ADC_10MS_MULTIPLE_WAIT_PERIOD; i++) util_genDelay10ms();
	if(adc_isAdcDone()) return adc_getValue();
	else return 0;
}

/**
 * @brief Returns voltage reading from VSense1 pin.
 *
 * @return Voltage reading from VSense1 pin
 */
float vsense_getV1()
{
	return (float)VSENSE1_CORRECTION_FACTOR*(float)vsense_getRawV1();
}

/**
 * @brief Returns voltage reading from VSense2 pin.
 *
 * @return Voltage reading from VSense2 pin.
 */
float vsense_getV2()
{
	return (float)VSENSE2_CORRECTION_FACTOR*(float)vsense_getRawV2();
}

/**
 * @brief Returns system voltage the Vsense1 pin. Same as getV1().
 *
 * @return System voltage reading.
 */
float vsense_getSystemVoltage()
{
	return vsense_getV1();
}

/**
 * @brief Returns system current in mA.
 *
 * @return System current in mA.
 */
float vsense_getCurrent()
{
	float fmeas1, fmeas2;
	for(int i = 0; i < 20; i++)
	{
		fmeas1 += vsense_getV1();
	}
	fmeas1 = fmeas1/20;
	for(int i = 0; i < 20; i++)
	{
		fmeas2 += vsense_getV2();
	}
	fmeas2 = fmeas2/20;
	return (fmeas1 - fmeas2)/(float)VSENSE_RESISTOR_VALUE;
}

/**
 * @brief Returns system power in mW.
 * 
 * @return System power in mW.
 */
float vsense_getPower()
{
	return vsense_getSystemVoltage()*vsense_getCurrent();
}
