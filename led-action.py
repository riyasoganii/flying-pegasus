#include <Servo.h>

Servo myServo;
Servo myServo1;
int potpin = 0;
int val;
int val1;
const int ledPin=4;

void setup() {
  pinMode(2, INPUT);
  pinMode(8, INPUT);
  myServo.attach(12);
  myServo1.attach(13);
 
  pinMode(4, OUTPUT);//for leds
  pinMode(7, OUTPUT);//for leds
  Serial.begin(9600);

}

void loop() {
  Serial.println(digitalRead(2));
  val = analogRead(potpin);
  val1 = analogRead(potpin);
 
  val = map(val,0,700  , 0, 360);
  val1 = map(val1,0,700, 360, 0);
  myServo.write(val);
  myServo1.write(val1);
  if (digitalRead(2) == HIGH) {
    // turn LED on:
    digitalWrite(4, HIGH);
  }
  else {
    // turn LED off:
    digitalWrite(4, LOW);
  }
  if (digitalRead(8) == HIGH) {
    // turn LED on:

    digitalWrite(7, HIGH);
  } else {
    // turn LED off:
 
    digitalWrite(7, LOW);
  }
 

  delay(100);

}
