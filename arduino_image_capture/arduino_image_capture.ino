// Arduino Serial-controlled LED example
const int LASER_PIN_1 = 1;
const int LASER_PIN_2 = 4;
const int LASER_PIN_3 = 8;
const int LASER_PIN_4 = 11;
String line = "";

void setup() {
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);
  Serial.begin(115200); // make sure Python uses the same baud
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();
    if (c == '\n') {
      line.trim();
      if (line == "LASER ON"){
        digitalWrite(LASER_PIN_1, HIGH);
        digitalWrite(LASER_PIN_2, HIGH);
        digitalWrite(LASER_PIN_3, HIGH);
        digitalWrite(LASER_PIN_4, HIGH);
      }
      else if (line == "LASER OFF") {
        digitalWrite(LASER_PIN, LOW);
      }
      else if (line.startsWith("PWM ")) {
        int val = line.substring(4).toInt(); // 0-255
        analogWrite(9, constrain(val,0,255)); // example PWM on pin 9
      }
      Serial.println("OK"); // simple acknowledgement
      line = "";
    } else {
      line += c;
    }
  }
}
