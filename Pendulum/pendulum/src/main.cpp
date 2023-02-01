#include <Arduino.h>

// char DELIM = '\t';
int laserDetectorPin = 2;
long baud_rate = 2000000;

bool eq_state = false;
int eq_state_light = 0;

float timeCounter = 0;
float prevTime = 0;
float currTime = 0;
float period = 0;
float halfPeriod = 0;

float hits[11];
float firstHit = 0;
int event = 0;

float length = 0;

void clearscreen()
{
  for (int i = 0; i < 10; i++)
  {
    Serial.println("\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
  }
}

void setup()
{
  Serial.begin(baud_rate);

  pinMode(laserDetectorPin, INPUT); //_PULLUP
  pinMode(13, OUTPUT);

  Serial.print("event");
  Serial.print(DELIM);

  Serial.print("time");
  Serial.print(DELIM);

  Serial.println("state");
  Serial.println("======================");
}

void loop()
{
  clearscreen();
  Serial.println("Calibrating the sensor...");

  eq_state_light = digitalRead(laserDetectorPin) - 2;
  eq_state = true;

  while (true)
  {
    if (digitalRead(laserDetectorPin) < eq_state_light)
    {
      Serial.println("Ball left the eq state");
      eq_state = false;
      break;
    }

    clearscreen();
    Serial.println("Color Sensor RAW:" + digitalRead(laserDetectorPin));
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

    if (digitalRead(laserDetectorPin) >= eq_state_light)
    {
      event = 0;
      hits[event] = timeCounter;
      Serial.print("Hit RAW:");
      Serial.println(timeCounter);
      delay(500);
      if (event > 10)
      {
        break;
      }
    }
  }

  clearscreen();
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

  Serial.println("Restarting...");
  delay(1000);
}
