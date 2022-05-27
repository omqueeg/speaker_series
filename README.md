# How To RFID
*For my besties who love RFIDs*

## The Code
- mfrc522.py goes in the "lib" folder on your board.
- code.py goes directly onto the board, in no folder.

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

