from binascii import hexlify, unhexlify
from lib.fileHandler import FileHandler

class Hex(FileHandler):

	def __init__(self, filename):
		super().__init__(filename)
		self.data = self.readFileAsBinary()

	def encode(self):
		return hexlify(self.data).decode()

	def decode(self):
		return unhexlify(self.data).decoded()

	@staticmethod
	def encodeHex(toEncode):
		return hexlify(toEncode)

	@staticmethod
	def decodeHex(toDecode):
		return unhexlify(toDecode)

class Dec(FileHandler):

	def __init__(self, filename):
		super().__init__(filename)
		self.data = self.readFile()

	def encode(self):
		return "".join([str(ord(char)) + " " for char in self.data])

	def decode(self):
		return "".join([chr(int(char)) for char in self.data.split(" ")])

	@staticmethod
	def encodeDec(toEncode):
		return "".join([str(ord(char)) + " " for char in toEncode])
	
	@staticmethod
	def decodeDec(toDecode):
		return "".join([chr(int(char)) for char in toDecode.split(" ")])

class Bin(FileHandler):

	def __init__(self, filename):
		super().__init__(filename)
		self.data = self.readFile()

	def encode(self):
		return ' '.join(format(ord(char), 'b') for char in self.data)

	def decode(self):
		return ''.join(chr(int(char, 2)) for char in self.data.strip().split(" "))

	@staticmethod
	def encodeBin(toEncode):
		return ' '.join(format(ord(char), 'b') for char in toEncode)

	@staticmethod
	def decodeBin(toDecode):
		return ''.join(chr(int(char, 2)) for char in toDecode.strip().split(" "))
