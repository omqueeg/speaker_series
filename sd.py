import board
import busio
import sdcardio
import storage

spi = board.SPI()
cs = board.D10     # Use the pin you wired to the breakout CS

sdcard = sdcardio.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")
