/**
 * @file diagnostics.c
 * @author Guilherme Kairalla Kolotelo
 * @author Bruno de Souza Ferreira
 * @version 1.2
 * @date 27 Jun 2016
 * @date 07 Oct 2016
 * @brief File containing the methods for executing a self-diagnostics routine.
 */

/* System includes */
#include <stdbool.h>
#include <MKL25Z4.h>

/* Project includes */
#include "diagnostics.h"
#include "hal/target_definitions.h"
#include "hal/util/util.h"
#include "hal/encoder/encoder.h"
#include "hal/driver/driver.h"
#include "hal/ir_array/ir_array.h"
#include "hal/vsense/vsense.h"
#include "hal/hmi/hmi.h"


/** Uses instances defined on main.c file */
extern encoder_instance_t tencoderL;
extern encoder_instance_t tencoderR;
extern driver_instance_t tdriverL;
extern driver_instance_t tdriverR;

/**
 * @brief Initiates diagnostics sequence.
 * @details Executes each subsystem test independently and reports the system status.
 *
 * @return True if tests were NOT successful.
 */
bool diagnostics_startDiagnostics()
{
	bool bVS_flag, bIR_flag, bMOT_flag, bENC_flag;

	hmi_initHmi();
	hmi_transmitS(HMI_DIAG_UITEXT_INIT);
	hmi_transmitNewLine();

	/* Test subsystems */
	bVS_flag = diagnostics_btestVSense();
	bIR_flag = diagnostics_btestIrArray();
	/* Wait for user to remove vehicle from the ground before running motors. */
	for(int i = 0; i < 50; i++) util_genDelay100ms();
	bMOT_flag = diagnostics_btestMotors();
	bENC_flag = diagnostics_btestEncoders();

	/* Transmit summary */
	hmi_transmitS(HMI_DIAG_UITEXT_SUMMARY);
	if(bVS_flag) hmi_transmitS(HMI_DIAG_UITEXT_VSENSE_ERR);
	else hmi_transmitS(HMI_DIAG_UITEXT_VSENSE_OK);
	if(bIR_flag) hmi_transmitS(HMI_DIAG_UITEXT_IR_ERR);
	else hmi_transmitS(HMI_DIAG_UITEXT_IR_OK);
	if(bMOT_flag) hmi_transmitS(HMI_DIAG_UITEXT_MOT_ERR);
	else hmi_transmitS(HMI_DIAG_UITEXT_MOT_OK);
	if(bENC_flag) hmi_transmitS(HMI_DIAG_UITEXT_ENC_ERR);
	else hmi_transmitS(HMI_DIAG_UITEXT_ENC_OK);
	hmi_transmitNewLine();
	if(bVS_flag || bIR_flag || bMOT_flag || bENC_flag)
	{
		hmi_transmitS(HMI_DIAG_UITEXT_COMPLETE_ERR);
		return true;
	}
	hmi_transmitS(HMI_DIAG_UITEXT_COMPLETE_OK);
	/* Driver instance tdriverR uses shared pin with UART0, this sets up the mux for proper motor behavior. */
	driver_initDriver(tdriverL);
	driver_appendDriver(tdriverR);
	return false;
}

/**
 * @brief Tests operation of the voltage sense.
 * @details Tests Vsense1 and Vsense2 pins, if main system voltage
 * (Vsense1) is smaller than VSENSE_MIN_VOLTAGE, the test is not passed.
 * If Vsense2 > Vsense1, an unexpected behavior, the test is not passed.
 * Quiescent current and power are also computed and displayed to the user
 * through the use of the two voltage sensors and a sense resistor.
 * 
 * @return True if test was NOT successful.
 */
bool diagnostics_btestVSense()
{
	hmi_transmitS(HMI_DIAG_UITEXT_VSENSE_RUNNING);
	bool berror_flag = false;
	float fmeas1, fmeas2, fmeas3, fmeas4;
	/* Measure average voltages before and after resistor */
	for(int i = 0; i < 20; i++)
	{
		fmeas1 += vsense_getV1();
		util_genDelay1ms();
	}
	fmeas1 = fmeas1/20;
	for(int i = 0; i < 20; i++)
	{
		fmeas2 += vsense_getV2();
		util_genDelay1ms();
	}
	fmeas2 = fmeas2/20;
	/* Get system current and power */
	fmeas3 = vsense_getCurrent();
	fmeas4 = vsense_getPower();
	/* If either voltages are below user define levels set error flag. */
	if(fmeas1 < VSENSE_MIN_VOLTAGE)
	{
		hmi_transmitSCSF(HMI_DIAG_UITEXT_VSENSEX, '1', HMI_DIAG_UITEXT_VSENSEX_ERR, fmeas1);
		berror_flag = true;
	}
	else
	{
		hmi_transmitSCSF(HMI_DIAG_UITEXT_VSENSEX, '1', HMI_DIAG_UITEXT_VSENSEX_OK, fmeas1);
	}
	if(fmeas2 < VSENSE_MIN_VOLTAGE)
	{
		hmi_transmitSCSF(HMI_DIAG_UITEXT_VSENSEX, '2', HMI_DIAG_UITEXT_VSENSEX_ERR, fmeas2);
		berror_flag = true;
	}
	else
	{
		hmi_transmitSCSF(HMI_DIAG_UITEXT_VSENSEX, '2', HMI_DIAG_UITEXT_VSENSEX_OK, fmeas2);
	}
	if(berror_flag)
		hmi_transmitS(HMI_DIAG_UITEXT_VSENSE_ERR);
	else
	{
		hmi_transmitSCSF(HMI_DIAG_UITEXT_VSENSEX, 'c', HMI_DIAG_UITEXT_VSENSE_CURR, fmeas3);
		hmi_transmitSCSF(HMI_DIAG_UITEXT_VSENSEX, 'c', HMI_DIAG_UITEXT_VSENSE_PWR, fmeas4);
		hmi_transmitS(HMI_DIAG_UITEXT_VSENSE_OK);
	}
	hmi_transmitNewLine();
	return berror_flag;
}

