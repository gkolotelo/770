/**
 * @file vsense.h
 * @author Guilherme Kairalla Kolotelo
 * @author Bruno de Souza Ferreira
 * @version 1.0
 * @date 07 Oct 2016
 * @brief File containing the definition of methods for interacting with the sense resistors.
 */

#ifndef SOURCES_VSENSE_H_
#define SOURCES_VSENSE_H_

/**
 * @brief Sets up pin configuration for voltage sense.
 * 
 */
void vsense_initVsense();

/**
 * @brief Returns raw ADC reading from VSense1 pin.
 *
 * @return Raw ADC reading from VSense1 pin
 */
uint16_t vsense_getRawV1();

/**
 * @brief Returns raw ADC reading from VSense2 pin.
 *
 * @return Raw ADC reading from VSense2 pin
 */
uint16_t vsense_getRawV2();

/**
 * @brief Returns voltage reading from VSense1 pin.
 *
 * @return Voltage reading from VSense1 pin
 */
float vsense_getV1();

/**
 * @brief Returns voltage reading from VSense2 pin.
 *
 * @return Voltage reading from VSense2 pin.
 */
float vsense_getV2();

/**
 * @brief Returns system voltage the Vsense1 pin. Same as getV1().
 *
 * @return System voltage reading.
 */
float vsense_getSystemVoltage();

/**
 * @brief Returns system current in mA.
 *
 * @return System current in mA.
 */
float vsense_getCurrent();

/**
 * @brief Returns system power in mW.
 * 
 * @return System power in mW.
 */
float vsense_getPower();

#endif /* SOURCES_VSENSE_H_ */
