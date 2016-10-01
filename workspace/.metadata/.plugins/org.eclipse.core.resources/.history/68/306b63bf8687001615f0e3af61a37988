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
	double uiEncoderPulsesPerSecond = 0;

} encoderInstance_t;


///**
// * @brief Channel O IRQ handler
// * 
// */
//extern void ENCODER_CHO_IRQ_HANDLER();

/**
 * @brief Initializes the encoder for an incremental encoder.
 * 
 * @param encoderInstance encoderInstance_t struct.
 */
void encoder_initEncoder(encoderInstance_t *encoderInstance);


/**
 * @brief Enables the counter.
 * 
 * @param encoderInstance encoderInstance_t struct.
 */
void encoder_enableCounter(encoderInstance_t *encoderInstance);


/**
 * @brief Disables the counter
 * 
 * @param encoderInstance encoderInstance_t struct.
 */
void encoder_disableCounter(encoderInstance_t *encoderInstance);


/**
 * @brief Resets the counter.
 * 
 * @param encoderInstance encoderInstance_t struct.
 */
void encoder_resetCounter(encoderInstance_t *encoderInstance);


///**
// * @brief Enables the interrupt on Channel O.
// * 
// * @param encoderInstance encoderInstance_t struct.
//*/
//void encoder_enableChOInterrupt(encoderInstance_t *encoderInstance);
//
//
///**
// * @brief Disables the interrupt on channel O.
// * 
// * @param encoderInstance encoderInstance_t struct.
// */
//void encoder_disableChOInterrupt(encoderInstance_t *encoderInstance);


/**
 * @brief Takes a measurement of speed, direction and position.
 * 
 * @param encoderInstance encoderInstance_t struct.
 */
void encoder_takeMeasurement(encoderInstance_t *encoderInstance);


/* Data retrieval methods */


/**
 * @brief Returns the angular position of the encoder in degrees.
 * 
 * @param encoderInstance encoderInstance_t struct.
 * @return Angular position of the encoder in degrees.
 */
double encoder_getAngularPositionDegree(encoderInstance_t *encoderInstance);


/**
 * @brief Returns the angular position of the encoder in radians.
 * 
 * @param encoderInstance encoderInstance_t struct.
 * @return Angular position of the encoder in radians.
 */
double encoder_getAngularPositionRad(encoderInstance_t *encoderInstance);


/**
 * @brief Returns the angular velocity of the encoder in pulses per second.
 * 
 * @param encoderInstance encoderInstance_t struct.
 * @return Angular velocity of the encoder in pps.
 */
double encoder_getAngularVelocity(encoderInstance_t *encoderInstance);


/**
 * @brief Returns the angular velocity of the encoder in Rad/s.
 * 
 * @param encoderInstance encoderInstance_t struct.
 * @return Angular velocity of the encoder in Rad/s.
 */
double encoder_getAngularVelocityRad(encoderInstance_t *encoderInstance);


/**
 * @brief Returns the angular velocity of the encoder in RPM.
 * 
 * @param encoderInstance encoderInstance_t struct.
 * @return Angular velocity of the encoder in RPM.
 */
double encoder_getAngularVelocityRPM(encoderInstance_t *encoderInstance);

#endif /* SOURCES_ENCODER_H_ */
