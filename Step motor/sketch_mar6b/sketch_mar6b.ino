
const int analogInPin = A0;
const int analogOutPin = 9;
const int motorPin = 3;

void setup() 
{
  // DC power
  Serial.begin(9600);       // Start serial for monitoring
  pinMode(analogInPin, INPUT);         // Not strictly necessary, default is INPUT

  // Step motor
  pinMode(2, OUTPUT);
  pinMode(motorPin, OUTPUT);
  digitalWrite(2, HIGH);
}


void step(int s)
{
  for (int i = 0l; i < s; i++)
  {
    digitalWrite(motorPin, HIGH);
    delayMicroseconds(60);
    digitalWrite(motorPin, LOW);
    delayMicroseconds(60);
  }
}

void loop()
{
  // Read the analog input and convert it to a voltage (5V reference)
  // int sensorValue = analogRead(analogInPin);
  // float voltage = sensorValue * (5.0 / 4095.0);

  analogWrite(analogOutPin, 120); // PWM, 0-255 is the duty cycle

  // Print it out
  // Serial.print("Analog reading = ");
  // Serial.print(sensorValue);
  // Serial.print(" | Voltage ~ ");
  // Serial.println(voltage);

  // delay(500); // Half a second between reads

  // Read input
  if (Serial.available())
  {
    String command = Serial.readStringUntil('\n');
    command.trim();
    switch (command.charAt(0))
    {
      case 's':
      {
        int steps = command.substring(2).toInt();
        step(steps);
        Serial.print("Stepped ");
        Serial.print(steps);
        Serial.println(" steps.");
        break;
      }
      default:
      {
        Serial.print("Unkown command: ");
        Serial.println(command);
        break;
      }
    }
  }
}


// Make sure the capacitor ground is the same as the transistor ground