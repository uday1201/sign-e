
const int flexpin0 = A0 , flexpin1 = A1 , flexpin2 = A2 , flexpin3 = A3, flexpin4 = A4;

int value0 , value1 , value2 ,value3, value4; // for saving values
const int trainPin = 12;

void setup()
{
 pinMode(flexpin0 , INPUT);
 pinMode(flexpin1 , INPUT);
 pinMode(flexpin2 , INPUT);
 pinMode(flexpin3 , INPUT); 
 pinMode(flexpin4 , INPUT);
 pinMode(12, INPUT);
 Serial.begin(9600);
}



void loop()
{  
    value0 = analogRead(flexpin0);
    value1 = analogRead(flexpin1);
    value2 = analogRead(flexpin2);
    value3 = analogRead(flexpin3);
    value4 = analogRead(flexpin4);
    //thumb
    Serial.print(value0);
    Serial.print(" ");
    //index
    Serial.print(value1);
    Serial.print(" ");
    //middle
    Serial.print(value2);
    Serial.print(" ");
    //ring
    Serial.print(value3);
    Serial.print(" ");
    //chi chi
    Serial.println(value4);
    if (digitalRead(12))
      delay(200);
    else
      delay(1000);
}
