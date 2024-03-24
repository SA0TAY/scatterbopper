#!/usr/bin/env python3
import cw
import pyaudio

p = pyaudio.PyAudio()
test = cw.CW()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)
stream.write(test.sentence("CQ TEST"))
stream.stop_stream()
stream.close()
p.terminate()
