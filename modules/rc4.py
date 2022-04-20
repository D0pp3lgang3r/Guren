
from lib.fileHandler import FileHandler
from .basics_encode import Hex

KEY_LEN = 256

class RC4(FileHandler):

	def __init__(self, filename, key):
		
		super().__init__(filename)

		self.data = self.readFile()
		
		if key is not None:
			self.key = [ord(c) for c in key]

			self.state_array = list(range(KEY_LEN))

			self.key_array = self.genKeyArray()

			self.key_stream = self.genKeyStream()

	def genKeyArray(self):
		return [self.key[counter % len(self.key)] for counter in range(KEY_LEN)]
	
	def genStateArray(self):
		return list(range(KEY_LEN))

	def keySchedule(self):
		j = 0
		for i in range(KEY_LEN):
			j = (j + self.state_array[i] + self.key_array[i]) % KEY_LEN
			self.state_array[i], self.state_array[j] = self.state_array[j], self.state_array[i]

	def genKeyStream(self):
		self.keySchedule()
		i, j = 0, 0
		while True:
			i = (i+1) % KEY_LEN
			j = (j+self.state_array[i]) % KEY_LEN

			self.state_array[i], self.state_array[j] = self.state_array[j], self.state_array[i]
			key = self.state_array[(self.state_array[i] + self.state_array[j]) % KEY_LEN]
			yield key

	def encode(self):
		cipher = b''
		for char in self.data:
			cipher += chr(ord(char) ^ next(self.key_stream)).encode("latin1")
		return Hex.encodeHex(cipher).decode("latin1")

	def decode(self):
		deciphered = ''
		for char in Hex.decodeHex(self.data.encode()):
			deciphered += chr(char ^ next(self.key_stream))
		return deciphered
	
	def getKey(self):
		return self.key

	def getData(self):
		return self.data

	def getCipher(self):
		return self.cipher