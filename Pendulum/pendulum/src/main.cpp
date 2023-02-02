#include <Arduino.h>

// char DELIM = '\t';
int sensorPin = PIN_A1;
int resetButton = PIN2;
long baud_rate = 9600;

bool hasRun = false;
bool eq_state = false;

float timeCounter = 0;
float prevTime = 0;
float currTime = 0;
float period = 0;
float halfPeriod = 0;
float hits[11];
float firstHit = 0;
float length = 0;

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

  pinMode(resetButton, INPUT_PULLUP);
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
  if (hasRun == false)
  {
    // clearscreen();
    Serial.println("Calibrating the sensor...");

    eq_state_light = analogRead(sensorPin) - 10;
    eq_state = true;

    while (true)
    {
      if (analogRead(sensorPin) < eq_state_light)
      {
        Serial.println("Ball left the eq state");
        eq_state = false;
        break;
      }

      // clearscreen();
      Serial.println("Color Sensor RAW:" + analogRead(sensorPin));
    }

    timeCounter = 0;
    prevTime = millis() / 1000.0;

    for (int i = 0; i < 10; i++)
    {
      hits[i] = 0.0;
    }

    while (true)
    {
      //-- -- -- -- -- - Time Handling -- -- -- -- -- -- -- -
      currTime = millis() / 1000.0;
      timeCounter += (currTime - prevTime);
      prevTime = currTime;
      //-- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -

      if (analogRead(sensorPin) >= eq_state_light)
      {
        hits[event] = timeCounter;
        Serial.print("Hit RAW:");
        Serial.println(timeCounter);
        delay(500);
        event++;
        if (event > 10)
        {
          break;
        }
      }
    }

    // clearscreen();
    firstHit = hits[0];
    Serial.println("-------- DONE --------");
    Serial.println("Hits shifted by the first hit value...");

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

    Serial.print("Average Period: ");
    Serial.print(period);
    Serial.println("s");

    Serial.print("Length of the pendulum is: ");
    Serial.print(period);
    Serial.println("m");

    Serial.print("Length of the pendulum is: ");
    Serial.print(period * 100.0);
    Serial.println("cm");

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
