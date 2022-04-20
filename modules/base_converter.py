
from lib.components import *
from lib.fileHandler import FileHandler
from lib.exceptions import EncodingError
from lib.exceptions import DecodingError
import base64

class BaseConverter(FileHandler):

	def __init__(self, filename, base_format=""):
		
		super().__init__(filename)
		
		self.data = self.readFileAsBinary().strip()
		self.base_format = base_format
		self.length = len(self.data)
		
		self.base_types = ["base45", "base62", "base32", "base64", "base16", "base85", "base58"]
		self.base_values = [45, 62, 32, 64, 16, 85, 58]
		if self.base_format != '':
			self.n_base = self.base_values[self.base_types.index(self.base_format)] # Get the base number of the format.

		self.functions_encode = [
			self.base45Encode, self.base62Encode,
			self.base32Encode, self.base64Encode,
			self.base16Encode, self.base85Encode,
			self.base58Encode
			]

		self.functions_decode = [
			self.base45Decode, self.base62Decode,
			self.base32Decode, self.base64Decode,
			self.base16Decode, self.base85Decode,
			self.base58Decode
			]

	# Activation base

	def encode(self):
		for elt in zip(self.functions_encode, self.base_types):
			if self.base_format == elt[1]: # Comparing given format to the base format list elt.
				return elt[0]()
	
	def decode(self):
		for elt in zip(self.functions_decode, self.base_types):
			if self.base_format == elt[1]:
				return elt[0]()

	def bruteForce(self, file_out):
		for elt in zip(self.functions_decode, self.base_types):
			try:
				self.n_base = self.base_values[self.base_types.index(elt[1])]
				file_out.write("%s : %s\n\n" % (elt[1], elt[0]()))
			except:
				file_out.write("%s : Not successfully decoded\n\n" % elt[1])

	# Redefine base

	def base45Encode(self):
		encoded = ""
		length = self.length&~1
		for j in range(0, length, 2):
			val = (self.data[j] << 8) + self.data[j+1]
			idx, val = divmod(val, 45**2)
			idx2, val2 = divmod(val, 45)
			encoded += (BASE45[val2] + BASE45[idx2] + BASE45[idx])
		if self.length & 1:
			idx2, val2 = divmod(self.data[-1], 45)
			encoded += (BASE45[val2] + BASE45[idx2])
		return encoded

	def base45Decode(self):
		return "Not successfully decoded" # To do...

	def baseNEncodeInt(self, integer, alphabet):
		encode = ""
		while integer:
			integer, idx = divmod(integer, self.n_base)
			encode = alphabet[idx:idx+1] + encode
		return encode

	def baseNDecodeInt(self,encoded,alphabet_dict):
		decimal = 0
		decode = "" 
		try:
			for char in encoded:
				decimal = decimal * self.n_base + alphabet_dict[chr(char)] # Use chr bcs we work with bytes
		except KeyError:
			raise EncodingError(f"{FAIL} [!] Seem's one of the char is incorrect, maybe it's not the good base...{RESET}")
		return decimal

	def baseNEncode(self, alphabet):
		return self.baseNEncodeInt(int.from_bytes(self.data, byteorder='big'), alphabet)
	
	def baseNDecode(self, alphabet):
		value = self.baseNDecodeInt(self.data, alphabet)
		decoded = []
		while value > 0:
			value, dec = divmod(value, 256)
			decoded.append(chr(dec))
		return ''.join(reversed(decoded))
	
	def base58Encode(self):
		return self.baseNEncode(BASE58_BITCOIN)

	def base58Decode(self):
		return self.baseNDecode(BASE58_BITCOIN_DICT)

	def base62Encode(self):
		return self.baseNEncode(BASE62)

	def base62Decode(self):
		return self.baseNDecode(BASE62_DICT)

	# Predefine base
	
	def base85Encode(self):
		return base64.b85encode(self.data).decode()

	def base85Decode(self):
		return base64.b85decode(self.data).decode()

	def base64Encode(self):
		return base64.b64encode(self.data).decode()

	def base64Decode(self):
		return base64.b64decode(self.data).decode()

	def base32Encode(self):
		return base64.b32encode(self.data).decode()

	def base32Decode(self):
		return base64.b32decode(self.data).decode()

	def base16Encode(self):
		return base64.b16encode(self.data).decode()
	
	def base16Decode(self):
		return base64.b16decode(self.data).decode()





