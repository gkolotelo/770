/**
 * @file ir_array.h
 * @author Guilherme Kairalla Kolotelo
 * @author Bruno de Souza Ferreira
 * @version 1.1
 * @date 27 Jun 2016
 * @date 07 Oct 2016
 * @brief File containing the definition of methods for interacting with an IR array .
 */

#ifndef SOURCES_IR_ARRAY_H_
#define SOURCES_IR_ARRAY_H_

uint16_t uiIrReadings[6] = {0, 0, 0, 0, 0, 0};
double dIrNormalizedReadings[6] = {0, 0, 0, 0, 0, 0};
uint16_t uiIrMinreadings[6] = {0, 0, 0, 0, 0, 0};
uint16_t uiIrMaxreadings[6] = {65535, 65535, 65535, 65535, 65535, 65535};

/**
 * @brief Initializes IR Array.
 * 
 */
void ir_array_initArray();

/**
 * @brief Turns on a single LED.
 * 
 * @param uiLedInstance LED index [0-5].
 */
void ir_array_ledSingleOn(uint8_t uiLedInstance);

/**
 * @brief Turns on all LEDS of the array.
 *
 */
void ir_array_ledArrayOn();

/**
 * @brief Turns off a single LED.
 * 
 * @param uiLedInstance LED index [0-5].
 */
void ir_array_ledSingleOff(uint8_t uiLedInstance);

/**
 * @brief Turns off all LEDS of the array.
 *
 */
void ir_array_ledArrayOff();

/**
 * @brief Takes a measurement of a single LED/sensor pair.
 * 
 * @param uiIrChannelInstance LED index [0-5].
 * @return Raw sensor measurement
 */
uint16_t ir_array_takeSingleMeasurement(uint8_t uiIrChannelInstance);

/**
 * @brief Takes a measurement of all LED/sensor pairs.
 * 
 * @param uiIrVector Array pointer to store raw sensor measurements
 */
void ir_array_takeMeasurement();

#endif /* SOURCES_IR_ARRAY_H_ */