/**
 * @brief Tests operation of the IR Array.
 * @details For each LED/Sensor pair on the IR array, a measurement is taken
 * with the LED off, and a measurement is taken with the LED on, if the latter
 * measurement is not greater than the former, the test is not successful.
 * 
 * @return True if test was NOT successful.
 */
bool diagnostics_btestIrArray()
{
	bool berror_flag = false;
	uint32_t fmeas1 = 0, fmeas2 = 0;

	hmi_transmitS(HMI_DIAG_UITEXT_IR_RUNNING);
	ir_array_ledArrayOff();
	for(int i = 0; i < 6; i++)
	{
		fmeas1 = 0, fmeas2 = 0;
		ir_array_ledSingleOn(i);
		util_genDelay10ms();
		fmeas1 = ir_array_takeSingleMeasurement(i);
		ir_array_ledSingleOff(i);
		util_genDelay10ms();
		fmeas2 = ir_array_takeSingleMeasurement(i);
		if(fmeas1 < fmeas2)
		{
			hmi_transmitSIS(HMI_DIAG_UITEXT_IRX, i, HMI_DIAG_UITEXT_IRX_ERR);
			hmi_transmitSISI(HMI_DIAG_UITEXT_IRAX, i, HMI_DIAG_UITEXT_IRAX_ERR, fmeas1);
			berror_flag = true;
		}
		else
		{
			hmi_transmitSIS(HMI_DIAG_UITEXT_IRX, i, HMI_DIAG_UITEXT_IRX_OK);
			hmi_transmitSISI(HMI_DIAG_UITEXT_IRAX, i, HMI_DIAG_UITEXT_IRAX_OK, fmeas1);
		}
	}
	if(berror_flag)
		hmi_transmitS(HMI_DIAG_UITEXT_IR_ERR);
	else
		hmi_transmitS(HMI_DIAG_UITEXT_IR_OK);
	hmi_transmitNewLine();
	return berror_flag;
}

/**
 * @brief Tests operation of the motors.
 * @details For each motor, the system current is measured with the motor on
 * and with the motor off. If the motor on measurement is not greater than 
 * MOTOR_MIN_CURR above the quiescent system current, the test is not successful.
 * That is not acceptable motor current was drawn for the motor being tested.
 * 
 * @return True if test was NOT successful.
 */
