''' HELLO EVERBODY I AM SATINDER SINGH AND I AM A ENGINEERING STUDENT AT ARMY INSTITUTE OF TECHNOLOGY,PUNE,MAHARASHTRA,INDIA 
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
 '''


#IMPORTING THE NECESSARY LIBRARIES
import cv2                                                          #OPENCV FOR VIDEO PROCESSING AND FOR REFERNCE YOU CAN USE THE OPEN CV PYTHON DOCUMENTATION
import numpy as np                                                  #NUMPY
import serial                                                       #SERIAL FOR COMMUNICATION WITH ARDUINO
import time                                                         #FOR GIVING DELAYS



ser=serial.Serial('COM4',9600,timeout=1)                            #MAKING A SERIAL VARIABLE

def shoot():                                                        #DEFINING FUNCTION SHOOT WHICH WRITES(OR SENDS) '1' SERIALLY TO ARDUINO TO WHICH ARDUINO FURTHER ACTS
    ser.write(b'1')                                                 #SENDING DATA TO ARDUINO
    data=ser.readline().decode('ascii')                             #RECEIVEING DATA FROM ARDUINO(WHICH ARE STRINGS)
    return data                                                     
def hAllignR():                                                     #DEFINING FUNCTION SHOOT WHICH WRITES(OR SENDS) '2' SERIALLY TO ARDUINO TO WHICH ARDUINO FURTHER ACTS
    ser.write(b'2')                                                 #SENDING DATA TO ARDUINO
    data=ser.readline().decode('ascii')
    return data
  
def hAllignL():                                                     #DEFINING FUNCTION SHOOT WHICH WRITES(OR SENDS) '3' SERIALLY TO ARDUINO TO WHICH ARDUINO FURTHER ACTS
    ser.write(b'3')                                                 #SENDING DATA TO ARDUINO
    data=ser.readline().decode('ascii')
    return data

def vAllignD():                                                     #DEFINING FUNCTION SHOOT WHICH WRITES(OR SENDS) '4' SERIALLY TO ARDUINO TO WHICH ARDUINO FURTHER ACTS
    ser.write(b'4')                                                 #SENDING DATA TO ARDUINO
    data=ser.readline().decode('ascii')
    return data
  
def vAllignU():                                                     #DEFINING FUNCTION SHOOT WHICH WRITES(OR SENDS) '5' SERIALLY TO ARDUINO TO WHICH ARDUINO FURTHER ACTS
    ser.write(b'5')                                                 #SENDING DATA TO ARDUINO
    data=ser.readline().decode('ascii')
    return data
    

    
