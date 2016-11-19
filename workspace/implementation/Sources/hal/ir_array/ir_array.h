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

/* Global variables */
uint16_t uiIrReadings[6] = {0, 0, 0, 0, 0, 0};
float fIrNormalizedReadings[6] = {0, 0, 0, 0, 0, 0};
uint16_t uiIrMinreadings[6] = {0, 0, 0, 0, 0, 0};
uint16_t uiIrMaxreadings[6] = {65535, 65535, 65535, 65535, 65535, 65535};
// No need to calculate x every interpolation, just sum the index: x[i]+1, x[i]+2, etc...
// Also t = x in this case, so we can use dcx in place of t.
float const fcx[10] = { 0.0, 0.111111, 0.222222, 0.333333, 0.444444,
						 0.555556, 0.666667, 0.777778, 0.888889, 1.0 };

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

/**
 * @brief Normalizes the IR sensor readings according to min and max values from calibration.
 * 
 * @param uiIrVector Array pointer to store raw sensor measurements
 * @param fIrNormalizedReadings Array pointer to store raw normalized measurements
 */
void ir_array_normalizeReadings(uint16_t* uiIrVector, float* fIrNormalizedReadings);

/**
 * @brief Executes the calibration routine for all LED/sensor pairs.
 * @details Store minimum and maximum reading values on uiIrMinreadings and uiIrMaxreadings respectively.
 * 
 * @param uiIrVector Array pointer to store raw sensor measurements
 */
void ir_array_calibrate(uint16_t* uiIrVector);

/**
 * @brief Implements the uniform Catmull-Rom spline algorithm between point p1 and p2.
 * @details Uniform Catmull-Rom using float precision data-type given 4 points and position t.
 * 
 * @param p0 Point 0
 * @param p1 Point 1
 * @param p2 Point 2
 * @param p3 Point 3
 * @param t Position
 * @return Returns the interpolated points fot position t between p1 and p2.
 */
float ir_array_catmullRom(float p0, float p1, float p2, float p3, float t);

/**
 * @brief Executes the Catmull-Rom algorithm for all pairs of sensors (0-1, 1-2, 2-3, 3-4, 4-5).
 * @details Generates a 46 point vector from position 0 to position 5 (sensor 0 to 5) with 9 
 * control points between each sensor:
 * sensor:		0			  1		 ...      2						5
 * position:	0, 1, ..., 8, 9, 10, ..., 17, 18, 19, ..........44, 45
 * 
 * @param y Array pointer to store interpolated values
 * @param y0 sensor 0 normalized measurement
 * @param y1 sensor 1 normalized measurement
 * @param y2 sensor 2 normalized measurement
 * @param y3 sensor 3 normalized measurement
 * @param y4 sensor 4 normalized measurement
 * @param y5 sensor 5 normalized measurement
 */
void ir_array_interpolate(float* y, float y0, float y1, float y2, float y3, float y4, float y5);

/**
 * @brief Evaluates the position of the trough, or occurence of a command bar.
 * @details Evaluates the position of the trough(pos), or occurence of a command bar(-1). If both are 
 * inexistent returns invalid (-2).
 * 
 * @param y0 sensor 0 normalized measurement
 * @param y1 sensor 1 normalized measurement
 * @param y2 sensor 2 normalized measurement
 * @param y3 sensor 3 normalized measurement
 * @param y4 sensor 4 normalized measurement
 * @param y5 sensor 5 normalized measurement
 * @return Trough Pos or -1 (command bar) or -2 (invalid/other)
 */
float ir_array_minMaxValuePosition(float y0, float y1, float y2, float y3, float y4, float y5);

/**
 * @brief Get position of trought or occurence of command bar.
 * @details [long description]
 * 
 * @param  [description]
 * @return [description]
 */
float ir_array_getPosition();

#endif /* SOURCES_IR_ARRAY_H_ */