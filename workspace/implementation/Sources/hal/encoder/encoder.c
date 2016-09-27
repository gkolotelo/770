/**
 * @file encoder.C
 * @author Guilherme Kairalla Kolotelo
 * @author Bruno de Souza Ferreira
 * @version 1.1
 * @date 20 Jun 2016
 * @date 27 Sep 2016
 * @brief File containing the methods for the reading of an incremental encoder.
 */


/* Project Includes */
#include "encoder.h"
#include "hal/target_definitions.h"

/* System Includes */
#include "fsl_tpm_hal.h"
#include "fsl_tpm_driver.h"
#include "fsl_gpio_driver.h"
#include "fsl_clock_manager.h"
#include "fsl_port_hal.h"
#include "fsl_gpio_hal.h"
#include "fsl_interrupt_manager.h"


/*
 * For ENCODER_ACQ_PERIOD_MS = 10ms: 368 pulses @ 2100RPM; 33 pulses @ 3.2RPM
 * for ENCODER_ACQ_PERIOD_MS = 28ms: 1004 pulses@ 2100RPM; 91 pulses @ 3.2RPM
 */

///**
// * @brief Channel O IRQ handler
// * 
// */
//extern void ENCODER_CHO_IRQ_HANDLER()
//{
//    PORT_HAL_ClearPinIntFlag(PORTD, 0);
//    uiEncoderPosition = 0;
//}



/********************************************* NEW STUFF ********************************************************/

#define DEBUG_MODE_ENABLE 1U // change tpm_general_config to reflect this. Also make this global (for all tpm's)

/*****************************************************************************************************************/


/**
 * @brief Initializes the encoder for an incremental encoder.
 * 
 * @param encoderInstance encoderInstance_t struct.
 */
void encoder_initEncoder(encoderInstance_t *encoderInstance)
{

	int instance = 0, port=0;
	TPM_Type *tpmBase = g_tpmBase[encoderInstance.uiEncoderTpmInstance];
	PORT_Type *encoderPortBase = g_portBase[encoderInstance.uiEncoderPortInstance];

    /* Configure Channel PORTs */
    CLOCK_SYS_EnablePortClock(encoderInstance.uiEncoderPortInstance);
    PORT_HAL_SetMuxMode(encoderPortBase, encoderInstance.uiEncoderPinNumber, encoderInstance.uiEncoderPortAlt);

    /* Configure external clock source for TPM modules */
    SIM_HAL_SetTpmExternalClkPinSelMode(SIM, encoderInstance.uiEncoderPortInstance, encoderInstance.uiEncoderTpmClkinSrc);

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

    /* Set up and enable Channel O interrupt */
    /*CLOCK_SYS_EnablePortClock(ENCODER_CHO_PORT_INSTANCE);
    PORT_HAL_SetMuxMode(ENCODER_CHO_PORT_BASE, ENCODER_CHO_PIN_NUMBER, kPortMuxAsGpio);
    PORT_HAL_SetPinIntMode(ENCODER_CHO_PORT_BASE, ENCODER_CHO_PIN_NUMBER, kPortIntRisingEdge);
    NVIC_EnableIRQ(ENCODER_CHO_IRQn);*/


}


/**
 * @brief Enables the counter.
 * 
 * @param encoderInstance encoderInstance_t struct.
 */
void encoder_enableCounter(encoderInstance_t *encoderInstance)
{
    TPM_Type *tpmBase = g_tpmBase[encoderInstance.uiEncoderTpmInstance];
    TPM_HAL_SetClockMode(tpmBase, kTpmClockSourceExternalClk);
}


/**
 * @brief Disables the counter
 * 
 * @param encoderInstance encoderInstance_t struct.
 */
void encoder_disableCounter(encoderInstance_t *encoderInstance)
{
    TPM_Type *tpmBase = g_tpmBase[encoderInstance.uiEncoderTpmInstance];
    TPM_HAL_SetClockMode(tpmBase, kTpmClockSourceNoneClk);
    encoder_resetCounter();
}


/**
 * @brief Resets the counter.
 * 
 * @param encoderInstance encoderInstance_t struct.
 */
void encoder_resetCounter(encoderInstance_t *encoderInstance)
{
    TPM_Type *tpmBase = g_tpmBase[encoderInstance.uiEncoderTpmInstance];
    TPM_HAL_ClearCounter(tpmBase);
}


///**
// * @brief Enables the interrupt on Channel O.
// * 
// * @param encoderInstance encoderInstance_t struct.
//*/
//void encoder_enableChOInterrupt(encoderInstance_t *encoderInstance)
//{
//    NVIC_EnableIRQ(ENCODER_CHO_IRQn);
//}
//
//
///**
// * @brief Disables the interrupt on channel O.
// * 
// * @param encoderInstance encoderInstance_t struct.
// */
//void encoder_disableChOInterrupt(encoderInstance_t *encoderInstance)
//{
//    NVIC_DisableIRQ(ENCODER_CHO_IRQn);
//}


/**
 * @brief Takes a measurement of speed, direction and position.
 * 
 * @param encoderInstance encoderInstance_t struct.
 */
void encoder_takeMeasurement(encoderInstance_t *encoderInstance)
{
    TPM_Type *tpmBase = g_tpmBase[encoderInstance.uiEncoderTpmInstance];
    encoderInstance.uiEncoderPulsesPerSecond = (1000*TPM_HAL_GetCounterVal(tpmBase))/ENCODER_ACQ_PERIOD_MS;
    encoder_resetCounter();
}


/* Data retrieval methods */


/**
 * @brief Returns the angular position of the encoder in degrees.
 * 
 * @param encoderInstance encoderInstance_t struct.
 * @return Angular position of the encoder in degrees.
 */
//double encoder_getAngularPositionDegree(encoderInstance_t *encoderInstance)
//{
//    return 360*((double)uiEncoderPosition/encoderInstance.uiEncoderPulseCount);
//}


/**
 * @brief Returns the angular position of the encoder in radians.
 * 
 * @param encoderInstance encoderInstance_t struct.
 * @return Angular position of the encoder in radians.
 */
//double encoder_getAngularPositionRad(encoderInstance_t *encoderInstance)
//{
//    return CONST_2PI*((double)uiEncoderPosition/encoderInstance.uiEncoderPulseCount);
//}


/**
 * @brief Returns the angular velocity of the encoder in pulses per second.
 * 
 * @param encoderInstance encoderInstance_t struct.
 * @return Angular velocity of the encoder in pps.
 */
double encoder_getAngularVelocity(encoderInstance_t *encoderInstance)
{
    return encoderInstance.uiEncoderPulsesPerSecond;
}


/**
 * @brief Returns the angular velocity of the encoder in Rad/s.
 * 
 * @param encoderInstance encoderInstance_t struct.
 * @return Angular velocity of the encoder in Rad/s.
 */
double encoder_getAngularVelocityRad(encoderInstance_t *encoderInstance)
{
    return CONST_2PI*(encoderInstance.uiEncoderPulsesPerSecond/encoderInstance.uiEncoderPulseCount);
}


/**
 * @brief Returns the angular velocity of the encoder in RPM.
 * 
 * @param encoderInstance encoderInstance_t struct.
 * @return Angular velocity of the encoder in RPM.
 */
double encoder_getAngularVelocityRPM(encoderInstance_t *encoderInstance)
{
    return 60*(encoderInstance.uiEncoderPulsesPerSecond/encoderInstance.uiEncoderPulseCount);
}