cap=cv2.VideoCapture(0)                                             #CREATING A CAP VARIABLE THAT HOLDS THE FRAME FROM THE CAMERA
while(1):                                                           #STARTING INFINITE LOOP FOR CAPTURING VIDEOS
    __,frame=cap.read()                                             #FRAME VARIABLE READS THE VIDEOS STREAM FRAME BY FRAME FROM THE WEBCAM                      
    frame2=frame
    frame=cv2.flip(frame,1)                                         #AS THE VIDEO CAPTURED IS LATERALLY INVERSED TO I FLIP IT
    frame2=frame                                                    #AS I WILL BE ALTERING THE FRAME VARIABLE SO I MADE A COPY OF IT
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)                     #CONVERTED THE COLOURED FRAME IMAGE TO GRAY                   
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)                       #CONVERTED THE COLOURED FRAME IMAGE TO HSV BECAUSE CLOUR DETECTION IS BETTER IN CASE OF HSV






    #FIRSTLY I AM DETECTING THE RED LASER LIGHT
    
    lower1=np.array([0,100,100])                                    #AS HSV OF RED COLOR LIES IN THE RANGE OF [(0,100,100) TO (10,255,255)] OR[(160,100,100) TO (179,255,255)]
    upper1=np.array([10,255,255])
    lower2=np.array([160,100,100])
    upper2=np.array([179,255,255])


    #I HAVE MADE A MASK THAT CONTAINS ONLY THE HSV RANGES BETWEEN  [(0,100,100) TO (10,255,255)] WHICH CONTAINS COLORS WHICH ARE IN THIS RANGE
    mask1=cv2.inRange(hsv,lower1,upper1)

    #I HAVE MADE A MASK THAT CONTAINS ONLY THE HSV RANGES BETWEEN  [(160,100,100) TO (179,255,255)] WHICH ARE IN THIS RANGE
    mask2=cv2.inRange(hsv,lower2,upper2)


    #AS I WANTED TWO RANGES SO I PERFORMED " OR " OPERATION OF BOTH OF THEM 
    mask=cv2.bitwise_or(mask1,mask2)
    #NOW MASK CONTAINS ONLY RED COLOR IN THE COMPLETE IMAGE




    #NOW DRAWING CONTOURS FOR THIS WHICH IS GOING TO BE ONLY THE RED COLOR
    __,contours,__=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #DRAWING THE CONTOURS 
    cv2.drawContours(frame,contours,-1,(0,255,100),2)

    # INITAILING TWO VARIABLE 'A' AND 'B' AND THEY ARE GOING TO BE THE CENTER OF THE RED SPOT
    a=0
    b=0
    if(len(contours)>0):                                                  #IF RED WAS DETECTED
        for i in range(len(contours)):                                    #LOOPING BETWEEN ALL THE CONTOURS
            cnt=contours[i]                                               #CNT CONTAINS THE CONTOURS[I]
                                                               
            m=cv2.moments(cnt)                                            #GETTING THE MOMENTS OF THAT CONTOUR
            if(m['m00']!=0):                                              
                a=int(m['m10']/m['m00'])                                  #THIS GIVES THE CENTER(X COORDINATE) OF THE RED SPOT
                b=int(m['m01']/m['m00'])                                  #THIS GIVES THE CENTER(X COORDINATE) OF THE RED SPOT                         
     
    circles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1.5,100)             #HOUGH CIRCLE FINDS THE CIRCLES IN THE VIDEO
                    
    if(circles is not None):                                              #IF THE CIRCLE IS FOUND
        for i in circles:
            x=int(i[0][0])                                                #X XOORDINATE OF CENTER OF CIRCLE
            y=int(i[0][1])                                                #Y COORDINATE OF CENTER OF CIRCLE
            r=int(i[0][2])                                                #RADIUS OF THE CIRCLE
            r1=int(r/2)                                                   
            cv2.rectangle(frame,(x-r1,y-r1),(x+r1,y+r1),(0,0,255),2)      #DRAWING A SQUARE BETWENN A CIRCLE
            
            if((a>(x-r1))&(a<(x+r1))&(b>(y-r1))&(b<(y+r1))):              #IF THE LASER SPOT LIES BETWEEN THIS BOX THEN SHOOT AND GIVE 5 SECONDS DELAY
                print("shoot")
                print(shoot())
                time.sleep(5)
            elif(a<(x-r1)):                                               #IF THE LASER SPOT LIES TO THE LEFT OF THE BOX MOVE RIGHT
                print(hAllignR())
            elif(a>(x+r1)):                                               #IF THE LASER SPOT LIES TO THE RIGHT OF THE BOX MOVE LEFT
                print(hAllignL())

            elif(b<(y-r1)):                                               #IF THE LASER SPOT LIES BELOW THE RECTANGLE THEN MOVE UP
                print(vAllignU())
            elif(b>(y-r1)):                                               #IF  LASER THE SPOT LIES ABOVE THE RACTANGLE THEN MOVE DOWN
                print(vAllignD())
    cv2.imshow("frame",frame)                                             #SHOW THE VIDEO IMAGE BY IMAGE
    #cv2.imshow("frame2",frame2)           
    if cv2.waitKey(1)&0XFF==ord('q'):                                   # IF 'q' IS PRESSED THEN BREAK FROM THE LOOP
        break   
cap.release()                                                           #RELEASING CAP VARIABLE
cv2.destroyAllWindows()                                                 #DESTROYING ALL THE WINDOWS
