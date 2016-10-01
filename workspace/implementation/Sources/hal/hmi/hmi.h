/**
 * @file hmi.h
 * @author Guilherme Kairalla Kolotelo
 * @author Bruno de Souza Ferreira
 * @version 1.1
 * @date 20 Jun 2016
 * @date 27 Sep 2016
 * @brief File containing the definition of methods for the interaction with a host device via a serial connection.
 */

#ifndef SOURCES_HMI_H_
#define SOURCES_HMI_H_






/* IR Text */
#define HMI_DIAG_UITEXT_IR_RUNNING		(char *)"IR Array: 		Running Diagnostics..."
#define HMI_DIAG_UITEXT_IR_ERR			(char *)"IR Array: 		Errors Found. Check Log!"
#define HMI_DIAG_UITEXT_IR_OK			(char *)"IR Array: 		A-OK!"
#define HMI_DIAG_UITEXT_IRX				(char *)"		IR Led #"
#define HMI_DIAG_UITEXT_IRX_OK			(char *)" OK!"
#define HMI_DIAG_UITEXT_IRX_ERR			(char *)" ERROR!"
#define HMI_DIAG_UITEXT_IRAX			(char *)"		IR Sensor #"
#define HMI_DIAG_UITEXT_IRAX_OK			(char *)" OK! Reading: "
#define HMI_DIAG_UITEXT_IRAX_ERR		(char *)" ERROR!"

/* Encoder Text */
#define HMI_DIAG_UITEXT_ENC_RUNNING		(char *)"Encoders: 		Running Diagnostics..."
#define HMI_DIAG_UITEXT_ENC_ERR			(char *)"Encoders: 		Errors Found. Check Log!"
#define HMI_DIAG_UITEXT_ENC_OK			(char *)"Encoders: 		A-OK!"
#define HMI_DIAG_UITEXT_ENCX			(char *)"		Encoder #"
#define HMI_DIAG_UITEXT_ENCX_OK			(char *)" OK! Reading: "
#define HMI_DIAG_UITEXT_ENCX_ERR		(char *)" ERROR!"

/* Motor Text */
#define HMI_DIAG_UITEXT_MOT_RUNNING		(char *)"Motors: 		Running Diagnostics..."
#define HMI_DIAG_UITEXT_MOT_ERR			(char *)"Motors: 		Errors Found. Check Log!"
#define HMI_DIAG_UITEXT_MOT_OK			(char *)"Motors: 		A-OK!"
#define HMI_DIAG_UITEXT_MOTX			(char *)"		Motor #"
#define HMI_DIAG_UITEXT_MOTX_OK			(char *)" OK! Current [mA]: "
#define HMI_DIAG_UITEXT_MOTX_ERR		(char *)" ERROR!"
#define HMI_DIAG_UITEXT_MOT_INNACURATE	(char *)"Skipping Motor Diagnostics: Voltage Sense Test Failed!"

/* Vsense Text */
#define HMI_DIAG_UITEXT_VSENSE_RUNNING	(char *)"Voltage Sense: 	Running Diagnostics..."
#define HMI_DIAG_UITEXT_VSENSE_ERR		(char *)"Voltage Sense: 	Errors Found. Check Log!"
#define HMI_DIAG_UITEXT_VSENSE_OK		(char *)"Voltage Sense: 	A-OK!"
#define HMI_DIAG_UITEXT_VSENSEX			(char *)"		VSense #"
#define HMI_DIAG_UITEXT_VSENSEX_OK		(char *)" OK! Voltage [V]: "
#define HMI_DIAG_UITEXT_VSENSEX_ERR		(char *)" ERROR!"
#define HMI_DIAG_UITEXT_VSENSE_CURR		(char *)" Current [mA]: "
#define HMI_DIAG_UITEXT_VSENSE_PWR		(char *)" Power [mW]: "

/* General Text */
#define HMI_DIAG_UITEXT_INIT			(char *)"Self-Diagnostics Routine Initiated. Please Wait..."
#define HMI_DIAG_UITEXT_COMPLETE_OK		(char *)"Self-Diagnostics Routine Complete! No Errors Found."
#define HMI_DIAG_UITEXT_COMPLETE_ERR	(char *)"Self-Diagnostics Routine Complete! Errors Found. Check Log For Errors! System Halted..."
#define HMI_DIAG_UITEXT_SUMMARY			(char *)"------------------ Summary: ------------------"


void hmi_initHmi();

void hmi_transmitNewLine();

void hmi_transmitS(char* string);

void hmi_transmitSCS(char* string1, char id, char* string2);

void hmi_transmitSIS(char* string1, int id, char* string2);

void hmi_transmitSCSF(char* string1, char id, char* string2, float reading);

void hmi_transmitSISI(char* string1, int id, char* string2, int reading);

#endif /* SOURCES_HMI_H_ */
