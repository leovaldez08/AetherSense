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

// Calibration constants
const float R_L = 20.0;  // Load resistance in kΩ
const float T0 = 20.0;   // Reference temperature
const float H0 = 65.0;   // Reference humidity
const float alpha = 0.01;  // Temperature coefficient
const float beta = 0.03;   // Humidity coefficient

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

  // Read raw sensor value
  int air_quality_raw = analogRead(MQ135);

  // Calculate sensor resistance (R_s)
  float R_s = ((1023.0 / air_quality_raw) - 1) * R_L;

  // Calculate PPM
  float PPM = 1000.0 / R_s;

  // Correct PPM for temperature and humidity
  float PPM_corrected = PPM / (1 + alpha * (temp - T0) + beta * (humidity - H0));

  // Map PPM to AQI
  int AQI;
  if (PPM_corrected <= 50) {
    AQI = map(PPM_corrected, 0, 50, 0, 50);  // Good
  } else if (PPM_corrected <= 100) {
    AQI = map(PPM_corrected, 51, 100, 51, 100);  // Moderate
  } else if (PPM_corrected <= 200) {
    AQI = map(PPM_corrected, 101, 200, 101, 200);  // Unhealthy
  } else if (PPM_corrected <= 300) {
    AQI = map(PPM_corrected, 201, 300, 201, 300);  // Very Unhealthy
  } else {
    AQI = map(PPM_corrected, 301, 500, 301, 500);  // Hazardous
  }

  // Print data to Serial Monitor
  Serial.print(millis());
  Serial.print(",");
  Serial.print(temp);
  Serial.print(",");
  Serial.print(humidity);
  Serial.print(",");
  Serial.print(PPM_corrected);
  Serial.print(",");
  Serial.println(AQI);

  // Display on LCD
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("AQI Value: " + String(AQI));
  lcd.setCursor(0, 1);
  lcd.print("T:" + String(temp) + "C H:" + String(humidity) + "%");
  delay(2000);

  // Scroll display
  for (int i = 0; i < 8; i++) {  
    lcd.scrollDisplayLeft();
    delay(600);  
  }
  for (int i = 0; i < 8; i++) {  
    lcd.scrollDisplayRight();
    delay(600);  
  }
  delay(1000);

  // Control LEDs and Buzzer
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