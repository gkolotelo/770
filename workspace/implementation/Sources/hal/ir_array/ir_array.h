/**
 * @file ir_array.h
 * @author Guilherme Kairalla Kolotelo
 * @author Bruno de Souza Ferreira
 * @version 1.1
 * @date 27 Jun 2016
 * @date 27 Sep 2016
 * @brief File containing the definition of methods for interacting with an IR array .
 */


void ir_array_initArray();

void ir_array_ledSingleOn(uint8_t uiLedInstance);

void ir_array_ledArrayOn();

void ir_array_ledSingleOff(uint8_t uiLedInstance);

void ir_array_ledArrayOff();

uint16_t ir_array_takeSingleMeasurement(uint8_t uiIrChannelInstance);

void ir_array_takeMeasurement(uint16_t* uiIrVector);
