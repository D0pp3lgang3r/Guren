from lib.fileHandler import FileHandler
from .basics_encode import Hex

class XOR(FileHandler):
	
	def __init__(self, filename):
		super().__init__(filename)
		self.data=self.readFile()

	def encode(self):
		tmp = self.data.split('\n')
		if len(tmp[0]) != len(tmp[1]): # We don't xor if data is not of the same length
			raise EncodingError({"message":"It seems we can't xor these strings because they don't have the same length"})
			return
		first_string, second_string = Hex.decodeHex(tmp[0].strip()), Hex.decodeHex(tmp[1].strip())

		return Hex.encodeHex(''.join([chr(first_string[i]^second_string[i]) for i in range(len(first_string))]).encode()).decode()

	def decode(self):
		return self.encode()