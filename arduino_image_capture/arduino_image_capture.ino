#include <Wire.h>
#include <SPI.h>
#include <ArduCAM.h>
#include "memorysaver.h"

#define CS_PIN 7

ArduCAM myCAM(OV2640, CS_PIN);

void setup() {
  Wire.begin();
  Serial.begin(115200);
  SPI.begin();

  pinMode(CS_PIN, OUTPUT);
  myCAM.write_reg(ARDUCHIP_TEST1, 0x55);
  if (myCAM.read_reg(ARDUCHIP_TEST1) != 0x55) {
    Serial.println("Camera not found!");
    while (1);
  }

  myCAM.set_format(JPEG);
  myCAM.InitCAM();
  myCAM.OV2640_set_JPEG_size(OV2640_640x480);
  delay(1000);
  Serial.println("READY");
}

void loop() {
  myCAM.flush_fifo();
  myCAM.clear_fifo_flag();
  myCAM.start_capture();
  Serial.println("CAPTURING...");
  while (!myCAM.get_bit(ARDUCHIP_TRIG, CAP_DONE_MASK));

  uint32_t length = myCAM.read_fifo_length();
  Serial.print("SIZE:");
  Serial.println(length);

  myCAM.CS_LOW();
  myCAM.set_fifo_burst();
  const uint8_t BURST_FIFO_READ = 0x3C;
  SPI.transfer(BURST_FIFO_READ);
  
  while (length--) {
    uint8_t b = SPI.transfer(0x00);
    Serial.write(b); // send raw bytes to PC
  }
  myCAM.CS_HIGH();
  Serial.println("DONE");
  delay(10000);
}
