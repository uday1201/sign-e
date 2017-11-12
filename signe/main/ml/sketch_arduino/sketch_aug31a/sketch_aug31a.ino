

#include "Wire.h"
 
// I2Cdev and MPU6050 must be installed as libraries, or else the .cpp/.h files
// for both classes must be in the include path of your project
#include "I2Cdev.h"
#include "MPU6050.h"
 
 
// class default I2C address is 0x68
// specific I2C addresses may be passed as a parameter here
// AD0 low = 0x68 (default for InvenSense evaluation board)
// AD0 high = 0x69
MPU6050 accelgyro;
 
int16_t ax, ay, az;
int16_t gx, gy, gz;


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
 Wire.begin();
 accelgyro.initialize();
}



void loop()
{  
    value0 = analogRead(flexpin0);
    value1 = analogRead(flexpin1);
    value2 = analogRead(flexpin2);
    value3 = analogRead(flexpin3);
    //thumb
    Serial.print(value0);
    Serial.print(" ");
    //index
    Serial.print(value1);
    Serial.print(" ");
    //middle
    Serial.print(value2);
    Serial.print(" ");
    //chi chi
    Serial.print(value3);
    // read raw accel/gyro measurements from device
    accelgyro.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
 
    // these methods (and a few others) are also available
    //accelgyro.getAcceleration(&ax, &ay, &az);
    //accelgyro.getRotation(&gx, &gy, &gz);
 
    // display tab-separated accel/gyro x/y/z values
    Serial.print(" ");
    Serial.print(ax); 
    Serial.print(" ");
    Serial.print(ay);
    Serial.print(" ");
    Serial.print(az);
    Serial.print(" ");
    Serial.print(gx);
    Serial.print(" ");
    Serial.print(gy);
    Serial.print(" ");
    Serial.println(gz);
    delay(1000);
}

