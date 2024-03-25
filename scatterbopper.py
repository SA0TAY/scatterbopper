#!/usr/bin/env python3
import pyaudio
from random import choices
from string import ascii_uppercase
from sys import argv, exit
from termcolor import cprint
import cw

if len(argv) != 4:
    print(f"Usage: {argv[0]} koch_level word_length test_length")
    exit(64) # EX_USAGE

koch_sequence = "LFCKRPXYQDBGANZUVWJHSIEOMT"
koch_level = int(argv[1])
word_length = int(argv[2])
test_length = int(argv[3])
test_score = 0

cw = cw.CW()
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=True)

for i in range(test_length):
    test = "".join(choices(koch_sequence[:koch_level], k=word_length))
    print(f"{'?' * word_length} | ", end="")
    stream.write(cw.word(test))
    reply = input()
    cprint(f"\x1b[1A{test} | {reply}", "green" if reply == test else "red")
    if reply == test: test_score += 1

print()
print("Summary:")
print(f"Test parameters: Koch level {koch_level}, word length {word_length}, test length {test_length}")
print(f"Test score: {test_score}/{test_length} ({round(test_score/test_length*100)}%)")
