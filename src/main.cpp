#include <Arduino.h>

int switch_pin = 3;    
int v5pin = 2; 

void sendRotation(bool act) {
        if(act) {
            Serial.println("command: landscape");
        } else {
            Serial.println("command: portrait");
        }
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
        delay(2000);
}

