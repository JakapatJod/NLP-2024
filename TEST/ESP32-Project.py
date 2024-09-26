#define BLYNK_TEMPLATE_ID           "TMPL6o_O-0R6x"
#define BLYNK_TEMPLATE_NAME         "Quickstart Template"
#define BLYNK_AUTH_TOKEN            "JaAzCkavqzZ0a5-nU2jrBNuzqMTLyMXQ"

#define BLYNK_PRINT Serial

#include "DHT.h"

#define DHTPIN 4  // Pin GPIO 4 สำหรับ ESP32
#define DHTTYPE DHT22  

DHT dht(DHTPIN, DHTTYPE);


#include <WiFi.h>  // เปลี่ยนเป็น WiFi.h สำหรับ ESP32
#include <BlynkSimpleEsp32.h>  // เปลี่ยนเป็น BlynkSimpleEsp32.h

// Your WiFi credentials.
// Set password to "" for open networks.
char ssid[] = "jakapat";
char pass[] = "Jakapat12";

BlynkTimer timer;

BLYNK_CONNECTED()
{
  Blynk.setProperty(V3, "offImageUrl", "https://static-image.nyc3.cdn.digitaloceanspaces.com/general/fte/congratulations.png");
  Blynk.setProperty(V3, "onImageUrl",  "https://static-image.nyc3.cdn.digitaloceanspaces.com/general/fte/congratulations_pressed.png");
  Blynk.setProperty(V3, "url", "https://docs.blynk.io/en/getting-started/what-do-i-need-to-blynk/how-quickstart-device-was-made");
}

void myTimerEvent()
{
  Blynk.virtualWrite(V2, millis() / 1000);
}

void setup()
{
  Serial.begin(115200);

  Blynk.begin(BLYNK_AUTH_TOKEN, ssid, pass);

  timer.setInterval(1000L, myTimerEvent);
  dht.begin();
}

void loop()
{
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }
  Serial.print(F("Temperature: "));
  Serial.print(temperature , 1);
  Serial.print(F("°C : "));

  Serial.print(F("Humidity: "));
  Serial.print(humidity , 1);
  Serial.println(F("%"));
  delay(2000);

  Blynk.run();
  Blynk.virtualWrite(V6, temperature);
  Blynk.virtualWrite(V7, humidity);
  timer.run();
}
