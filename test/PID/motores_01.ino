nt ENA = 9; //pin 9 pwm
int IN1 = 8; // pin 8
int IN2 = 7; // pin 7
int IN3 = 6; // pin 6
int IN4 = 5; // pin 5
int ENB = 4; // pin 4 pwm

void setup (){
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  pinMode(ENB, OUTPUT);
 
  
}

void loop(){

  //main code 
  digitalWrite(IN1, LOW); // SI ES HIGH AVANZA 
  digitalWrite(IN2, LOW); // EL PIN 7 SE MANTENDRA APAGADO
  analogWrite(ENA,106);
  
  //MOTOR B
  digitalWrite(IN3, LOW); // EL PIN 8 EMITIRA 5V
  digitalWrite(IN4, LOW); // EL PIN 7 SE MANTENDRA APAGAD
  analogWrite(ENB,106);
   
}
