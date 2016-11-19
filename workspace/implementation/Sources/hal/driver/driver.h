/**
 * @file driver.h
 * @author Guilherme Kairalla Kolotelo
 * @author Bruno de Souza Ferreira
 * @version 1.1
 * @date 10 Jun 2016
 * @date 27 Sep 2016
 * @brief File containing the definition of methods for the operation of an H-Bridge in bipolar operation mode.
 * @detail File containing the definition of methods for the operation
 *         of an H-Bridge in bipolar operation mode.
 *         
 *         - Driver actuation through driver_setDriver goes from -100 to 100, the
 *           former being full reverse, and the latter, full steam ahead.
 *         - Driver max freq @ 100kHz.
 *         - Channel A on HighTrue and Channel B on LowTrue makes
 *           for a bipolar H-Bridge pair of control signals.
 */

#include <MKL25Z4.h>
#include "fsl_sim_hal.h"
#include "fsl_tpm_hal.h"

#ifndef SOURCES_DRIVER_H_
#define SOURCES_DRIVER_H_

/**
 * @brief driver_instance_t Struct containing specific data for a motor driver instance.
 */
typedef struct {
	/* Config section */
	char cDriverInstance;
	uint8_t uiDriverPwmChAPortInstance;
	uint8_t uiDriverPwmChAPinNumber;
	uint8_t uiDriverPwmChAPortAlt;
    uint8_t uiDriverPwmChAChannelInstance;
    uint8_t uiDriverPwmChBPortInstance;
    uint8_t uiDriverPwmChBPinNumber;
    uint8_t uiDriverPwmChBPortAlt;
    uint8_t uiDriverPwmChBChannelInstance;
    uint8_t uiDriverTpmInstance;
    uint8_t uiDriverTpmClkinInstance;
	clock_tpm_src_t tTpmClkSrc; // kClockTpmSrcNone
	tpm_clock_ps_t tTpmClkPrescaler; // kTpmDividedBy1

	uint8_t uiDriverEnPinNumber;
	uint8_t uiDriverEnPortAlt;
	uint8_t uiDriverEnPortInstance;
    uint8_t uiDriverEnGpioInstance;

} driver_instance_t;

/**
 * @brief Initializes the driver with the load in idle (50% duty cycle).
 * 
 * @param driverInstance driver_instance_t struct.
 */
void driver_initDriver(driver_instance_t driverInstance);

/**
 * @brief Add another driver instance to an already active driver session with the load in idle (50% duty cycle).
 *
 * @param driverInstance driver_instance_t struct.
 */
void driver_appendDriver(driver_instance_t driverInstance);

/**
 * @brief Disables the driver by clearing the enable pin.
 * 
 * @param driverInstance driver_instance_t struct.
 */
void driver_disableDriver(driver_instance_t driverInstance);

/**
 * @brief Enables the driver by setting the enable pin
 * 
 * @param driverInstance driver_instance_t struct.
 */
void driver_enableDriver(driver_instance_t driverInstance);

/**
 * @brief Sets duty cycle for Channel A only.
 * 
 * @param driverInstance driver_instance_t struct.
 * @param uiDutyCyclePercent Duty cycle in percentage.
 */
void driver_setChannelADutyCycle(driver_instance_t driverInstance, int uiDutyCyclePercent);

/**
 * @brief Sets duty cycle for Channel B only.
 * 
 * @param driverInstance driver_instance_t struct.
 * @param uiDutyCyclePercent Duty cycle in percentage.
 */
void driver_setChannelBDutyCycle(driver_instance_t driverInstance, int uiDutyCyclePercent);

/**
 * @brief Sets duty cycle for H-Bridge operation. Both ChA and ChB.
 * 
 * @param driverInstance driver_instance_t struct.
 * @param uiDutyCyclePercent Duty cycle in percentage (0% is full reverse, 100% is full ahead).
 */
void driver_setHBridgeDutyCycle(driver_instance_t driverInstance, int uiDutyCyclePercent);

/**
 * @brief Sets the driver from -100 to 100, the former being full reverse, and the latter, full steam ahead.
 * 
 * @param driverInstance driver_instance_t struct.
 * @param input -100 to 100.
 */
void driver_setDriver(driver_instance_t driverInstance, int input);


/**
 * @brief setDriver but takes another argument to multiply duty cycle
 *
 * @param driverInstance driver_instance_t struct.
 * @param input -100 to 100.
 * @param factor to multiply input.
 */
void driver_setDriver2(driver_instance_t driverInstance, int input, float factor);

#endif /* SOURCES_DRIVER_H_ */