bool diagnostics_btestMotors()
{
	hmi_transmitS(HMI_DIAG_UITEXT_MOT_RUNNING);
	bool berror_flag = false;
	float fsscurr = 0, fmeas1 = 0, fmeas2 = 0;
	fsscurr = vsense_getCurrent();
	if(0 == fsscurr)
	{
		hmi_transmitS(HMI_DIAG_UITEXT_MOT_INNACURATE);
		return true;
	}
	/* Testing Right Wheel encoder */
	/* Driver instance tdriverR uses shared pin with UART0, this sets up the mux for proper motor behavior. */
	driver_initDriver(tdriverL);
	driver_appendDriver(tdriverR);
	util_genDelay100ms();
	driver_setDriver(tdriverR, 90);
	driver_enableDriver(tdriverR);
	for(int i = 0; i < 10; i++) util_genDelay100ms();
	fmeas1 = vsense_getCurrent();
	driver_disableDriver(tdriverR);
	driver_setDriver(tdriverR, 0);
	util_genDelay100ms();
	/* Driver instance tdriverR uses shared pin with UART0, this sets up the mux for proper serial behavior. */
	hmi_initHmi();
	util_genDelay100ms();
	/* If motor current not above necessary set error flag. */
	if(fmeas1 < fsscurr + MOTOR_MIN_CURR)
	{
		hmi_transmitSCSF(HMI_DIAG_UITEXT_MOTX, tdriverR.cDriverInstance , HMI_DIAG_UITEXT_MOTX_ERR, fmeas1-fsscurr);
		berror_flag = true;
	}
	else
	{
		hmi_transmitSCSF(HMI_DIAG_UITEXT_MOTX, tdriverR.cDriverInstance, HMI_DIAG_UITEXT_MOTX_OK, fmeas1-fsscurr);
	}
	/* Testing Left Wheel encoder */
	driver_setDriver(tdriverL, 90);
	driver_enableDriver(tdriverL);
	for(int i = 0; i < 10; i++) util_genDelay100ms();
	fmeas2 = vsense_getCurrent();
	/* If motor current not above necessary set error flag. */
	if(fmeas2 < fsscurr + MOTOR_MIN_CURR)
	{
		hmi_transmitSCSF(HMI_DIAG_UITEXT_MOTX, tdriverL.cDriverInstance, HMI_DIAG_UITEXT_MOTX_ERR, fmeas2-fsscurr);
		berror_flag = true;
	}
	else
	{
		hmi_transmitSCSF(HMI_DIAG_UITEXT_MOTX, tdriverL.cDriverInstance, HMI_DIAG_UITEXT_MOTX_OK, fmeas2-fsscurr);
	}
	driver_disableDriver(tdriverL);
	driver_setDriver(tdriverL, 0);
	for(int i = 0; i < 10; i++) util_genDelay100ms();

	if(berror_flag)
		hmi_transmitS(HMI_DIAG_UITEXT_MOT_ERR);
	else
		hmi_transmitS(HMI_DIAG_UITEXT_MOT_OK);
	hmi_transmitNewLine();
	return berror_flag;
}

/**
 * @brief Tests operation of the encoders.
 * @details For each encoder, the encoder count is reset and the motor is
 * turned on. If the encoder measurement is not greater than MOTOR_MIN_VEL
 * the test is not successful.
 * 
 * @return True if test was NOT successful.
 */
bool diagnostics_btestEncoders()
{
	hmi_transmitS(HMI_DIAG_UITEXT_ENC_RUNNING);
	bool berror_flag = false;
	float fmeas1 = 0, fmeas2 = 0;
	/* Test R */
	encoder_resetCounter(tencoderL);
	encoder_resetCounter(tencoderR);
	/* Driver instance tdriverR uses shared pin with UART0, this sets up the mux for proper motor behavior. */
	driver_initDriver(tdriverL);
	driver_appendDriver(tdriverR);
	driver_setDriver(tdriverR, 90);
	driver_enableDriver(tdriverR);
	driver_setDriver(tdriverL, 90);
	driver_enableDriver(tdriverL);
	/* Wait for motor to reach speed. */
	for(int i = 0; i < 10; i++) util_genDelay100ms();
	/* Get encoder readings. */
	encoder_takeMeasurement(&tencoderL);
	encoder_takeMeasurement(&tencoderR);
	fmeas1 = encoder_getAngularVelocity(tencoderL);
	fmeas2 = encoder_getAngularVelocity(tencoderR);

	driver_setDriver(tdriverR, 0);
	driver_disableDriver(tdriverR);
	driver_setDriver(tdriverL, 0);
	driver_disableDriver(tdriverL);
	/* Driver instance tdriverR uses shared pin with UART0, this sets up the mux for proper serial behavior. */
	hmi_initHmi();
	for(int i = 0; i < 10; i++) util_genDelay100ms();
	/* If encoder  didn't capture enough counts the test was not succesfull. */
	if(fmeas1 < MOTOR_MIN_VEL)
	{
		hmi_transmitSCSF(HMI_DIAG_UITEXT_ENCX, tencoderL.cEncoderInstance , HMI_DIAG_UITEXT_ENCX_ERR, fmeas1);
		berror_flag = true;
	}
	else
	{
		hmi_transmitSCSF(HMI_DIAG_UITEXT_ENCX, tencoderL.cEncoderInstance, HMI_DIAG_UITEXT_ENCX_OK, fmeas1);
	}
	/* If encoder didn't capture enough counts the test was not succesfull. */
	if(fmeas2 < MOTOR_MIN_VEL)
	{
		hmi_transmitSCSF(HMI_DIAG_UITEXT_ENCX, tencoderR.cEncoderInstance , HMI_DIAG_UITEXT_ENCX_ERR, fmeas2);
		berror_flag = true;
	}
	else
	{
		hmi_transmitSCSF(HMI_DIAG_UITEXT_ENCX, tencoderR.cEncoderInstance, HMI_DIAG_UITEXT_ENCX_OK, fmeas2);
	}

	if(berror_flag)
		hmi_transmitS(HMI_DIAG_UITEXT_ENC_ERR);
	else
		hmi_transmitS(HMI_DIAG_UITEXT_ENC_OK);
	hmi_transmitNewLine();
	return berror_flag;
}


