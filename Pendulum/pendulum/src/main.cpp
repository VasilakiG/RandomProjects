#include <Arduino.h>

int LaserDetectorPin = 2;
char DELIM = '\t';

long baud_rate = 2000000;

bool photoGate;
bool lastState = 0;

int eventNum = 1;
long eventTime;

void setup(){
  Serial.begin(baud_rate);

  pinMode(LaserDetectorPin, INPUT_PULLUP);
  pinMode(13, OUTPUT);

  Serial.print("event");
  Serial.print(DELIM);

  Serial.print("time");
  Serial.print(DELIM);

  Serial.println("state");
  Serial.println("======================");
}

void loop(){
  photoGate = digitalRead(LaserDetectorPin);
  digitalWrite(13, !photoGate);
  
  if (photoGate != lastState)
    {
      eventTime = millis();
      Serial.print(eventNum);
      Serial.print(DELIM);
      Serial.print(eventTime / 1000.0, 3);
      Serial.print(DELIM);
      Serial.println(photoGate);
      eventNum++;
    }
  lastState = photoGate;

}
