/*
 * Descripción -> Uso de la pantalla nextion para la operación de relay, 
 *                motor DC, servomotor y lectura de LM35
 * Placa -> Aruino Nano
 * Shield -> Kaanbal V1.0
 * Display -> NX3224T024
 * WIFI -> ESP8266
*/
#include <Wire.h> 
#include <Servo.h>
#include "chimalli.h"
#include "hmi.h"
#include "request.h"


void setup(){
  Serial.begin(9600);
}

void loop(){
  //Array of bytes [ff, 45, ...]
  byte displayResponse[9];
  while (Serial.available() > 0){   
    for (int i = 1 ; i < 16; i++){
      displayResponse[i] =  Serial.read();
      delay(20);                 
    }
    displayResponse[9] = '\0';
    defineAction(displayResponse);
  }
}
