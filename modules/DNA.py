from lib.fileHandler import FileHandler
from lib.exceptions import EncodingError
from lib.exceptions import DecodingError
from lib.components import *

class DNA(FileHandler):

	def __init__(self, filename):
		
		self.sequences = {
			"AAA" : "a", "AAC" : "b", "AAG" : "c", "AAT" : "d", "ACA" : "e", "ACC" : "f", 
			"ACG" : "g", "ACT" : "h", "AGA" : "i", "AGC" : "j", "AGG" : "k", "AGT" : "l", 
			"ATA" : "m", "ATC" : "n", "ATG" : "o", "ATT" : "p", "CAA" : "q", "CAC" : "r", 
			"CAG" : "s", "CAT" : "t", "CCA" : "u", "CCC" : "v", "CCG" : "w", "CCT" : "x", 
			"CGA" : "y", "CGC" : "z", "CGG" : "A", "CGT" : "B", "CTA" : "C", "CTC" : "D", 
			"CTG" : "E", "CTT" : "F", "GAA" : "G", "GAC" : "H", "GAG" : "I", "GAT" : "J", 
			"GCA" : "K", "GCC" : "L", "GCG" : "M", "GCT" : "N", "GGA" : "O", "GGC" : "P", 
			"GGG" : "Q", "GGT" : "R", "GTA" : "S", "GTC" : "T", "GTG" : "U", "GTT" : "V", 
			"TAA" : "W", "TAC" : "X", "TAG" : "Y", "TAT" : "Z", "TCA" : "1", "TCC" : "2", 
			"TCG" : "3", "TCT" : "4", "TGA" : "5", "TGC" : "6", "TGG" : "7", "TGT" : "8", 
			"TTA" : "9", "TTC" : "0", "TTG" : " ", "TTT" : "."
			}
		
		super().__init__(filename)
		
		self.data = self.readFile()

		self.group_keys = list(self.sequences.keys())
		self.group_values = list(self.sequences.values())

	def isValidValues(self):
		for char in self.data:
			if char not in self.sequences.values():
				return False
		return True

	def isValidKeys(self):

		for char in self.data.split(" "):
			if char not in self.sequences.keys():
				return False
		return True

	def encode(self):
		if not self.isValidValues():
			raise EncodingError({"message" : " [!] One of the char has no DNA sequence correspondance", "keyboard" : self.setPrintableTab()})
			return

		encoded = ""
		for char in self.data:
			encoded += getKeyFromValue(self.sequences, char) + " "
		
		return encoded

	def decode(self):
		decoded = ""
		if not self.isValidKeys():
			raise EncodingError({
				"message" : " [!] This DNA sequence can't be decoded, perhaps one of the char does not correspond to a piece of sequence...", 
				"keyboard" : self.setPrintableTab()
				})
			return
		for char in self.data.split(" "):
			decoded += self.sequences.get(char)
		return decoded

	def setPrintableTab(self):
		
		return tableCode(self.group_keys, self.group_values)
