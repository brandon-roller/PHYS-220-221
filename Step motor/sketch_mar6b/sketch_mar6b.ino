// Brandon Roller, Aldiyar Zhumashov

const int directionPin = 2;
const int stepPin = 3;
const int analogOutPin = 9;

void setup()
{
  // Starts communication at 9500 baud
  Serial.begin(9600);

  // Sets all analog pins to input
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
  pinMode(A4, INPUT);
  pinMode(A5, INPUT);

  // Step motor
  pinMode(directionPin, OUTPUT);
  pinMode(stepPin, OUTPUT);
  digitalWrite(directionPin, HIGH); // Forwards, initially
}


// Step helper method
// Steps by a given integer of steps
void step(int s)
{

  // Reset step direction 
  if (s < 0)
  {
    // Backwards stepping
    digitalWrite(directionPin, LOW);
  }
  else
  {
    // Forwards stepping
    digitalWrite(directionPin, HIGH);
  }

  // Step s-many steps
  for (int i = 0; i < abs(s); i++)
  {
    digitalWrite(stepPin, HIGH);
    delayMicroseconds(60);
    digitalWrite(stepPin, LOW);
    delayMicroseconds(60);
  }

}


void loop()
{
  analogWrite(analogOutPin, 120); // PWM, 0-255 is the duty cycle

  // Read input
  // TODO: add a new command for analog in pins
  if (Serial.available())
  {
    String command = Serial.readStringUntil('\n');
    command.trim();
    switch (command.charAt(0))
    {
      case 's':  // Stepping
      {
        int steps = command.substring(2).toInt();
        step(steps);
        Serial.print("Stepped ");
        Serial.print(steps);
        Serial.println(" steps.");
        break;
      }
      case 'r':  // Reading
      {
        int pin = command.substring(2).toInt();

        // Read the analog input and convert it to a voltage with a 5V reference
        int sensorValue = analogRead(pin);
        float voltage = sensorValue * (5.0 / 4095.0);

        //Print the results
        Serial.print("Analog reading = ");
        Serial.print(sensorValue);
        Serial.print(" | Voltage ~ ");
        Serial.println(voltage);
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