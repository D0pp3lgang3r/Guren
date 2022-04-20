from lib.fileHandler import FileHandler
from lib.components import *

class Bacon(FileHandler):

	def __init__(self, filename):
		super().__init__(filename)

		self.data = self.readFile()

		self.BACON_ALPHABET_CODE = {
			'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa',
        	'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab',
        	'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba',
        	'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb',
        	'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa', 
        	'Z':'bbaab'
        	}
		self.BACON_BIN = {key:value.replace("a", "0").replace("b", "1") for key, value in self.BACON_ALPHABET_CODE.items()}

	def encode(self, dictionnary={}):
		if len(dictionnary) == 0:
			dictionnary = self.BACON_ALPHABET_CODE

		return ' '.join([dictionnary.get(char.upper()) for char in self.data if char.upper() in dictionnary.keys()])
    
	def decode(self, dictionnary={}):
		if len(dictionnary) == 0:
			dictionnary = self.BACON_ALPHABET_CODE

		return ''.join([getKeyFromValue(dictionnary, code) for code in self.data.split(" ") if code in dictionnary.values()])



class BaconBin(Bacon):
	def __init__(self, filename):
		super().__init__(filename)

	def encode(self):
		return super().encode(self.BACON_BIN)

	def decode(self):
		return super().decodeBacon(self.BACON_BIN)
		
