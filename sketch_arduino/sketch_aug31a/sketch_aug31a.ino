


const int flexpin0 = A0 , flexpin1 = A1 , flexpin2 = A2 , flexpin3 = A3;
// A3 -> thumb , a2-> index finger , a1-> middle finger , a0 -> little finger
int value0 , value1 , value2 ,value3; // for saving values
const float VCC = 4.98; // Measured voltage of Ardunio 5V line
const float R_DIV = 10000.0; // Measured resistance of 10k resistor




// value > 300 -> no bend
//((f<300)&&(f>260))    -> small bend



void setup()
{
 pinMode(flexpin0 , INPUT);
 pinMode(flexpin1 , INPUT);
 pinMode(flexpin2 , INPUT);
 pinMode(flexpin3 , INPUT); 
 Serial.begin(9600);
}



void loop()
{  
    value0 = analogRead(flexpin0);
    value1 = analogRead(flexpin1);
    value2 = analogRead(flexpin2);
    value3 = analogRead(flexpin3);
    Serial.print("little Finger :");
    Serial.println(value0);
    Serial.print("middle Finger :");
    Serial.println(value1);
    Serial.print("index Finger :");
    Serial.println(value2);
    Serial.print("Thumb Finger :");
    Serial.println(value3);



  Serial.println();




 

    delay(1000);
}

