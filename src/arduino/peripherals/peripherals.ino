const int HELLO_BUTTON = 13;
const int APP_BUTTON = 12;

int oldHelloButtonVal = 0;
int helloButtonState = 0;

int oldAppButtonVal = 0;
int appButtonState = 0;

void setup() {
  Serial.begin(9600);
  pinMode(HELLO_BUTTON, INPUT);
  pinMode(APP_BUTTON, INPUT);
}

void loop() {
  checkHelloButton();
  checkAppButton();
}

void checkHelloButton() {
  int buttonVal = digitalRead(HELLO_BUTTON);
  if ((buttonVal == HIGH) && (oldHelloButtonVal == LOW)) {
    int buttonState = 1 - helloButtonState;
    Serial.println("HELLO");
  }
  oldHelloButtonVal = buttonVal;
}

void checkAppButton() {
  int buttonVal = digitalRead(APP_BUTTON);
  if ((buttonVal == HIGH) && (oldAppButtonVal == LOW)) {
    int buttonState = 1 - appButtonState;
    Serial.println("APP");
  }
  oldAppButtonVal = buttonVal;
}


