from lib.exceptions import EncodingError
from lib.exceptions import DecodingError
from lib.components import *
from lib.fileHandler import FileHandler

class OldPhone(FileHandler):

	def __init__(self, filename):
		
		self.KEYBOARD = {"2" : "A", "22" : "B", "222" : "C", "3" : "D", "33" : "E", "333" : "F", "4" : "G", "44" : "H", "444" : "I", "0": " ", 
		"5" : "J", "55" : "K", "555" : "L", "6" : "M", "66" : "N", "666" : "O", "7" : "P", "77" : "Q","777" : "R", "7777" : "S" ,"8" : "T", 
		"88" : "U", "888" : "V", "9" : "W", "99" : "X", "999": "Y", "9999" : "Z"}
		
		super().__init__(filename) # Call the FileHandler constructor
		
		self.data = self.readFile()

		self.group_keys = list(self.KEYBOARD.keys())

		self.group_values = list(self.KEYBOARD.values())

	def setPrintableTab(self):
		return tableCode(self.group_values, self.group_keys)

	def encode(self):
		encoded_buffer = ""
		for i, char in enumerate(self.data):
			if char.upper() in self.group_values:
				encoded_buffer += (getKeyFromValue(self.KEYBOARD, char.upper()) + " ")
			else:
				raise EncodingError({"message" : " [!] One of the char is not in the old phone KEYBOARD", "keyboard" : self.setPrintableTab()})
				return

		return encoded_buffer

	def decode(self):
		encoded_buffer = self.data.split(" ")
		decoded_message = ""
		try:
			for number_serie in encoded_buffer:
				decoded_message += (self.KEYBOARD[number_serie] + " ")
		except:
			raise DecodingError({"message" : " [!] One of the number serie is not in the old phone KEYBOARD", "keyboard" : self.setPrintableTab()})
			return
		return decoded_message
