#include <RH_ASK.h>
#include <SPI.h>
#include <Arduino.h>

RH_ASK rf_driver;

void setup()
{
  rf_driver.init();
  Serial.begin(9600);
}

void loop()
{
  uint8_t buf[11];
  uint8_t buflen = sizeof(buf);

  if (rf_driver.recv(buf, &buflen))
  {
    Serial.print("Message Recieved: ");
    Serial.println((char *)buf);
  }
}