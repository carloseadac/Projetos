

#include <DHT.h>
#include <WiFi.h>
#include <FirebaseESP32.h>

#define WIFI_SSID "Vivo-Internet-BF17"
#define WIFI_PASSWORD "78814222"
#define FIREBASE_HOST "https://projettaprata-default-rtdb.firebaseio.com/"
#define FIREBASE_AUTH "HBgMgpLEgC9VofRykMoTu6nSrun5BETlLfHjLGdY"

FirebaseData firebaseData;
FirebaseJson json;

#define DHTPIN 4     
#define DHTTYPE DHT11  

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
  Firebase.reconnectWiFi(true);
  Firebase.setReadTimeout(firebaseData, 1000*60);
  Firebase.setwriteSizeLimit(firebaseData, "tiny"); 
  dht.begin();
  WiFi.begin(WIFI_SSID,WIFI_PASSWORD);
  
  Serial.begin(9600);
  
  while(WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    delay(300);
  }
  Serial.print("\nConnected with IP: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  
  json.set("/temperatura",dht.readTemperature());
  json.set("/umidade", dht.readHumidity());
  Serial.print(dht.readTemperature());
  Serial.print(dht.readHumidity());
  Firebase.updateNode(firebaseData, "/Sensor", json);
}
