class Relay{
  /*3-5-6-9-10-11*/
  public:
    int pin;
  Relay(int number){
    pin=number;
    pinMode(pin, OUTPUT);
  }
  void changeState(bool ref){
    digitalWrite(pin, ref);
  }
  void pwmValue(int value){
    analogWrite(pin, value);
  }
};


class TemperatureSensor{
   /*A5-A6*/
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


class Motor{
  /*A0-A4*/
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
    }else{
      // TODO send error configuraction
    }
  }
  void toStop(){
    digitalWrite(pinA, LOW);
    digitalWrite(pinB, LOW);
  }
};

class Buzzer{
  //TODO
};

class ServoMotor{
  // TOD0
};
