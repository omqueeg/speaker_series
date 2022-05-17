# How To Get RFID on your Raspberry Pi Pico
*For my besties who love RFID*

## The Code
- mfrc522.py goes in the "lib" folder on your Pico.
- code.py goes directly onto the Pico, in no folder.

## The Pinout
|RFID RC522 | Pico|
|:---:| :---:|
|3V3 | 3V3|
|RST|GP8|
|GND|GND|
|IRQ| *nothing*|
|MISO| GP4|
|MOSI| GP7|
|SCK|GP6|
|SDA|GP5|

