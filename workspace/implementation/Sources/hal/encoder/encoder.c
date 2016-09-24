/**
 *
 * File name:           encoder.c                            
 * File description:    File containing the methods for the reading
 *                      of an incremental, 3-pin, encoder.
 *                      
 *
 * Authors:             Bruno de Souza Ferreira
 *                      Guilherme Kairalla Kolotelo
 *                      Guilherme Bersi Pereira
 *
 * Creation date:       10Jun2016                                       
 * Revision date:       27Jun2016
 *
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
 * Method name:         ENCODER_CHO_IRQ_HANDLER
 * Method description:  Channel O IRQ handler
 * Input params:        n/a
 * Output params:       n/a
 */
extern void ENCODER_CHO_IRQ_HANDLER()
{
    PORT_HAL_ClearPinIntFlag(PORTD, 0);
    uiEncoderPosition = 0;
}



/********************************************* NEW STUFF ********************************************************/


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


#define DEBUG_MODE_ENABLE 1U // change tpm_general_config to reflect this. Also make this global (for all tpm's)

/*****************************************************************************************************************/
//ADD CHB BACK


/**
 * Method name:         encoder_initEncoder
 * Method description:  Initializes the encoder for an incremental 3-pin encoder
 * Input params:        n/a
 * Output params:       n/a
 */
void encoder_initEncoder(encoder_instance_t encoder_instance)
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
 * Method name:         encoder_enableCounter
 * Method description:  Enables the counter
 * Input params:        n/a
 * Output params:       n/a
 */
void encoder_enableCounter(encoder_instance_t encoder_instance)
{
    TPM_HAL_SetClockMode(ENCODER_CHA_TPM_BASE, kTpmClockSourceExternalClk);
}

/**
 * Method name:         encoder_disableCounter
 * Method description:  Disables the counter
 * Input params:        n/a
 * Output params:       n/a
 */
void encoder_disableCounter(encoder_instance_t encoder_instance)
{
    TPM_HAL_SetClockMode(ENCODER_CHA_TPM_BASE, kTpmClockSourceNoneClk);
    encoder_resetCounter();
}

/**
 * Method name:         encoder_resetCounter
 * Method description:  Resets the counter
 * Input params:        n/a
 * Output params:       n/a
 */
void encoder_resetCounter(encoder_instance_t encoder_instance)
{
    TPM_HAL_ClearCounter(ENCODER_CHA_TPM_BASE);
}

/**
 * Method name:         encoder_enableChOInterrupt
 * Method description:  Enables the interrupt on Channel O
 * Input params:        n/a
 * Output params:       n/a
 */
void encoder_enableChOInterrupt(encoder_instance_t encoder_instance)
{
    NVIC_EnableIRQ(ENCODER_CHO_IRQn);
}

/**
 * Method name:         encoder_disableChOInterrupt
 * Method description:  Disables the interrupt on channel O
 * Input params:        n/a
 * Output params:       n/a
 */
void encoder_disableChOInterrupt(encoder_instance_t encoder_instance)
{
    NVIC_DisableIRQ(ENCODER_CHO_IRQn);
}

/**
 * Method name:         encoder_takeMeasurement
 * Method description:  Takes a measurement of speed, direction and position
 * Input params:        n/a
 * Output params:       n/a
 */
void encoder_takeMeasurement(encoder_instance_t encoder_instance)
{
    uiEncoderPulsesPerSecond = (1000*TPM_HAL_GetCounterVal(ENCODER_CHA_TPM_BASE))/ENCODER_ACQ_PERIOD_MS;
    iEncoderDirection = TPM_HAL_GetCounterVal(ENCODER_CHA_TPM_BASE) > TPM_HAL_GetCounterVal(ENCODER_CHB_TPM_BASE) ? 1 : -1;
    uiEncoderPosition += TPM_HAL_GetCounterVal(ENCODER_CHA_TPM_BASE);
    encoder_resetCounter();
}


/* Data retrieval methods */

/**
 * Method name:         encoder_getAngularPositionDegree
 * Method description:  Returns the angular position of the encoder in degrees
 * Input params:        n/a
 * Output params:       double = Angular position of the encoder in degrees
 */
double encoder_getAngularPositionDegree(encoder_instance_t encoder_instance)
{
    return 360*((double)uiEncoderPosition/ENCODER_PULSE_COUNT);
}

/**
 * Method name:         encoder_getAngularPositionRad
 * Method description:  Returns the angular position of the encoder in radians
 * Input params:        n/a
 * Output params:       double = Angular position of the encoder in radians
 */
double encoder_getAngularPositionRad(encoder_instance_t encoder_instance)
{
    return CONST_2PI*((double)uiEncoderPosition/ENCODER_PULSE_COUNT);
}

/**
 * Method name:         encoder_getAngularVelocity
 * Method description:  Returns the angular velocity of the encoder in pulses per second
 * Input params:        n/a
 * Output params:       double = Angular velocity of the encoder in pps
 */
double encoder_getAngularVelocity(encoder_instance_t encoder_instance)
{
    return (double)uiEncoderPulsesPerSecond;
}

/**
 * Method name:         encoder_getAngularVelocityRadPerSec
 * Method description:  Returns the angular velocity of the encoder in Rad/s
 * Input params:        n/a
 * Output params:       double = Angular velocity of the encoder in Rad/s
 */
double encoder_getAngularVelocityRad(encoder_instance_t encoder_instance)
{
    return CONST_2PI*((double)uiEncoderPulsesPerSecond/ENCODER_PULSE_COUNT);
}

/**
 * Method name:         encoder_getAngularVelocityRPM
 * Method description:  Returns the angular velocity of the encoder in RPM
 * Input params:        n/a
 * Output params:       double = Angular velocity of the encoder in RPM
 */
double encoder_getAngularVelocityRPM(encoder_instance_t encoder_instance)
{
    return 60*((double)uiEncoderPulsesPerSecond/ENCODER_PULSE_COUNT);
}







