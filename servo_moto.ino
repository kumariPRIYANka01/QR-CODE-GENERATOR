

#include <Servo.h>
 Servo servo1;

 Servo servo3;
 
 int pos;

 void setup(){
  servo1.attach(3);
 
  
    servo3.attach(4);
 }
 void loop(){
  for(pos=0;pos<180;pos++){
    servo1.write(pos);
     
         servo3.write(pos);
   
    
  }
  delay(1000);
  for(pos=180;pos<=0;pos--){
    servo1.write(pos);
     
         servo3.write(pos);
   
  }
   delay(1000);
 }
 
