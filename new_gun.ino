/* HELLO EVERBODY I AM SATINDER SINGH AND I AM A ENGINEERING STUDENT AT ARMY INSTITUTE OF TECHNOLOGY 
 *  THIS IS MY PROJECT FOR AUTOMATIC TARGET DETECTION USING OPENCV IN PYTHON AND THEN   ARDUINO CONTOLLS THE SERVO'S  TO ALLIGN TO THE TARGET AND THEN SHOOT
 *  IT'S BEEN THREE WEEKS THAT I WAS DOING THIS PROJECT AND I NOW IT IS COMPLETE
 *  THIS IS THE ARDUINO CODE 
 *  I HAVE USED THE FOLLOWING THINGS
 *  3 SERVO MOTORS
 *  ARDUINO UNO 
 *  MOTOR DRIVER
 *  JUMPER CABLES
 *  LAPTOP OR PC WITH WEBCAM WITH PYTHON AND OPENCV INSTALLED
 *  A TOY GUN
 *  
 *  
 *  *****************************************************************************************************************************************************************************************
 *  CHECK OUT MY YOUTUBE CHANNEL "REACTOR SCIENCE" FOR VIDEO TUTORIAL
 */




#include<Servo.h>                     //including the servo library
Servo x,y,z;                          //making objects of class servo
int a;                                //making a variable of type int in which I will receive the data comming from the serial input
int horizontal=90;                    //making horizontal and vertical variable and setting their position to 90 degree which is going to be the initial position of my servo's
int vertical=90;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);                  //starting a serial connection to send and receive data serially

x.attach(2);                         //attaching the servo's to their respective pins
y.attach(3);
z.attach(11);
z.write(90);                         //initally the servo controlling the trigger of the gun is at disarmed position
delay(1000);
}

void loop() {
  // put your main code here, to run repeatedly:
if(Serial.available()>0)             //checking if there is a serial connection available

{
  a=Serial.read();                   //reading whatever received in variable "a"
  if(a=='1')                         //if '1' is received then the servo controlling the servo is set to 0 which means the gun is shooting now
  {z.write(0);
  
  delay(1000);
  z.write(90);                      //as soon as the gun is shot then the servo returns back to the disarmed position
  delay(1000);
  Serial.println("shooted");       //sending "shooted" to the python monitor
  delay(1000);                     
  }
  else if(a=='2')                 //python will send '2' until the gun has to move right and thus the horizontal variable is incremented and postion is fed to the servo
  {
   horizontal=horizontal+2;
   x.write(horizontal);
   delay(15);
   Serial.println("ALLIGNING TOWARDS THE TARGET.............");
    }
  else if(a=='3')                 //python will send '3' until the gun has to move left and thus the horizontal variable is incremented and postion is fed to the servo
  {
   horizontal=horizontal-2;
   x.write(horizontal);
   delay(15);
   Serial.println("ALLIGNING TOWARDS THE TARGET.............");  
    }
  else if(a=='4')                 //python will send '4' until the gun has to move up and thus the vertical variable is incremented and postion is fed to the servo
  {
   vertical=vertical+2;
   y.write(vertical);
   delay(15);
   Serial.println("ALLIGNING TOWARDS THE TARGET.............");   
    }
  else if(a=='5')                 //python will send '5' until the gun has to move donw and thus the vertical variable is incremented and postion is fed to the servo
  {
   vertical=vertical-2;
   y.write(vertical);
   delay(15);
   Serial.println("ALLIGNING TOWARDS THE TARGET.............");
    }

  }
}
