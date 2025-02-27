#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <DHT11.h>

#define DHTPIN A1
#define MQ135 A0
#define BUZZER 6
#define GREEN_LED 4
#define YELLOW_LED 3
#define RED_LED 2

DHT11 dht(DHTPIN);
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  pinMode(MQ135, INPUT);
  pinMode(BUZZER, OUTPUT);
  pinMode(GREEN_LED, OUTPUT);
  pinMode(YELLOW_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);

  Serial.begin(9600);
  
  lcd.init();
  lcd.backlight();
}

void loop() {
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print(" Air Quality");
  lcd.setCursor(0, 1);
  lcd.print("   Monitor");
  delay(2000);

  float temp = dht.readTemperature();
  float humidity = dht.readHumidity();

  if (isnan(temp) || isnan(humidity)) {
    Serial.println("DHT Sensor Error! Retrying...");
    delay(500);
    temp = dht.readTemperature();
    humidity = dht.readHumidity();
  }

  if (isnan(temp) || isnan(humidity)) {
    Serial.println("DHT Sensor Failed!");
    lcd.clear();
    lcd.print("DHT Sensor Error");
    delay(2000);
    return;
  }

  int air_quality_raw = analogRead(MQ135);
  float air_quality_ppm = (1000.0 * air_quality_raw) / 1024.0;
  int AQI = map(air_quality_ppm, 0, 400, 0, 300);

  Serial.print(millis());
  Serial.print(",");
  Serial.print(temp);
  Serial.print(",");
  Serial.print(humidity);
  Serial.print(",");
  Serial.print(air_quality_ppm);
  Serial.print(",");
  Serial.println(AQI);

  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("AQI Value: " + String(AQI));

  String stats = "T:" + String(temp) + "C H:" + String(humidity) + "%";
  lcd.setCursor(0, 1);
  lcd.print(stats);
  delay(2000);  

  for (int i = 0; i < 8; i++) {  
    lcd.scrollDisplayLeft();
    delay(600);  
  }

    for (int i = 0; i < 8; i++) {  
    lcd.scrollDisplayRight();
    delay(600);  
  }
  delay(1000);  

  digitalWrite(GREEN_LED, LOW);
  digitalWrite(YELLOW_LED, LOW);
  digitalWrite(RED_LED, LOW);

  if (AQI < 50) {
    digitalWrite(GREEN_LED, HIGH);
  } else if (AQI >= 50 && AQI < 100) {
    digitalWrite(YELLOW_LED, HIGH);
  } else {
    digitalWrite(RED_LED, HIGH);
    digitalWrite(BUZZER, HIGH);
    delay(500);
    digitalWrite(BUZZER, LOW);
  }
}
