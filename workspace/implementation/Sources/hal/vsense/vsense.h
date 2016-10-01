/**
 * @file vsense.h
 * @author Guilherme Kairalla Kolotelo
 * @author Bruno de Souza Ferreira
 * @version 1.0
 * @date 30 Sep 2016
 * @brief File containing the definition of methods for interacting with the sense resistors.
 */

void vsense_initVsense();

uint16_t vsense_getRawV1();

uint16_t vsense_getRawV2();

float vsense_getV1();

float vsense_getV2();

float vsense_getSystemVoltage();

float vsense_getCurrent();

float vsense_getPower();
