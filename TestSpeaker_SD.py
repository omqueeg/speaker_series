import board
import busio
import sdcardio
import storage

spi = board.SPI()
cs = board.D10     # Use the pin you wired to the breakout CS

sdcard = sdcardio.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

#SD Card + Speaker test

import digitalio
from audioio import AudioOut
from audiomp3 import MP3Decoder

sck = board.SCK
mosi = board.MOSI
miso = board.MISO
audio = AudioOut(board.A0)


# The listed mp3files will be played in order
mp3files = ["/sd/song_1.mp3", "/sd/song_2.mp3"]

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
            pass
        decoder.file.close()
print("Completed SD Card + Speaker Test!")
