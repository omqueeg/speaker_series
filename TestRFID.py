#Produces Identification Code For Each RFID Tag Scanned

import digitalio
import board
import busio
import mfrc522
import time

sck = board.SCK
mosi = board.MOSI
miso = board.MISO
spi = busio.SPI(sck, MOSI=mosi, MISO=miso) #Are sck, mosi, & miso necessary??)
cs = digitalio.DigitalInOut(board.A5)
rst = digitalio.DigitalInOut(board.A2)
rfid = mfrc522.MFRC522(spi, cs, rst)
rfid.set_antenna_gain(0x07 << 4)

print("\n***** Scan your RFid tag/card, then CTRL-SHIFT-C the UID *****\n")

prev_data = ""
prev_time = 0
timeout = 1

while True:
    (status, tag_type) = rfid.request(rfid.REQALL)

    if status == rfid.OK:
        (status, raw_uid) = rfid.anticoll()

        if status == rfid.OK:
            rfid_data = "{:02x}{:02x}{:02x}{:02x}".format(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])

            if rfid_data != prev_data:
                prev_data = rfid_data
                print("Card detected! UID: {}".format(rfid_data))
            else:
                print("Something new please!")
            prev_time = time.monotonic()

    else:
        if time.monotonic() - prev_time > timeout:
            prev_data = prev_data
            #prev_data = ""
