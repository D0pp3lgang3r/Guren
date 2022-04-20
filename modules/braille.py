from lib.fileHandler import FileHandler
from lib.exceptions import EncodingError
from lib.exceptions import DecodingError
from lib.components import *

class Braille(FileHandler):

	def __init__(self, filename):

		super().__init__(filename)

		self.BRAILLE_ALPHABET = {
		' ': '⠀', '!': '⠮', '"': '⠐', '#': '⠼', '$': '⠫', '%': '⠩', '&': '⠯', '': '⠄', '(': '⠷', ')': '⠾', 
		'*': '⠡', '+': '⠬', ',': '⠠', '-': '⠤','.': '⠨', '/': '⠌', '0': '⠴', '1': '⠂', '2': '⠆', '3': '⠒', 
		'4': '⠲', '5': '⠢', '6': '⠖', '7': '⠶', '8': '⠦', '9': '⠔', ':': '⠱', ';': '⠰', '<': '⠣', '=': '⠿',
		'>': '⠜', '?': '⠹', '@': '⠈', 'a': '⠁', 'b': '⠃', 'c': '⠉', 'd': '⠙', 'e': '⠑', 'f': '⠋', 'g': '⠛',
		'h': '⠓', 'i': '⠊', 'j': '⠚', 'k': '⠅', 'l': '⠇', 'm': '⠍', 'n': '⠝', 'o': '⠕', 'p': '⠏', 'q': '⠟', 
		'r': '⠗', 's': '⠎', 't': '⠞', 'u': '⠥', 'v': '⠧', 'w': '⠺', 'x': '⠭', 'y': '⠽', 'z': '⠵', '[': '⠪', 
		'\\': '⠳', ']': '⠻', '^': '⠘', '_': '⠸'
		}
		self.group_keys = list(self.BRAILLE_ALPHABET.keys())
		self.group_values = list(self.BRAILLE_ALPHABET.values())
		self.data = self.readFile()

	def setPrintableTab(self):
		return tableCode(self.group_keys, self.group_values)

	def encode(self):
		encoded = ""
		try:
			for char in self.data:
				encoded += self.BRAILLE_ALPHABET[char.lower()]
		except:
			raise EncodingError({"message" : " [!] One of the char has no braille char correspondance", "keyboard" : self.setPrintableTab()})
			return
		return encoded

	def decode(self):
		decoded = ""
		try:
			for braille_char in self.data:
				decoded += getKeyFromValue(self.BRAILLE_ALPHABET, braille_char)
		except:
			raise EncodingError({"message" : " [!] One of the braille char has no char correspondance", "keyboard" : self.setPrintableTab()})
			return
		return decoded