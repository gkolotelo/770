/*
 * File name: adc.h
 *
 *  Created on: 06/06/2016
 *      Author: msoliveira
 */


#ifndef SOURCES_ADC_H_
#define SOURCES_ADC_H_


/* ************************************************** */
/* Method name: 	   adc_initAadc                   */
/* Method description: configure ADC module           */
/* Input params:	   n/a 							  */
/* Output params:	   n/a 							  */
/* ************************************************** */
void adc_initAdc(void);


/* ************************************************** */
/* Method name: 	   adc_startConversion            */
/* Method description: init a conversion from D to A  */
/* Input params:	   n/a 							  */
/* Output params:	   n/a 							  */
/* ************************************************** */
void adc_startConversion(void);

/* ************************************************** */
/* Method name: 	   adc_isAdcDone                  */
/* Method description: check if conversion is done    */
/* Input params:	   n/a 							  */
/* Outpu params:	   int= 1 if complete, 0 otherwise*/
/* ************************************************** */
int adc_isAdcDone(void);

/* ************************************************** */
/* Method name: 	   adc_getValue                   */
/* Method description: retrieve converted value       */
/* Input params:	   n/a 							  */
/* Output params:	   int = Converted value          */
/* ************************************************** */
int adc_getValue(void);

#endif /* SOURCES_ADC_H_ */
