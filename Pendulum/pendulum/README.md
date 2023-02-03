## Introduction
This code is written for Arduino boards, it uses the `Arduino.h` library to control the board and read from the sensor and button. The purpose of the code is to measure the length of a pendulum using a light detection resistor(LDR) sensor and calculate the average period of its oscillations.

## Variables
`sensorPin`: This integer variable represents the analog pin of the color sensor that is connected to the Arduino board.

`resetButton`: This integer variable represents the digital pin of the button that is connected to the Arduino board.

`baud_rate`: This long variable represents the baud rate of the serial communication that is used to display the results on the serial monitor.

`hasRun`: This boolean variable determines if the code has already been run.

`eq_state`: This boolean variable determines the state of the pendulum (if it's in an equilibrium state or not).

`timeCounter`: This float variable represents the elapsed time between the first and last oscillation.

`prevTime`: This float variable stores the previous value of the elapsed time.

`currTime`: This float variable stores the current value of the elapsed time.

`period`: This float variable represents the average period of the pendulum's oscillations.

`halfPeriod`: This float variable represents half the value of the average period.

`hits`: This float array stores the time of each oscillation.

`firstHit`: This float variable stores the time of the first oscillation.

`length`: This float variable represents the calculated length of the pendulum.

`event`: This integer variable counts the number of oscillations that have occurred.

`eq_state_light`: This integer variable stores the initial light value that is used to determine the pendulum's state.

### Setup
The `setup()` function initializes the board and sets the necessary pins and variables to their initial values.

The serial communication is started with a baud rate of 9600.

The `resetButton` and `sensorPin` pins are set to inputs.

The LED on pin 13 is set to an output.

### Loop
The `loop()` function is the main part of the code that reads from the sensor and calculates the length of the pendulum.

If the code has not been run before, the function starts by calibrating the sensor and measuring the time between each oscillation.

The first oscillation is used to determine the state of the pendulum. If it's in an equilibrium state, the code waits until it leaves this state.

The elapsed time between each oscillation is calculated and stored in the `hits` array.

Once 10 oscillations have been recorded, the first hit is subtracted from each value in the hits array.

The average period of the pendulum's oscillations is calculated by taking the average of half the elapsed time between each oscillation.

The length of the pendulum is calculated using the formula `length = period^2 * 9.81 / (4 * PI^2)`.

The calculated length of the pendulum is displayed on the serial monitor in meters and centimeters.

If the `resetButton` is pressed, the code is set to run again.

## Conclusion
This method for determining length of a pendulum is only useful in cases of small angles of swinging. For big angles and long lenths of the pendulum it is not effective.
