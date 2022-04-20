
from lib.fileHandler import FileHandler
from lib.exceptions import EncodingError
from lib.exceptions import DecodingError
from lib.components import *

class Walross(FileHandler):

	def __init__(self, filename):

		super().__init__(filename)

		self.WALROSS_ALPHABET = {
			"A" : ".-", "B" : "-...", "C" : "-.-.", "D"	: "-..", "E" : ".",
			"F" : "..-.", "G" : "--.", "H" : "....", "I" : "..", "J" : ".---", 
			"K" : "-.-", "L": ".-..", "M" :	"--", "N" : "-.", "O" : "---", 
			"P" : ".--.", "Q" : "--.-", "R"	: ".-.", "S" : "...", "T": "-", 
			"U"	: "..-", "V": "...-" , "W" : ".--", "X" : "-..-", "Y" : "-.--",
			"Z"	: "--..", "À" : ".--.-", "Â" : ".--.-", "Æ" : ".-.-", "Ç" : "-.-..",
			"È"	: ".-..-", "Ë" : "..-..", "É" : "..-..", "Ê" : "-..-.", "Ï" : "-..--", 
			"Ô" : "---.", "Ü" : "..--", "Ù" : "..--","0" : "-----", "1" : ".----", 
			"2" : "..---", "3" : "...--", "4" : "....-", "5" : ".....", "6" : "-....", 
			"7"	: "--...", "8" : "---..", "9" : "----.", "." : ".-.-.-", "," : "--..--", 
			"?" : "..--..", "'" : ".----.",	"!" : "-.-.--", "/" : "-..-.", "(" : "-.--.",
			")" : "-.--.-", "&" : ".-...",	":" : "---...", ";" : "-.-.-.", "=" : "-...-",
			"+" : ".-.-.", "-" : "-....-",	"_"	: "..--.-", "\"": ".-..-.", "$" : "...-..-",
			"@" : ".--.-.", "¿" : "..-.-", 	"¡" : "--...-"
		}

		self.group_keys = list(self.WALROSS_ALPHABET.keys())
		
		self.group_values = list(self.WALROSS_ALPHABET.values())

		self.data = self.readFile()

	def isWalrossValid(self):

		for char in self.data.split(" "):
			if char not in self.group_values:
				return False
		return True
	
	def encode(self):

		encoded = ""
		try:
			for char in self.data:

				encoded += (self.WALROSS_ALPHABET[char.upper()] + " ")
		
			return encoded
		except:
			raise EncodingError({"message" : " [!] The data that you gave us is not valid for morse code, please have a look at this tab :", "keyboard" : self.setPrintableTab()})
			return

	def decode(self):

		if (not self.isWalrossValid()):
			raise EncodingError({"message" : " [!] We can't decode with these char, make sure, you can find the equivalent in this tab :", "keyboard" : self.setPrintableTab()})
			return

		else:
			decoded = ""
			for char in self.data.split(" "):
				decoded += getKeyFromValue(self.WALROSS_ALPHABET, char)
			return decoded

	def setPrintableTab(self):

		return tableCode(self.group_keys, self.group_values)
		

