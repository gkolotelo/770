/**
 * @file encoder.h
 * @author Guilherme Kairalla Kolotelo
 * @author Bruno de Souza Ferreira
 * @version 1.1
 * @date 20 Jun 2016
 * @date 27 Sep 2016
 * @brief File containing the definition of methods for the reading of an incremental encoder.
 */


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
	uint8_t uiEncoderPulseCount;
	uint32_t uiEncoderAcqPeriodUs;

	/* Data section */
	uint32_t uiEncoderPulsesPerSecond = 0;

} encoder_instance_t;


/**
 * @brief Channel O IRQ handler
 * 
 */
extern void ENCODER_CHO_IRQ_HANDLER();

/**
 * @brief Initializes the encoder for an incremental encoder.
 * 
 * @param encoder_instance encoder_instance_t struct.
 */
void encoder_initEncoder(encoder_instance_t *encoder_instance);


/**
 * @brief Enables the counter.
 * 
 * @param encoder_instance encoder_instance_t struct.
 */
void encoder_enableCounter(encoder_instance_t *encoder_instance);


/**
 * @brief Disables the counter
 * 
 * @param encoder_instance encoder_instance_t struct.
 */
void encoder_disableCounter(encoder_instance_t *encoder_instance);


/**
 * @brief Resets the counter.
 * 
 * @param encoder_instance encoder_instance_t struct.
 */
void encoder_resetCounter(encoder_instance_t *encoder_instance);


/**
 * @brief Enables the interrupt on Channel O.
 * 
 * @param encoder_instance encoder_instance_t struct.
*/
void encoder_enableChOInterrupt(encoder_instance_t *encoder_instance);


/**
 * @brief Disables the interrupt on channel O.
 * 
 * @param encoder_instance encoder_instance_t struct.
 */
void encoder_disableChOInterrupt(encoder_instance_t *encoder_instance);


/**
 * @brief Takes a measurement of speed, direction and position.
 * 
 * @param encoder_instance encoder_instance_t struct.
 */
void encoder_takeMeasurement(encoder_instance_t *encoder_instance);


/* Data retrieval methods */


/**
 * @brief Returns the angular position of the encoder in degrees.
 * 
 * @param encoder_instance encoder_instance_t struct.
 * @return Angular position of the encoder in degrees.
 */
double encoder_getAngularPositionDegree(encoder_instance_t *encoder_instance);


/**
 * @brief Returns the angular position of the encoder in radians.
 * 
 * @param encoder_instance encoder_instance_t struct.
 * @return Angular position of the encoder in radians.
 */
double encoder_getAngularPositionRad(encoder_instance_t *encoder_instance);


/**
 * @brief Returns the angular velocity of the encoder in pulses per second.
 * 
 * @param encoder_instance encoder_instance_t struct.
 * @return Angular velocity of the encoder in pps.
 */
double encoder_getAngularVelocity(encoder_instance_t *encoder_instance);


/**
 * @brief Returns the angular velocity of the encoder in Rad/s.
 * 
 * @param encoder_instance encoder_instance_t struct.
 * @return Angular velocity of the encoder in Rad/s.
 */
double encoder_getAngularVelocityRad(encoder_instance_t *encoder_instance);


/**
 * @brief Returns the angular velocity of the encoder in RPM.
 * 
 * @param encoder_instance encoder_instance_t struct.
 * @return Angular velocity of the encoder in RPM.
 */
double encoder_getAngularVelocityRPM(encoder_instance_t *encoder_instance);

#endif /* SOURCES_ENCODER_H_ */
