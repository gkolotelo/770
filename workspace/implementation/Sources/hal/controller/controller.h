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
	double dControllerKp;
	double dControllerKi;
	double dControllerKd;
	double dControllerSensorPreviousValue;
	double dControllerErrorSum;
	double dControllerMaxSumError;

} controller_instance_t;


/**
 * @brief Initializes the controller with safe values.
 * 
 * @param controllerInstance controller_instance_t struct.
 */
void controller_initPID(controller_instance_t *controllerInstance);

/**
 * @brief Sets the maximum integrative error.
 * 
 * @param controllerinstance controller_instance_t struct.
 * @param dMaxSumError Maximum error acceptable
 */
void controller_setMaxSumError(controller_instance_t *controllerInstance, double dMaxSumError);

/**
 * @brief Sets the Kp.
 * 
 * @param controllerInstance controller_instance_t struct.
 * @param dPGain Proportional constant.
 */
void controller_setKp(controller_instance_t *controllerInstance, double dPGain);

/**
 * @brief Sets the Ki.
 * 
 * @param controllerInstance controller_instance_t struct.
 * @param dIGain Integrative constant.
 */
void controller_setKi(controller_instance_t *controllerInstance, double dIGain);

/**
 * @brief Sets the Kd.
 * 
 * @param controllerInstance controller_instance_t struct.
 * @param dDGain Derivative constant.
 */
void controller_setKd(controller_instance_t *controllerInstance, double dDGain);

/**
 * @brief Updates the active controller and retrieves the actuation value
 * @details [long description]
 * 
 * @param controllerInstance controller_instance_t struct.
 * @param dSensorValue Value from sensor.
 * @param dReferenceValue Reference value.
 * @return Actuation value.
 */
double controller_PIDUpdate(controller_instance_t *controllerInstance, double dSensorValue, double dReferenceValue);

#endif /* SOURCES_CONTROLLER_H_ */
