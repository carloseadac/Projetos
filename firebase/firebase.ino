#include <WiFi.h>
#include <FirebaseESP32.h>
#include "DHT.h"
  
#define WIFI_SSID "Qwertyuiop"
#define WIFI_PASSWORD "carlo2233"
#define FIREBASE_HOST "https://dsmod3-default-rtdb.firebaseio.com/"
#define FIREBASE_AUTH "4k6JNrElbIda17kE2eqdhFayrlY8yuMU9lcKKBBE"

#define DHTPIN 4
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

FirebaseData firebaseData;
FirebaseJson json;

void setup() {
  // put your setup code here, to run once:
  
  Serial.begin(9600);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    delay(300);
  }
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());

  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);
  Firebase.setReadTimeout(firebaseData, 1000 * 60);
  Firebase.setwriteSizeLimit(firebaseData, "tiny");
  dht.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  float t = dht.readTemperature();
  float h = dht.readHumidity();
  
  json.set("/temperatura", t);
  json.set("/humidade", h);
  Firebase.updateNode(firebaseData, "/Sensor/murilo", json);
}
