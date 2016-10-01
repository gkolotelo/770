/**
 * @file ir_array.c
 * @author Guilherme Kairalla Kolotelo
 * @author Bruno de Souza Ferreira
 * @version 1.1
 * @date 27 Jun 2016
 * @date 27 Sep 2016
 * @brief File containing the methods for interacting with an IR array .
 */

#include <MKL25Z4.h>
#include "hal/adc/adc.h"
#include "fsl_gpio_driver.h"
#include "fsl_gpio_hal.h"
#include "hal/target_definitions.h"
#include "fsl_clock_manager.h"

void ir_array_initArray()
{
	PORT_Type *irPortBase;
	GPIO_Type *irGpioBase;

	/* Configure enable pins */
	for(int i = 0; i < 6; i++)
	{
		CLOCK_SYS_EnablePortClock(ADC_IRX_EN_PORT_INSTANCE[i]);
		irPortBase = g_portBase[ADC_IRX_EN_PORT_INSTANCE[i]];
		PORT_HAL_SetMuxMode(irPortBase, ADC_IRX_EN_PIN_NUMBER[i], ADC_EN_PORT_ALT);
		irGpioBase = g_gpioBase[ADC_IRX_EN_GPIO_INSTANCE[i]];
		GPIO_HAL_SetPinDir(irGpioBase, ADC_IRX_EN_PIN_NUMBER[i], kGpioDigitalOutput);
		GPIO_HAL_ClearPinOutput(irGpioBase, ADC_IRX_EN_PIN_NUMBER[i]);
	}

	/* Configure ADC pins */
	for(int i = 0; i < 6; i++)
	{
		CLOCK_SYS_EnablePortClock(ADC_IRX_ADC_PORT_INSTANCE[i]);
		irPortBase = g_portBase[ADC_IRX_ADC_PORT_INSTANCE[i]];
		PORT_HAL_SetMuxMode(irPortBase, ADC_IRX_ADC_PIN_NUMBER[i], ADC_ADC_PORT_ALT);
	}

	// What about pre calibration (Driver method)?
	// Re-do adc library
}

void ir_array_ledSingleOn(uint8_t uiLedInstance)
{
	GPIO_Type *irGpioBase = g_gpioBase[ADC_IRX_EN_GPIO_INSTANCE[uiLedInstance]];
	GPIO_HAL_SetPinOutput(irGpioBase, ADC_IRX_EN_PIN_NUMBER[uiLedInstance]);
}

void ir_array_ledArrayOn()
{
	for(int i = 0; i < 6; i++)
	{
		ir_array_ledSingleOn(i);
	}
}

void ir_array_ledSingleOff(uint8_t uiLedInstance)
{
	GPIO_Type *irGpioBase = g_gpioBase[ADC_IRX_EN_GPIO_INSTANCE[uiLedInstance]];
	GPIO_HAL_ClearPinOutput(irGpioBase, ADC_IRX_EN_PIN_NUMBER[uiLedInstance]);
}

void ir_array_ledArrayOff()
{
	for(int i = 0; i < 6; i++)
	{
		ir_array_ledSingleOff(i);
	}
}



uint16_t ir_array_takeSingleMeasurement(uint8_t uiIrChannelInstance)
{
	adc_startConversion(ADC_IRX_ADC_CH_NUMBER[uiIrChannelInstance]);
	for(int i = 0; i < ADC_10MS_MULTIPLE_WAIT_PERIOD; i++) util_genDelay10ms();
	if(adc_isAdcDone()) return adc_getValue();
	else return 0;
}


void ir_array_takeMeasurement(uint16_t* uiIrVector)
{
	for(int i = 0; i < 6; i++)
	{
		uiIrVector[i] = ir_array_takeSingleMeasurement(i);
	}
	// Return all conversions successful (within waiting time)
	// Figure out timing for each conversion
	// Play with faster conversion times and low power mode
}




