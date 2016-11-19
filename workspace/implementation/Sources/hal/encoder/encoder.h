/**
 * @file encoder.h
 * @author Guilherme Kairalla Kolotelo
 * @author Bruno de Souza Ferreira
 * @version 1.1
 * @date 20 Jun 2016
 * @date 27 Sep 2016
 * @brief File containing the definition of methods for the reading of an incremental encoder.
 */

#include <MKL25Z4.h>

#ifndef SOURCES_ENCODER_H_
#define SOURCES_ENCODER_H_

/**
 * @brief driver_instance_t Struct containing specific data for a motor driver instance.
 */
typedef struct {
	/* Config section */
	char cEncoderInstance;
	uint8_t uiEncoderPortInstance;
	uint8_t uiEncoderPinNumber;
	uint8_t uiEncoderPortAlt;
	uint8_t uiEncoderTpmInstance;
	uint8_t uiEncoderTpmClkinSrc;
    /* Encoder Hardware Setup section */
	uint16_t uiEncoderMaxPulseCount;
	uint16_t uiEncoderPulseCount;
	uint32_t uiEncoderAcqPeriodUs;

	/* Data section */
	float uiEncoderPulsesPerSecond;

} encoder_instance_t;


///**
// * @brief Channel O IRQ handler
// * 
// */
//extern void ENCODER_CHO_IRQ_HANDLER();

/**
 * @brief Initializes the encoder for an incremental encoder.
 * 
 * @param encoderInstance encoder_instance_t struct.
 */
void encoder_initEncoder(encoder_instance_t encoderInstance);


/**
 * @brief Enables the counter.
 * 
 * @param encoderInstance encoder_instance_t struct.
 */
void encoder_enableCounter(encoder_instance_t encoderInstance);


/**
 * @brief Disables the counter
 * 
 * @param encoderInstance encoder_instance_t struct.
 */
void encoder_disableCounter(encoder_instance_t encoderInstance);


/**
 * @brief Resets the counter.
 * 
 * @param encoderInstance encoder_instance_t struct.
 */
void encoder_resetCounter(encoder_instance_t encoderInstance);


///**
// * @brief Enables the interrupt on Channel O.
// * 
// * @param encoderInstance encoder_instance_t struct.
//*/
//void encoder_enableChOInterrupt(encoder_instance_t encoderInstance);
//
//
///**
// * @brief Disables the interrupt on channel O.
// * 
// * @param encoderInstance encoder_instance_t struct.
// */
//void encoder_disableChOInterrupt(encoder_instance_t encoderInstance);


/**
 * @brief Takes a measurement of speed, direction and position.
 * 
 * @param encoderInstance encoder_instance_t struct.
 */
void encoder_takeMeasurement(encoder_instance_t *encoderInstance);


/* Data retrieval methods */


/**
 * @brief Returns the angular position of the encoder in degrees.
 * 
 * @param encoderInstance encoder_instance_t struct.
 * @return Angular position of the encoder in degrees.
 */
float encoder_getAngularPositionDegree(encoder_instance_t encoderInstance);


/**
 * @brief Returns the angular position of the encoder in radians.
 * 
 * @param encoderInstance encoder_instance_t struct.
 * @return Angular position of the encoder in radians.
 */
float encoder_getAngularPositionRad(encoder_instance_t encoderInstance);


/**
 * @brief Returns the angular velocity of the encoder in pulses per second.
 * 
 * @param encoderInstance encoder_instance_t struct.
 * @return Angular velocity of the encoder in pps.
 */
float encoder_getAngularVelocity(encoder_instance_t encoderInstance);


/**
 * @brief Returns the angular velocity of the encoder in Rad/s.
 * 
 * @param encoderInstance encoder_instance_t struct.
 * @return Angular velocity of the encoder in Rad/s.
 */
float encoder_getAngularVelocityRad(encoder_instance_t encoderInstance);


/**
 * @brief Returns the angular velocity of the encoder in RPM.
 * 
 * @param encoderInstance encoder_instance_t struct.
 * @return Angular velocity of the encoder in RPM.
 */
float encoder_getAngularVelocityRPM(encoder_instance_t encoderInstance);

#endif /* SOURCES_ENCODER_H_ */
