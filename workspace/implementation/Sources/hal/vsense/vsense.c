/**
 * @file vsense.c
 * @author Guilherme Kairalla Kolotelo
 * @author Bruno de Souza Ferreira
 * @version 1.0
 * @date 30 Sep 2016
 * @brief File containing the methods for interacting with for interacting with the sense resistors.
 */

#include <MKL25Z4.h>
#include "hal/adc/adc.h"
#include "fsl_gpio_driver.h"
#include "fsl_gpio_hal.h"
#include "hal/target_definitions.h"
#include "fsl_clock_manager.h"
#include "hal/util/util.h"

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

uint16_t vsense_getRawV1()
{
	adc_startConversion(VSENSE1_CH_NUMBER);
	for(int i = 0; i < ADC_10MS_MULTIPLE_WAIT_PERIOD; i++) util_genDelay10ms();
	if(adc_isAdcDone()) return adc_getValue();
	else return 0;
}

uint16_t vsense_getRawV2()
{
	adc_startConversion(VSENSE2_CH_NUMBER);
	for(int i = 0; i < ADC_10MS_MULTIPLE_WAIT_PERIOD; i++) util_genDelay10ms();
	if(adc_isAdcDone()) return adc_getValue();
	else return 0;
}

float vsense_getV1()
{
	return (float)VSENSE1_CORRECTION_FACTOR*(float)vsense_getRawV1();
}

float vsense_getV2()
{
	return (float)VSENSE2_CORRECTION_FACTOR*(float)vsense_getRawV2();
}

float vsense_getSystemVoltage()
{
	return vsense_getV1();
}

float vsense_getCurrent()
{
	float v1, v2;
	v1 = vsense_getV1();
	v2 = vsense_getV2();
	if(v1 == 0 || v2 == 0) return 0;
	return (v1 - v2)/(float)VSENSE_RESISTOR_VALUE;
}

float vsense_getPower()
{
	return vsense_getSystemVoltage()*vsense_getCurrent();
}
