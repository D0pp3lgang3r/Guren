from lib.fileHandler import FileHandler
from .basics_encode import Hex

class Cloudflare(FileHandler):

	def __init__(self, filename, key=""):
		super().__init__(filename)
		self.data = self.readFile()
		if key is not None:
			self.key = key

	def encode(self):
		return self.key + ''.join([Hex.encodeHex(chr(int(self.key, 16) ^ ord(char)).encode("latin1")).decode("latin1") for char in self.data])

	def decode(self):
		self.key = int(self.data[:2], 16)
		return ''.join([chr(self.key ^ int(self.data[i:i+2], 16)) for i in range(2, len(self.data), 2)])
