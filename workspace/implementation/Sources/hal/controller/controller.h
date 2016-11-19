/**
 * @file controller.h
 * @author Guilherme Kairalla Kolotelo
 * @author Bruno de Souza Ferreira
 * @version 1.1
 * @date 20 Jun 2016
 * @date 26 Sep 2016
 * @brief File containing the definition of methods implementing a PID controller.
 */

#ifndef SOURCES_CONTROLLER_H_
#define SOURCES_CONTROLLER_H_

/**
 * @brief controller_instance_t Struct containing specific data for a PID controller instance.
 */
typedef struct {
	/* Config section */
	char cControllerInstance;

	/* Data section */
	float fControllerKp;
	float fControllerKi;
	float fControllerKd;
	float fControllerSensorPreviousValue;
	float fControllerErrorSum;
	float fControllerMaxSumError;

} controller_instance_t;


/**
 * @brief Initializes the controller with safe values.
 * 
 * @param controllerInstance controller_instance_t struct.
 */
void controller_initPID(controller_instance_t *controllerInstance, float fMaxSumError,
                        float fPGain, float fIGain, float fDGain);

/**
 * @brief Sets the maximum integrative error.
 * 
 * @param controllerinstance controller_instance_t struct.
 * @param fMaxSumError Maximum error acceptable
 */
void controller_setMaxSumError(controller_instance_t *controllerInstance, float fMaxSumError);

/**
 * @brief Sets the Kp.
 * 
 * @param controllerInstance controller_instance_t struct.
 * @param fPGain Proportional constant.
 */
void controller_setKp(controller_instance_t *controllerInstance, float fPGain);

/**
 * @brief Sets the Ki.
 * 
 * @param controllerInstance controller_instance_t struct.
 * @param fIGain Integrative constant.
 */
void controller_setKi(controller_instance_t *controllerInstance, float fIGain);

/**
 * @brief Sets the Kd.
 * 
 * @param controllerInstance controller_instance_t struct.
 * @param fDGain Derivative constant.
 */
void controller_setKd(controller_instance_t *controllerInstance, float fDGain);

/**
 * @brief Updates the active controller and retrieves the actuation value
 * @details [long description]
 * 
 * @param controllerInstance controller_instance_t struct.
 * @param fSensorValue Value from sensor.
 * @param fReferenceValue Reference value.
 * @return Actuation value.
 */
float controller_PIDUpdate(controller_instance_t *controllerInstance, float fSensorValue, float fReferenceValue);

#endif /* SOURCES_CONTROLLER_H_ */
