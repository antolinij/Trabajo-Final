int IN1 = 2; 
int IN2 = 3;
int IN3 = 5; 
int IN4 = 4;


void setup()
{
  Serial.begin(9600);
  pinMode (IN4, OUTPUT); 
  pinMode (IN3, OUTPUT); 
  pinMode (IN2, OUTPUT);   
  pinMode (IN1, OUTPUT); 
}

void loop(){
  
  while (Serial.available() > 0) {
    
    char inChar = (char)Serial.read();
    switch(inChar) {
      case '0':
        digitalWrite (IN4, LOW);
        digitalWrite (IN1, LOW);
        digitalWrite (IN3, LOW);
        digitalWrite (IN2, LOW);
        Serial.print("STOP");
      break;
      case '1':
        digitalWrite (IN4, LOW);
        digitalWrite (IN1, LOW);
        digitalWrite (IN3, HIGH); 
        digitalWrite (IN2, HIGH); 
        Serial.print("REVERSE..."); 
      break;
      case '2':
        digitalWrite (IN4, HIGH);
        digitalWrite (IN1, HIGH);
        digitalWrite (IN3, LOW); 
        digitalWrite (IN2, LOW);
        Serial.print("FORWARD"); 
      break;
    }
  
  }
}
   
