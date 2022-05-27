#Final Code Template

import os

import digitalio
import board
import busio
import mfrc522
import time
import sdcardio
import storage
from audioio import AudioOut
from audiomp3 import MP3Decoder

sck = board.SCK
mosi = board.MOSI
miso = board.MISO
spi = busio.SPI(sck, MOSI=mosi, MISO=miso)
cs_sd = board.D10
sdcard = sdcardio.SDCard(spi, cs_sd)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

cs_rfid = digitalio.DigitalInOut(board.A5)
rst = digitalio.DigitalInOut(board.A2)
rfid = mfrc522.MFRC522(spi, cs_rfid, rst)
rfid.set_antenna_gain(0x07 << 4)
audio = AudioOut(board.A0)

all_playlists = {
05230230 : "/sd/playlists/sadboyplaylist",
05230233 : "/sd/playlists/goodtimesplaylist",
05230231 : "/sd/playlists/partymix",
}
prev_data = ""
prev_time = 0
timeout = 1

print("\n***** Scan your RFid tag/card *****\n")

def play_song(folder):
    print("Current Playlist: " + folder[14:])
    # The listed mp3files will be played in order
    mp3files = os.listdir(folder)

    # You have to specify some mp3 file when creating the decoder
    mp3 = open(mp3files[0], "rb")
    decoder = MP3Decoder(mp3)


    for filename in mp3files:
            # Updating the .file property of the existing decoder
            # helps avoid running out of memory (MemoryError exception)
            decoder.file = open(filename, "rb")
            audio.play(decoder)
            print("playing", filename)

            # This allows you to do other things while the audio plays!
            while audio.playing:
                (status, tag_type) = rfid.request(rfid.REQALL)
                if status == rfid.OK and rfid_data in all_playlists.keys():
                    mp3.close()
                    decoder.file.close()
                    play_song(all_playlists[rfid_data])
                pass
            mp3.close()
            decoder.file.close()

while True:
    (status, tag_type) = rfid.request(rfid.REQALL)

    if status == rfid.OK:
        (status, raw_uid) = rfid.anticoll()

        if status == rfid.OK:
            rfid_data = "{:02x}{:02x}{:02x}{:02x}".format(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])

            if rfid_data in all_playlists.keys():
                play_song(all_playlists[rfid_data])
            else:
                print("Error: Unrecognized RFID Card.")
            prev_time = time.monotonic()

    else:
        if time.monotonic() - prev_time > timeout:
            prev_data = prev_data
