// our button pins
const int button1 = 2;
const int button2 = 3;

void setup() {
  pinMode(button1, INPUT_PULLUP); 
  pinMode(button2, INPUT_PULLUP); 
  Serial.begin(9600);
}

void loop() {
  int state1 = digitalRead(button1); // reads 1 or 0 (0 = pressed)
  int state2 = digitalRead(button2); // reads 1 or 0
  // send both inputs to computer
  Serial.print(state1);
  Serial.print(",");  
  Serial.println(state2); 
  delay(200);
}


