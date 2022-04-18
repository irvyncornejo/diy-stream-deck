/*
 * Descripción -> Uso de la pantalla nextion para la operación de relay, 
 *                motor DC, servomotor y lectura de LM35
 * Placa -> Aruino Nano
 * Shield -> Kaanbal V1.0
 * Display -> NX3224T024
*/
#include <Wire.h> 
#include <Servo.h>

//Clases
class Relay{
  public:
    int pin;
  Relay(int number){
    pin=number;
    pinMode(pin, OUTPUT);
  }
  void changeState(bool ref){
    digitalWrite(pin, ref);
  }
};

//Class for sensor lm35
class TemperatureSensor{
  public:
    int pin;
  TemperatureSensor(int number){
    pin=number;
  }
  float getValue(){
    int valuePin = analogRead(pin);
    float tempC = (5.0 * valuePin * 100.0)/1024;
    return tempC;
  }
};

//Class for DC Motor
class Motor{
  public:
    int pinA;
    int pinB;
  Motor(int poloA, int poloB){
    pinA=poloA;
    pinB=poloB;
    pinMode(pinA, OUTPUT);
    pinMode(pinB, OUTPUT);
  }
  void toTurn(bool valueA, bool valueB){
    if(valueA != valueB){
      digitalWrite(pinA, valueA);
      digitalWrite(pinB, valueB);
    }
  }
  void toStop(){
    digitalWrite(pinA, LOW);
    digitalWrite(pinB, LOW);
  }
};

//Global Variables
bool flagRelay1 = false;
bool flagMotorA = false;
String valueSensor;
Servo servoMotor;
Motor motorA = Motor(A0, A1);
Relay relay1 = Relay(4);
TemperatureSensor  sensorTemp1 = TemperatureSensor(A6);

//Auxiliar Functions
void defineAction(byte displayResponse[8]){
  byte byte1 = displayResponse[1];  // Botón->Error | Slider -> Identificador de memoria 
  byte byte2 = displayResponse[2];  // boton->Página desde donde llega la información desde la pantalla | slider-> Valor del componente
  byte byte3 = displayResponse[3];  // Identificación del componente que ha enviado la información desde la pantalla
  byte byte4 = displayResponse[4];  // Evento del componente que se ha enviado
  byte byte5 = displayResponse[5];  // fin de envío FF
  byte byte6 = displayResponse[6];  // "
  byte byte7 = displayResponse[7];  // "
  if(byte1==113){
    servoMotor.write(byte2);
    delay(50);
  }  
  if(byte2==0 && byte3==2 && flagRelay1==false){
    relay1.changeState(true);
    flagRelay1=true;
    byte3=0;
    delay(5);                                       
  }
  if(byte2==0 && byte3==2 && flagRelay1==true){
    relay1.changeState(false);
    flagRelay1 = false;                          
    delay(5);                                 
  }
  if(byte2==0 && byte3==3 && flagMotorA==false){
    motorA.toTurn(false, true);
    flagMotorA=true;
    byte3=0;                         
    delay(5);                                 
  }
  if(byte2==0 && byte3==3 && flagMotorA==true){
    motorA.toStop();
    flagMotorA=false;                  
    delay(5);                                 
  }
}

void setup(){
  Serial.begin(9600);
  servoMotor.attach(8);
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
