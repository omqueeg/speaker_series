# How To Get RFID on your Raspberry Pi Pico
*For my besties who love RFID*

## The Code
- mfrc522.py goes in the "lib" folder on your Pico.
- code.py goes directly onto the Pico, in no folder.

## The Pinout
*Simplified Pico Diagram*

![image](https://user-images.githubusercontent.com/87877397/168765322-e54c4797-dac0-4a39-9159-922dfad77c69.png)


|RFID RC522 | Pico| # on Simplified Pico Diagram |
|:---:| :---:| :---: |
|3V3 | 3V3| 36|
|RST|GP8| 11 |
|GND|GND| 38 |
|IRQ| *---*| *--* |
|MISO| GP4| 06|
|MOSI| GP7| 10 |
|SCK|GP6| 09 |
|SDA|GP5| 05 |

