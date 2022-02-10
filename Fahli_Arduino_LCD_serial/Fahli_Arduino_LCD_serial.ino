// Fahli_Arduino_LCD_serial 
// this sketch receives a 10-char long string via TX-RX serial comm
// this string contains coded two concatenated strings each 5 chars
// - a temperature string of two numbers - period - two numbers
// - a humidity string of two numbers - period - two numbers    
// the 10 char 'receivestring_ch' is broken up into two strings of five chars
// next the strings are converted into floats with the atof function
// and then sent to LCD display 
// Floris Wouterlood - July 20 1017
// public domain

#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

String receivestring_ch;
String temp_ch;
String umidade_ch;


void setup()
{
   lcd.begin(16, 2);
   Serial.begin(9600);

}

void loop()
{

 while(Serial.available()){ 
    delay(10);
    if (Serial.available() >0) {
           char c = Serial.read();                     // gets one byte from serial buffer
           receivestring_ch += c;                      // construct the string
       }
    }
    
 if (receivestring_ch.length() >0) {
     Serial.print("receivestring_ch = ");              // see what was received
     Serial.println(receivestring_ch);                 // see what was received
     
// == expect a string like 15.0060.00 containing the suhu and kelembapan (tempo, humidity) ==  

     temp_ch = receivestring_ch.substring(0, 4);       // get the first five characters
     umidade_ch = receivestring_ch.substring(5, 9); // get the next five characters

     receivestring_ch = ""; //  
     Serial.print("temp_ch = ");                       
     Serial.println(temp_ch);                          // see what was received
     Serial.print("umidade_ch = ");                 
     Serial.println(umidade_ch);                    // see what was received
     Serial.println();                                 // clear the receivestring_ch


     float temp_fl = 0.00;                             // declare float for temp
     float umidade_fl = 0.00;                       // declare float for humidity

     
     char carray1[6];                                  // magic needed to convert string to a number
     temp_ch.toCharArray(carray1, sizeof(carray1));
     temp_fl = atof(carray1);
     
     char carray2[6];
     umidade_ch.toCharArray(carray2, sizeof(carray2));
     umidade_fl = atof(carray2);

  {
  
 }
   
   lcd.setCursor(0, 0);                                // LCD control
   lcd.print("Temp||Umidade");

   lcd.setCursor(0, 1);
   lcd.print(temp_fl,2);
   
   lcd.setCursor(10, 1);     
   lcd.print(umidade_fl,2);

   temp_fl=0;                                           // cleear suhu_fl
   umidade_fl=0;                                     // clkear kelembapan_fl

   delay(1000);
  
}
}





  
