#include <Arduino.h>

int switch_pin = 3;    
int v5pin = 2;

int sensor_pin = A7;
int measurement = 0;

void sendRotation(bool act) {
        if(act) {
            Serial.println("command: landscape");
        } else {
            Serial.println("command: portrait");
        }
}

String parseMeasurement(int m) {
  if(m > 800) {
    return "100";
  } else if (m > 700) {
    return "85";
  }
  else if (m > 600) {
    return "70";
  }
  else if (m > 600) {
    return "55";
  }
  else if (m > 500) {
    return "40";
  }
  else if (m > 400) {
    return "25";
  }
  else if (m > 250) {
    return "10";
  }
  return "0";
}

void sendBrightness() {
    int pin_read = 1024 - analogRead(sensor_pin);
    if(abs(measurement - pin_read) > 80) {
        measurement = pin_read;
    }
    Serial.println("brightness: " + parseMeasurement(measurement));
}

void setup()
{
    Serial.begin(9600);
    pinMode(switch_pin, INPUT);
    pinMode(v5pin, OUTPUT);
    digitalWrite(v5pin, HIGH);
    sendRotation(digitalRead(switch_pin));
}

void loop()
{
        sendRotation(digitalRead(switch_pin));

        delay(600);

        sendBrightness();

        delay(600);
}

