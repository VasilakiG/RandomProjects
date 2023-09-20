#include <Arduino.h>

// Pin definitions
int sensorPin = PIN_A1;
int resetButton = PIN2;
long baud_rate = 9600;
// char DELIM = '\t';

// Boolean flag to control the calibration process
bool hasRun = false;
bool eq_state = false;

// Variables for storing time, period and pendulum length
float timeCounter = 0;
float prevTime = 0;
float currTime = 0;
float period = 0;
float halfPeriod = 0;
float hits[11];
float firstHit = 0;
float length = 0;

// Variables for storing event number and light threshold
int event = 0;
int eq_state_light = 0;

// void clearscreen()
// {
//   for (int i = 0; i < 10; i++)
//   {
//     Serial.println("\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
//   }
// }

void setup()
{

  Serial.begin(baud_rate);

  pinMode(resetButton, INPUT);
  pinMode(sensorPin, INPUT); //_PULLUP
  pinMode(13, OUTPUT);

  // Serial.print("event");
  // Serial.print(DELIM);

  // Serial.print("time");
  // Serial.print(DELIM);

  // Serial.println("state");
  // Serial.println("======================");
}

void loop()
{
  // Wait for reset button to be pressed
  if (!hasRun)
  {
    // clearscreen();

    // Calibrate the sensor
    Serial.println("======================");
    Serial.println("Calibrating the sensor...");
    Serial.println("======================");

    eq_state_light = analogRead(sensorPin) - 10;
    eq_state = true;

    while (eq_state)
    {
      if (analogRead(sensorPin) < eq_state_light)
      {
        Serial.println("======================");
        Serial.println("Ball left the equilibrium state");
        Serial.println("======================");
        eq_state = false;
        break;
      }

      // clearscreen();
      Serial.println("Sensor value:" + analogRead(sensorPin));
    }

    // Record the time of 10 pendulum swings
    timeCounter = 0;
    prevTime = millis() / 1000.0;

    for (int i = 0; i < 10; i++)
    {
      hits[i] = 0.0;
    }

    while (event < 10)
    {
      //-- -- -- -- -- - Time Handling -- -- -- -- -- -- -- -
      currTime = millis() / 1000.0;
      timeCounter += (currTime - prevTime);
      prevTime = currTime;
      //-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -

      // Check if the pendulum has swung
      if (analogRead(sensorPin) >= eq_state_light)
      {
        hits[event] = timeCounter;
        Serial.print("Time hit:");
        Serial.println(timeCounter);
        delay(500);
        event++;
      }
    }

    // clearscreen();

    // Calculate the period and length of the pendulum
    firstHit = hits[0];
    Serial.println("======== DONE ========");
    Serial.println("Results:");

    for (int i = 0; i < 10; i++)
    {
      Serial.print("Hit ");
      Serial.print(i);
      Serial.print(": ");
      Serial.println(hits[i] - firstHit);
    }

    halfPeriod = (hits[1] - hits[0]);

    for (int i = 0; i < 9; i++)
    {
      halfPeriod = (halfPeriod + (hits[i + 1] - hits[i])) / 2.0;
    }

    period = halfPeriod * 2.0;
    length = period * period * 9.81 / (4.0 * PI * PI);

    Serial.println("======================");
    Serial.print("Average Period: ");
    Serial.print(period);
    Serial.println("s");

    Serial.print("Length of the pendulum is: ");
    Serial.print(period);
    Serial.println("m");

    Serial.print("Length of the pendulum is: ");
    Serial.print(period * 100.0);
    Serial.println("cm");
    Serial.println("======================");

    hasRun = true;
    delay(1000);
  }

  if (digitalRead(resetButton) == HIGH)
  {
    hasRun = false;
    event = 0;
    delay(1000);
  }
}
