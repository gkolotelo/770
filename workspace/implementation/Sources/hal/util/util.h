/**
 * @file util.h
 * @author dloubach
 * @author Guilherme Kairalla Kolotelo
 * @author Bruno de Souza Ferreira
 * @version 1.1
 * @date 09 Jan 2015
 * @date 27 Sep 2016
 * @brief File containing the methods for software delays.
 */

#ifndef UTIL_H
#define UTIL_H


/**
 * @brief generates ~ 180 micro sec
 */
void util_genDelay180us(void);


/**
 * @brief generates ~ 500 micro sec
 */
void util_genDelay500us(void);


/**
 * @brief generates ~ 1 milli sec
 */
void util_genDelay1ms(void);


/**
 * @brief generates ~ 10 milli sec
 */
void util_genDelay10ms(void);


/**
 * @brief generates ~ 100 milli sec
 */
void util_genDelay100ms(void);


#endif /* UTIL_H */
