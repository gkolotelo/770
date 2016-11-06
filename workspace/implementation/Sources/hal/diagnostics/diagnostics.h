/**
 * @file diagnostics.h
 * @author Guilherme Kairalla Kolotelo
 * @author Bruno de Souza Ferreira
 * @version 1.2
 * @date 27 Jun 2016
 * @date 07 Oct 2016
 * @brief File containing the definition of methods for executing a self-diagnostics routine.
 */

/**
 * @brief Initiates diagnostics sequence.
 * @details Executes each system component test independently and reports the system status.
 * IF ALL TESTS ARE NOT PASSED, THE SYSTEM IS HALTED!
 *
 * @return True if tests were NOT successful.
 */
bool diagnostics_startDiagnostics();

/**
 * @brief Tests operation of the voltage sense.
 * @details Tests Vsense1 and Vsense2 pins, if main system voltage
 * (Vsense1) is smaller than VSENSE_MIN_VOLTAGE, the test is not passed.
 * If Vsense2 > Vsense1, an unexpected behavior, the test is not passed.
 * 
 * @return True if test was NOT successful.
 */
bool diagnostics_btestVSense();

/**
 * @brief Tests operation of the IR Array.
 * @details For each LED/Sensor pair on the IR array, a measurement is taken
 * with the LED off, and a measurement is taken with the LED on, if the latter
 * measurement is not greater than the former, the test is not successful.
 * 
 * @return True if test was NOT successful.
 */
bool diagnostics_btestIrArray();

/**
 * @brief Tests operation of the motors.
 * @details For each motor, the system current is measured with the motor on
 * and with the motor off. If the former measurement is not greater than 
 * MOTOR_MIN_CURR above the quiescent system current, the test is not successful.
 * 
 * @return True if test was NOT successful.
 */
bool diagnostics_btestMotors();

/**
 * @brief Tests operation of the encoders.
 * @details For each encoder, the encoder count is reset and the motor is
 * turned on. If the encoder measurement is not greater than MOTOR_MIN_VEL
 * the test is not successful.
 * 
 * @return True if test was NOT successful.
 */
bool diagnostics_btestEncoders();
