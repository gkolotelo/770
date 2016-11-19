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
void controller_initPID(controller_instance_t *controllerInstance, float fMaxSumError,
                        float fPGain, float fIGain, float fDGain)
{
    controllerInstance->fControllerKp = fPGain;
    controllerInstance->fControllerKi = fIGain;
    controllerInstance->fControllerKd = fDGain;
    controllerInstance->fControllerSensorPreviousValue = 0;
    controllerInstance->fControllerErrorSum = 0;
    controllerInstance->fControllerMaxSumError = fMaxSumError;
}

/**
 * @brief Sets the maximum integrative error.
 * 
 * @param controllerinstance controller_instance_t struct.
 * @param fMaxSumError Maximum error acceptable
 */
void controller_setMaxSumError(controller_instance_t *controllerInstance, float fMaxSumError)
{
    controllerInstance->fControllerMaxSumError = fMaxSumError;
}

/**
 * @brief Sets the Kp.
 * 
 * @param controllerInstance controller_instance_t struct.
 * @param fPGain Proportional constant.
 */
void controller_setKp(controller_instance_t *controllerInstance, float fPGain)
{
    controllerInstance->fControllerKp = fPGain;
}

/**
 * @brief Sets the Ki.
 * 
 * @param controllerInstance controller_instance_t struct.
 * @param fIGain Integrative constant.
 */
void controller_setKi(controller_instance_t *controllerInstance, float fIGain)
{
    controllerInstance->fControllerKi = fIGain;
}

/**
 * @brief Sets the Kd.
 * 
 * @param controllerInstance controller_instance_t struct.
 * @param fDGain Derivative constant.
 */
void controller_setKd(controller_instance_t *controllerInstance, float fDGain)
{
    controllerInstance->fControllerKd = fDGain;
}

/**
 * @brief Updates the active controller and retrieves the actuation value
 * @details [long description]
 * 
 * @param controllerInstance controller_instance_t struct.
 * @param fSensorValue Value from sensor.
 * @param fReferenceValue Reference value.
 * @return Actuation value.
 */
float controller_PIDUpdate(controller_instance_t *controllerInstance, float fSensorValue, float fReferenceValue)
{
    //if(fReferenceValue < 0.06) return 0;
    float fPterm, fIterm, fDterm;
    float fError, fDifference, fItemp;

    fError = fReferenceValue - fSensorValue;

    /* Proportional */
    fPterm = controllerInstance->fControllerKp * fError;

    /*  Integrative */
    fItemp = controllerInstance->fControllerErrorSum + fError;
    if(abs(fItemp) < controllerInstance->fControllerMaxSumError)
        controllerInstance->fControllerErrorSum = fItemp;
    fIterm = controllerInstance->fControllerKi * controllerInstance->fControllerErrorSum;

    /*  Derivative  */
    fDifference = controllerInstance->fControllerSensorPreviousValue - fSensorValue;
    controllerInstance->fControllerSensorPreviousValue = fSensorValue;
    fDterm = controllerInstance->fControllerKd * fDifference;

    return (fPterm + fIterm + fDterm);
}

