/**
 * @file controller.c
 * @author Guilherme Kairalla Kolotelo
 * @author Bruno de Souza Ferreira
 * @version 1.1
 * @date 20 Jun 2016
 * @date 26 Sep 2016
 * @brief File containing the methods implementing a PID controller.
 */


/* System includes */
#include <stdlib.h>

/* Project includes */
#include "controller.h"

/**
 * @brief Initializes the controller with safe values.
 * 
 * @param controllerInstance controller_instance_t struct.
 */
void controller_initPID(controller_instance_t *controllerInstance)
{
    controllerInstance->dControllerKp = 0;
    controllerInstance->dControllerKi = 0;
    controllerInstance->dControllerKd = 0;
    controllerInstance->dControllerSensorPreviousValue = 0;
    controllerInstance->dControllerErrorSum = 0;
    controllerInstance->dControllerMaxSumError = 0;
}

/**
 * @brief Sets the maximum integrative error.
 * 
 * @param controllerinstance controller_instance_t struct.
 * @param dMaxSumError Maximum error acceptable
 */
void controller_setMaxSumError(controller_instance_t *controllerInstance, double dMaxSumError)
{
    controllerInstance->dControllerMaxSumError = dMaxSumError;
}

/**
 * @brief Sets the Kp.
 * 
 * @param controllerInstance controller_instance_t struct.
 * @param dPGain Proportional constant.
 */
void controller_setKp(controller_instance_t *controllerInstance, double dPGain)
{
    controllerInstance->dControllerKp = dPGain;
}

/**
 * @brief Sets the Ki.
 * 
 * @param controllerInstance controller_instance_t struct.
 * @param dIGain Integrative constant.
 */
void controller_setKi(controller_instance_t *controllerInstance, double dIGain)
{
    controllerInstance->dControllerKi = dIGain;
}

/**
 * @brief Sets the Kd.
 * 
 * @param controllerInstance controller_instance_t struct.
 * @param dDGain Derivative constant.
 */
void controller_setKd(controller_instance_t *controllerInstance, double dDGain)
{
    controllerInstance->dControllerKd = dDGain;
}

/**
 * @brief Updates the active controller and retrieves the actuation value
 * @details [long description]
 * 
 * @param controllerInstance controller_instance_t struct.
 * @param dSensorValue Value from sensor.
 * @param dReferenceValue Reference value.
 * @return Actuation value.
 */
double controller_PIDUpdate(controller_instance_t *controllerInstance, double dSensorValue, double dReferenceValue)
{
    if(dReferenceValue < 20) return 0;
    double dPterm, dIterm, dDterm;
    double dError, dDifference, dItemp;

    dError = dReferenceValue - dSensorValue;

    /* Proportional */
    dPterm = controllerInstance->dControllerKp * dError;

    /*  Integrative */
    dItemp = controllerInstance->dControllerErrorSum + dError;
    if(abs(dItemp) < controllerInstance->dControllerMaxSumError)
        controllerInstance->dControllerErrorSum = dItemp;
    dIterm = controllerInstance->dControllerKi * controllerInstance->dControllerErrorSum;

    /*  Derivative  */
    dDifference = controllerInstance->dControllerSensorPreviousValue - dSensorValue;
    controllerInstance->dControllerSensorPreviousValue = dSensorValue;
    dDterm = controllerInstance->dControllerKd * dDifference;

    return (dPterm + dIterm + dDterm);
}

