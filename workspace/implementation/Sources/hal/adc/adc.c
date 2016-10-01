/*
 * File name: adc.c
 *
 *  Created on: 06/06/2016
 *      Author: msoliveira
 */

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
#include "hal/target_definitions.h"



#define ADC_CONVERSION_DONE			1
#define ADC_CONVERSION_PROCESSING	1

#define ADC_PIN_TEMP				21U
#define ADC_PIN_VSENSE				20U
#define ADC_ALT						0U




#define ADC0_SC1A_COCO (ADC0_SC1A >> 7)

/* ************************************************** */
/* Method name: 	   adc_initAadc                   */
/* Method description: configure ADC module           */
/* Input params:	   n/a 							  */
/* Output params:	   n/a 							  */
/* ************************************************** */
void adc_initAdc(void)
{
	/* un-gate port clock*/
	SIM_SCGC6 |= SIM_SCGC6_ADC0(CGC_CLOCK_ENABLED);	//Enable clock for ADC

    /* un-gate port clock*/
    SIM_SCGC5 |= SIM_SCGC5_PORTE(CGC_CLOCK_ENABLED);

    /* set pin as ADC In */

    PORTE_PCR(ADC_PIN_VSENSE)  |= PORT_PCR_MUX(ADC_ALT);   //Voltage Sensor
    PORTE_PCR(ADC_PIN_TEMP)  |= PORT_PCR_MUX(ADC_ALT);   //Temperature Sensor

    ADC0_CFG1 |= (ADC_CFG1_ADICLK(1U) | ADC_CFG1_MODE(3U) | ADC_CFG1_ADLSMP(0U) | ADC_CFG1_ADIV(0U) | ADC_CFG1_ADLPC(0U));

	/*
	ADC_CFG1_ADICLK(1U)// bus/2 clock selection
	ADC_CFG1_MODE(3U)  // 16-bit Conversion mode selection
	ADC_CFG1_ADLSMP(0U)// Short sample time configuration
	ADC_CFG1_ADIV(0U)  // Clock Divide Select (Divide by 1)
	ADC_CFG1_ADLPC(0U) // Normal power Configuration
	*/

    ADC0_CFG2 |= (ADC_CFG2_ADLSTS(0U) | ADC_CFG2_ADHSC(0U) | ADC_CFG2_ADACKEN(0U) | ADC_CFG2_MUXSEL(0U));

	/*
	ADC_CFG2_ADLSTS(0U)  // default time
	ADC_CFG2_ADHSC(0U)   // normal conversion sequence
	ADC_CFG2_ADACKEN(0U) // disable adack clock
	ADC_CFG2_MUXSEL(0U)  // select 'a' channels
	*/

	ADC0_SC2 |= (ADC_SC2_REFSEL(0U) | ADC_SC2_DMAEN(0U) | ADC_SC2_ACFE(0U) | ADC_SC2_ADTRG(0U));

	/*
	ADC_SC2_REFSEL(0U)// reference voltage selection - external pins
	ADC_SC2_DMAEN(0U) // dma disabled
	ADC_SC2_ACREN(x) // dont care - range function
	ADC_SC2_ACFGT(x) // dont care - 0 -> Less than, 1 -> Greater Than
	ADC_SC2_ACFE(0U)  // compare function disabled
	ADC_SC2_ADTRG(0U) // When software trigger is selected, a conversion is initiated following a write to SC1A
	ADC_SC2_ADACT(x) // HW-set indicates if a conversion is being held, is cleared when conversion is done
	*/

}


/* ************************************************** */
/* Method name: 	   adc_startConversion            */
/* Method description: init a conversion from D to A  */
/* Input params:	   n/a 							  */
/* Output params:	   n/a 							  */
/* ************************************************** */
void adc_startConversion(uint8_t adcChannel)
{
	//ADC0_SC1A &= (ADC_SC1_ADCH(0b00100) | ADC_SC1_DIFF(0U) | ADC_SC1_AIEN(0U));
	ADC0_SC1A &= (ADC_SC1_ADCH(adcChannel) | ADC_SC1_DIFF(0U) | ADC_SC1_AIEN(0U));

    /*
    ADC_SC1_COCO(x) // conversion complete flag HW-set
    ADC_SC1_AIEN(0U) // conversion complete interrupt disables
	ADC_SC1_DIFF(0U) // selects single-ended conversion
	ADC_SC1_ADCH(0b00100) // selects channel, view 3.7.1.3.1 ADC0 Channel Assignment ADC0_SE4a from datasheet
	*/
}

/* ************************************************** */
/* Method name: 	   adc_isAdcDone                  */
/* Method description: check if conversion is done    */
/* Input params:	   n/a 							  */
/* Outpu params:	   int= 1 if complete, 0 otherwise*/
/* ************************************************** */
int adc_isAdcDone(void)
{
	return ADC0_SC1A_COCO; // Returns 1 if conversion is complete, 0 otherwise

}

/* ************************************************** */
/* Method name: 	   adc_getValue                   */
/* Method description: retrieve converted value       */
/* Input params:	   n/a 							  */
/* Output params:	   int = Converted value          */
/* ************************************************** */
int adc_getValue(void)
{
	return ADC0_RA; // return the register value that keeps the result of conversion
}
