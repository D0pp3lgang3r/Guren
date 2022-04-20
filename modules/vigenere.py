from lib.fileHandler import FileHandler
import re
ALPHABET_LEN = 26

class Vigenere(FileHandler):

	def __init__(self, filename, key=""):
		super().__init__(filename)
		
		if key is not None:
			self.key = self.filterKey(key).upper()

		self.data = self.readFile()

		self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		
	def encode(self, decipher=False):
		ciphered = ""
		i = 0
		for char in self.data.upper():

			if char in self.alphabet:
				
				offset = ord(self.key[i % len(self.key)]) - ord('A')
				if decipher != False:
					ciphered += chr((ord(char) - ord('A') + (ALPHABET_LEN - offset)) % ALPHABET_LEN + ord('A'))
				else:
					ciphered += chr((ord(char) - ord('A') + offset) % ALPHABET_LEN + ord('A'))

				i += 1

			else:

				ciphered+= char

		if self.data.islower():
			return ciphered.lower()
		return ciphered
	
	def decode(self):
		return self.encode(decipher=True)

	def filterKey(self,text,filter='[^A-Z]'):
		return re.sub(filter,'',text.upper())