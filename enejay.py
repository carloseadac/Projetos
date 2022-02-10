

#include <FirebaseESP32.h>


#include <LiquidCrystal.h>
#include <DHT.h>
#include <PubSubClient.h>
#include <WiFi.h>
#define ANALOG_PIN A0
// Create An LCD Object. Signals: [ RS, EN, D4, D5, D6, D7 ]
LiquidCrystal My_LCD(13, 12, 14, 27, 26, 25);


// Set these to run example.
#define FIREBASE_HOST "projettaprata-default-rtdb.firebaseio.com"
#define FIREBASE_AUTH "HBgMgpLEgC9VofRykMoTu6nSrun5BETlLfHjLGdY"
#define WIFI_SSID "Siqueira"
#define WIFI_PASSWORD "joaovitor50"

FirebaseData firebaseData;
FirebaseJson json;

void setup() {

  pinMode(ANALOG_PIN, INPUT);
  Serial.begin(9600);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("conectando");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  Serial.println();
  Serial.print("conectado: ");
  Serial.println(WiFi.localIP());
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);

  // Initialize The LCD. Parameters: [ Columns, Rows ]
  My_LCD.begin(16, 2);
  // Clears The LCD Display
  My_LCD.clear();
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);
  Firebase.setReadTimeout(firebaseData, 1000 * 60);
  Firebase.setwriteSizeLimit(firebaseData, "tiny");
}

void loop()
{
  int l = readLDRSensor();

  Serial.print("Luminosidade: ");
  Serial.println(l);
  json.set("/luminosidade", l);
  Firebase.updateNode(firebaseData, "/Sensor/luminosidade", json);
  My_LCD.print("lumi:");
  My_LCD.setCursor(5, 1);
  My_LCD.print(l);
  delay(5000);
}
//
int readLDRSensor(){
  int ldrValue = map(analogRead(ANALOG_PIN),0,4095,0,100);
  return ldrValue;
}
//

import requests
import json
import matplotlib.pyplot as plt


def sinal():
 proxies = {'https': "http://disrct:saladigital0311@10.224.200.26:8080/"}
 lumi = "https://projeto-ldr-default-rtdb.firebaseio.com/Sensor/luminosidade.json"
 luminosidade = int(requests.get(lumi, proxies=proxies).content)
 return luminosidade

import pyodbc
def InserirBD(sinal):
 server = 'JVLPC0481\SQLSERVER'
 database = 'Projeto_LDR'
 username = 'Nicholas'
 password = 'admin'
 cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
 cursor = cnxn.cursor()
 cursor.execute(f"INSERT dbo.Sensor (luminosidade) VALUES ({sinal});")
 cursor.commit()
 print("Inserido com sucesso!")
 
 
def apresentar(sinal):
 print(sinal)
 
import time
while True:
    valores=sinal()
    print(valores)
    apresentar(valores)
    InserirBD(valores)
    time.sleep(15);