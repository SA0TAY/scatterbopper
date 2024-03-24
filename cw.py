from array import array
from math import pi, sin

class CW:
    cw_symbols = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----',
        '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
        '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.',
        ')': '-.--.-', '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
        '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
        '$': '...-..-', '@': '.--.-.'
}
    def __init__(self, sample_rate=44100, volume=0.5, frequency=600, wpm=20):
        self.sample_rate = sample_rate
        self.volume = volume
        self.frequency = frequency
        # WPM to element duration (PARIS model)
        self.element_duration = 1 / (wpm * 50 / 60)

    def _elements(self, amount, sounding=True):
        sample_count = int(amount * self.element_duration * self.sample_rate)
        samples = [self.volume * sin(2 * pi * i * (self.frequency if sounding else 0) / self.sample_rate) for i in range(0, sample_count)]
        return array("f", samples).tobytes()

    def _dah(self):
        return self._elements(amount=3)

    def _dit(self):
        return self._elements(amount=1)

    def _element_spacing(self):
        return self._elements(amount=1, sounding=False)

    def _symbol_spacing(self):
        return self._elements(amount=3, sounding=False)

    def _word_spacing(self):
        return self._elements(amount=7, sounding=False)

    def symbol(self, symbol):
        data = []
        for e in CW.cw_symbols[symbol]:
            if e == ".":
                data.append(self._dit())
            elif e == "-":
                data.append(self._dah())
        return self._element_spacing().join(data)

    def word(self, word):
        data = []
        for s in word:
            data.append(self.symbol(s))
        return self._symbol_spacing().join(data)

    def sentence(self, sentence):
        data = []
        for w in sentence.split():
            data.append(self.word(w))
        return self._word_spacing().join(data)
