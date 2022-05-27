#Test if the speaker can produce sound

import time
import array
import math
import board
import digitalio
from audiocore import RawSample
from audioio import AudioOut

tone_volume = 0.1  # Increase this to increase the volume of the tone.
frequency = 440  # Set this to the Hz of the tone you want to generate.
length = 8000 // frequency
sine_wave = array.array("H", [0] * length)
for i in range(length):
    sine_wave[i] = int((1 + math.sin(math.pi * 2 * i / length)) * tone_volume * (2 ** 15 - 1))

audio = AudioOut(board.A0)
sine_wave_sample = RawSample(sine_wave)

print("Now Producing High-Pitched Noise For 5 seconds...")
audio.play(sine_wave_sample, loop=True)
time.sleep(5)
audio.stop()
print("Sound test complete!")
