const int button1 = 2;        // defining button1 for port d2
const int button2 = 3;        // button2 for port d3
const int buzzer1 = 9;        // buzzer1 for port d9
const int buzzer2 = 10;       // buzzer2 for port d10

int winner = 0;               // Set to 0 initially, n changes to 1 (player1) and 2 (player2) accordingly based on outcome
unsigned long lockedtime = 0;
const unsigned long roundms = 5000;  // Lets say round last around 5ms 

void setup(){
  pinMode(button1, INPUT_PULLUP);
  pinMode(button2, INPUT_PULLUP);
  pinMode(buzzer1, OUTPUT);
  pinMode(buzzer2, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  // State low/0 (when pushed) and high/1 (when unpressed)
  int state1 = digitalRead(button1);   
  int state2 = digitalRead(button2);
  // Locking the first player to press push button
  // Also using millis() to return number of ms passed
  if (winner == 0){
    if (state1 == LOW){
      winner = 1; lockedtime = millis(); 
    }
    else if (state2 == LOW){
      winner = 2;
      lockedtime = millis(); 
    }
  }
  int out1 = state1;
  int out2 = state2;
  // Forcing player 2 such that they cannot press
  if (winner == 1){
    out2 = HIGH;
  }
  // Forcing player 1 such that they cannot press  
  if (winner == 2){
    out1 = HIGH;  
  }
  Serial.print(out1);
  Serial.print(",");
  Serial.println(out2);

  // ----- BUZZER: only winner can buzz, only while holding -----
  if (winner == 1){
    if (state1 == LOW){
      tone(buzzer1, 1200);
    }
    else{
      noTone(buzzer1);
    }
    noTone(buzzer2);
   } 
   else if (winner == 2){
    if (state2 == LOW){
      tone(buzzer2, 1200);
    }
    else{
      noTone(buzzer2);
    }
    noTone(buzzer1);
  }
  else {
    noTone(buzzer1);
    noTone(buzzer2);
  }

  // Auto resetting after one round 
  // Earlier when someone answers the round we store the time they press it first in lockedtime
  // Basically with this diff we r able to figure out how long it takes for the next person to hit buzzer
  if (winner != 0 && (millis() - lockedtime) > roundms) {
    winner = 0;
    noTone(buzzer1);
    noTone(buzzer2);
  }
  delay(50);
}