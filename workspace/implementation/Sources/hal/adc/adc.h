/**
 * @file adc.h
 * @author msoliveira
 * @author Guilherme Kairalla Kolotelo
 * @author Bruno de Souza Ferreira
 * @version 1.1
 * @date 06 Jun 2016
 * @date 27 Sep 2016
 * @brief File containing the methods for interacting with the ADC module.
 */

#ifndef SOURCES_ADC_H_
#define SOURCES_ADC_H_


/**
 * @brief configure ADC module
 */
void adc_initAdc(void);


/**
 * @brief init a conversion from A to D
 * @param adcChannel ADC channel to convert. Given in bytes.
 */
void adc_startConversion(uint8_t adcChannel);


/**
 * @brief check if conversion is done
 * @return 1 if complete, 0 otherwise
 */
int adc_isAdcDone(void);


/**
 * @brief retrieve converted value
 * @return Converted value
 */
int adc_getValue(void);

#endif /* SOURCES_ADC_H_ */
