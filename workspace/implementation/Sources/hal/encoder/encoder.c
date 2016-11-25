/**
 * @file encoder.C
 * @author Guilherme Kairalla Kolotelo
 * @author Bruno de Souza Ferreira
 * @version 1.1
 * @date 20 Jun 2016
 * @date 27 Sep 2016
 * @brief File containing the methods for the reading of an incremental encoder.
 */


/* Project includes */
#include "encoder.h"
#include "hal/target_definitions.h"

/* System includes */
#include "fsl_tpm_hal.h"
#include "fsl_tpm_driver.h"
#include "fsl_gpio_driver.h"
#include "fsl_clock_manager.h"
#include "fsl_port_hal.h"
#include "fsl_gpio_hal.h"
#include "fsl_interrupt_manager.h"
#include "fsl_clock_manager.h"



/**
 * @brief Initializes the encoder for an incremental encoder.
 * 
 * @param encoderInstance encoder_instance_t struct.
 */
void encoder_initEncoder(encoder_instance_t encoderInstance)
{
	encoderInstance.uiEncoderPulsesPerSecond = 0;
	TPM_Type *tpmBase = g_tpmBase[encoderInstance.uiEncoderTpmInstance];
	PORT_Type *encoderPortBase = g_portBase[encoderInstance.uiEncoderPortInstance];

    /* Configure Channel PORTs */
    CLOCK_SYS_EnablePortClock(encoderInstance.uiEncoderPortInstance);
    PORT_HAL_SetMuxMode(encoderPortBase, encoderInstance.uiEncoderPinNumber, encoderInstance.uiEncoderPortAlt);

    /* Configure external clock source for TPM modules */
    SIM_HAL_SetTpmExternalClkPinSelMode(SIM, encoderInstance.uiEncoderTpmInstance, encoderInstance.uiEncoderTpmClkinSrc);

    /* Might be using USB serial over OpenSDA, must enable Debug Mode */
    tpm_general_config_t config=
    {
            .isDBGMode = DEBUG_MODE_ENABLE
    };
    TPM_DRV_Init(encoderInstance.uiEncoderTpmInstance, &config);

    TPM_HAL_SetClockDiv(tpmBase, kTpmDividedBy1);//REVIEW PS SETTING

    TPM_HAL_SetMod(tpmBase, encoderInstance.uiEncoderMaxPulseCount);

    TPM_HAL_ClearCounter(tpmBase);

    /* Set TPM clock to external for both channels */
    TPM_HAL_SetClockMode(tpmBase, kTpmClockSourceExternalClk);

}



/**
 * @brief Enables the counter.
 * 
 * @param encoderInstance encoder_instance_t struct.
 */
void encoder_enableCounter(encoder_instance_t encoderInstance)
{
    TPM_Type *tpmBase = g_tpmBase[encoderInstance.uiEncoderTpmInstance];
    TPM_HAL_SetClockMode(tpmBase, kTpmClockSourceExternalClk);
}


/**
 * @brief Disables the counter
 * 
 * @param encoderInstance encoder_instance_t struct.
 */
void encoder_disableCounter(encoder_instance_t encoderInstance)
{
    TPM_Type *tpmBase = g_tpmBase[encoderInstance.uiEncoderTpmInstance];
    TPM_HAL_SetClockMode(tpmBase, kTpmClockSourceNoneClk);
    encoder_resetCounter(encoderInstance);
}


/**
 * @brief Resets the counter.
 * 
 * @param encoderInstance encoder_instance_t struct.
 */
void encoder_resetCounter(encoder_instance_t encoderInstance)
{
    TPM_Type *tpmBase = g_tpmBase[encoderInstance.uiEncoderTpmInstance];
    TPM_HAL_ClearCounter(tpmBase);
}


/**
 * @brief Takes a measurement of speed, direction and position.
 * 
 * @param encoderInstance encoder_instance_t struct.
 */
void encoder_takeMeasurement(encoder_instance_t *encoderInstance)
{
	float tmp;
    TPM_Type *tpmBase = g_tpmBase[encoderInstance->uiEncoderTpmInstance];
    tmp = ((float)(1000000*TPM_HAL_GetCounterVal(tpmBase)))/((float)encoderInstance->uiEncoderAcqPeriodUs);
    encoderInstance->uiEncoderPulsesPerSecond = tmp;
    encoder_resetCounter(*encoderInstance);
}


/* Data retrieval methods */
/**
 * @brief Returns the angular velocity of the encoder in pulses per second.
 * 
 * @param encoderInstance encoder_instance_t struct.
 * @return Angular velocity of the encoder in pps.
 */
float encoder_getAngularVelocity(encoder_instance_t encoderInstance)
{
    return encoderInstance.uiEncoderPulsesPerSecond;
}


/**
 * @brief Returns the angular velocity of the encoder in Rad/s.
 * 
 * @param encoderInstance encoder_instance_t struct.
 * @return Angular velocity of the encoder in Rad/s.
 */
float encoder_getAngularVelocityRad(encoder_instance_t encoderInstance)
{
    return CONST_2PI*(encoderInstance.uiEncoderPulsesPerSecond/((float)encoderInstance.uiEncoderPulseCount));
}


/**
 * @brief Returns the angular velocity of the encoder in RPM.
 * 
 * @param encoderInstance encoder_instance_t struct.
 * @return Angular velocity of the encoder in RPM.
 */
float encoder_getAngularVelocityRPM(encoder_instance_t encoderInstance)
{
    return 60*(encoderInstance.uiEncoderPulsesPerSecond/((float)encoderInstance.uiEncoderPulseCount));
}







