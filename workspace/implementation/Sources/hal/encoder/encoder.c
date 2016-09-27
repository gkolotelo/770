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



/* Global variables: */
/* Measured pulses per second */
uint32_t uiEncoderPulsesPerSecond = 0;
/* Orientation of quadrature, -1 or 1 */
int iEncoderDirection = 0;
/* Angular position, in pulses */
uint32_t uiEncoderPosition = 0;

/*
 * For ENCODER_ACQ_PERIOD_MS = 10ms: 368 pulses @ 2100RPM; 33 pulses @ 3.2RPM
 * for ENCODER_ACQ_PERIOD_MS = 28ms: 1004 pulses@ 2100RPM; 91 pulses @ 3.2RPM
 */

/**
 * @brief Channel O IRQ handler
 * 
 */
extern void ENCODER_CHO_IRQ_HANDLER()
{
    PORT_HAL_ClearPinIntFlag(PORTD, 0);
    uiEncoderPosition = 0;
}



/********************************************* NEW STUFF ********************************************************/

#define DEBUG_MODE_ENABLE 1U // change tpm_general_config to reflect this. Also make this global (for all tpm's)

/*****************************************************************************************************************/
//ADD CHB BACK


/**
 * @brief Initializes the encoder for an incremental encoder.
 * 
 * @param encoder_instance encoder_instance_t struct.
 */
void encoder_initEncoder(encoder_instance_t *encoder_instance)
{

	int instance = 0, port=0;
	TPM_Type *tpmBase = g_tpmBase[encoder_instance.uiEncoderTpmInstance];
	PORT_Type *encoderPortBase = g_portBase[encoder_instance.uiEncoderPortInstance];

    /* Configure Channel PORTs */
    CLOCK_SYS_EnablePortClock(encoder_instance.uiEncoderPortInstance);
    PORT_HAL_SetMuxMode(encoderPortBase, encoder_instance.uiEncoderPinNumber, encoder_instance.uiEncoderPortAlt);

    /* Configure external clock source for TPM modules */
    SIM_HAL_SetTpmExternalClkPinSelMode(SIM, encoder_instance.uiEncoderPortInstance, encoder_instance.uiEncoderTpmClkinSrc);

    /* Might be using USB serial over OpenSDA, must enable Debug Mode */
    tpm_general_config_t config=
    {
            .isDBGMode = DEBUG_MODE_ENABLE
    };
    TPM_DRV_Init(encoder_instance.uiEncoderTpmInstance, &config);

    TPM_HAL_SetClockDiv(tpmBase, kTpmDividedBy1);//REVIEW PS SETTING

    TPM_HAL_SetMod(tpmBase, encoder_instance.uiEncoderMaxPulseCount);

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
 * @param encoder_instance encoder_instance_t struct.
 */
void encoder_enableCounter(encoder_instance_t *encoder_instance)
{
    TPM_HAL_SetClockMode(ENCODER_CHA_TPM_BASE, kTpmClockSourceExternalClk);
}


/**
 * @brief Disables the counter
 * 
 * @param encoder_instance encoder_instance_t struct.
 */
void encoder_disableCounter(encoder_instance_t *encoder_instance)
{
    TPM_HAL_SetClockMode(ENCODER_CHA_TPM_BASE, kTpmClockSourceNoneClk);
    encoder_resetCounter();
}


/**
 * @brief Resets the counter.
 * 
 * @param encoder_instance encoder_instance_t struct.
 */
void encoder_resetCounter(encoder_instance_t *encoder_instance)
{
    TPM_HAL_ClearCounter(ENCODER_CHA_TPM_BASE);
}


/**
 * @brief Enables the interrupt on Channel O.
 * 
 * @param encoder_instance encoder_instance_t struct.
*/
void encoder_enableChOInterrupt(encoder_instance_t *encoder_instance)
{
    NVIC_EnableIRQ(ENCODER_CHO_IRQn);
}


/**
 * @brief Disables the interrupt on channel O.
 * 
 * @param encoder_instance encoder_instance_t struct.
 */
void encoder_disableChOInterrupt(encoder_instance_t *encoder_instance)
{
    NVIC_DisableIRQ(ENCODER_CHO_IRQn);
}


/**
 * @brief Takes a measurement of speed, direction and position.
 * 
 * @param encoder_instance encoder_instance_t struct.
 */
void encoder_takeMeasurement(encoder_instance_t *encoder_instance)
{
    uiEncoderPulsesPerSecond = (1000*TPM_HAL_GetCounterVal(ENCODER_CHA_TPM_BASE))/ENCODER_ACQ_PERIOD_MS;
    iEncoderDirection = TPM_HAL_GetCounterVal(ENCODER_CHA_TPM_BASE) > TPM_HAL_GetCounterVal(ENCODER_CHB_TPM_BASE) ? 1 : -1;
    uiEncoderPosition += TPM_HAL_GetCounterVal(ENCODER_CHA_TPM_BASE);
    encoder_resetCounter();
}


/* Data retrieval methods */


/**
 * @brief Returns the angular position of the encoder in degrees.
 * 
 * @param encoder_instance encoder_instance_t struct.
 * @return Angular position of the encoder in degrees.
 */
double encoder_getAngularPositionDegree(encoder_instance_t *encoder_instance)
{
    return 360*((double)uiEncoderPosition/ENCODER_PULSE_COUNT);
}


/**
 * @brief Returns the angular position of the encoder in radians.
 * 
 * @param encoder_instance encoder_instance_t struct.
 * @return Angular position of the encoder in radians.
 */
double encoder_getAngularPositionRad(encoder_instance_t *encoder_instance)
{
    return CONST_2PI*((double)uiEncoderPosition/ENCODER_PULSE_COUNT);
}


/**
 * @brief Returns the angular velocity of the encoder in pulses per second.
 * 
 * @param encoder_instance encoder_instance_t struct.
 * @return Angular velocity of the encoder in pps.
 */
double encoder_getAngularVelocity(encoder_instance_t *encoder_instance)
{
    return (double)uiEncoderPulsesPerSecond;
}


/**
 * @brief Returns the angular velocity of the encoder in Rad/s.
 * 
 * @param encoder_instance encoder_instance_t struct.
 * @return Angular velocity of the encoder in Rad/s.
 */
double encoder_getAngularVelocityRad(encoder_instance_t *encoder_instance)
{
    return CONST_2PI*((double)uiEncoderPulsesPerSecond/ENCODER_PULSE_COUNT);
}


/**
 * @brief Returns the angular velocity of the encoder in RPM.
 * 
 * @param encoder_instance encoder_instance_t struct.
 * @return Angular velocity of the encoder in RPM.
 */
double encoder_getAngularVelocityRPM(encoder_instance_t *encoder_instance)
{
    return 60*((double)uiEncoderPulsesPerSecond/ENCODER_PULSE_COUNT);
}







