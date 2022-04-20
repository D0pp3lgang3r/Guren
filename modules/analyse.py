from lib.components import *
from lib.fileHandler import FileHandler

class Analyzer(FileHandler):

	def __init__(self, filename):

		super().__init__(filename)

		self.hashes_encodings = [
			'base64','base32', 'base45',
			'base58', 'base85', 'base91','base62', 
			'morse code', 'DNA', 'T9-SMS','bacon',
			'bacon-bin', 'brainfuck', 'deadfish',
			'md5', 'md4','md2',
			'sha256', 'sha512', 'sha1',
			'sha384', 'sha224','sha512-224',
			'sha512-256', 'sha3-224', 'sha3-256', 
			'sha3-384', 'sha3-512','Snefru', 'Whirlpool',
			'DCC2'
		]

		self.hashes_encodings_functions = [
			self.isBase64, self.isBase32, self.isBase45,
			self.isBase58, self.isBase85, self.isBase91,
			self.isBase62, self.isMorseCode, self.isDNA,
			self.isOldPhone, self.isBacon, self.isBaconBin,
			self.isBrainFuck, self.isDeadFish, self.isMD5,
			self.isMD4, self.isMD2, self.isSha256,
			self.isSha512, self.isSha1, self.isSha384,
			self.isSha224, self.isSha512_224, self.isSha512_256,
			self.isSha3_224, self.isSha3_256, self.isSha3_384,
			self.isSha3_512, self.isSnefru, self.isWhirlpool,
			self.isDCC2
		]

		self.__data = self.readFile()

		self.type = ""

	def getData(self):
		return self.__data
	
	def isDCC2(self):
		if "$DCC2$" in self.getData():
			return True
		return False
	
	def isABase(self, BASE_CHARS):
		for c in self.getData():
			if c not in BASE_CHARS:
				return False
		return True

	def isBase64(self):
		return self.isABase(BASE64)

	def isBase32(self):
		return self.isABase(BASE32)

	def isBase45(self):
		return self.isABase(BASE45)

	def isBase62(self):
		return self.isABase(BASE62)
	
	def isBase91(self):
		return self.isABase(BASE91)

	def isBase85(self):
		return self.isABase(BASE85)

	def isBase58(self):
		return self.isABase(BASE58_BITCOIN) or self.isABase(BASE58_RIPPLE)

	def isInList(self, list_l):
		for c in self.getData().replace(" ", ""):
			if c not in list_l:
				return False
		return True

	def isMorseCode(self):
		return self.isInList(['.', '-'])

	def isBacon(self):
		return self.isInList(['a', 'b', 'A', 'B'])

	def isBaconBin(self):
		return self.isInList(['0', '1'])

	def isDNA(self):
		return self.isInList(["T", "G", "A", "C", 't', 'g', 'a', 'c'])

	def isOldPhone(self):
		return self.isInList([str(i) for i in range(10)])

	def isDeadFish(self):
		return self.isInList(['i', 's', 'o', 'd', 'I', 'S', 'O', 'D'])

	def isBrainFuck(self):
		return self.isInList(['+', '-', ',', '.', '[', ']', '>', '<'])

	def isHex(self):
		return self.isInList([char for char in "abcdef0123456789"])

	def isMD5(self):
		return self.getHashLen() == 32 and self.isHex()
	
	def isMD4(self):
		return self.isMD5()
	
	def isMD2(self):
		return self.isMD5()

	def isSnefru(self):
		for val in [i*8 for i in range(15)]:
			if self.getHashLen() == val:
				return True
		return False

	def isSha1(self):
		return self.getHashLen() == 40 and self.isHex()

	def isSha224(self):
		return self.getHashLen() == 56 and self.isHex()

	def isSha256(self):
		return self.getHashLen() == 64 and self.isHex()

	def isSha384(self):
		return self.getHashLen() == 96 and self.isHex()

	def isSha512(self):
		return self.getHashLen() == 128 and self.isHex()

	def isSha512_224(self):
		return self.isSha224()

	def isSha512_256(self):
		return self.isSha256()

	def isSha3_224(self):
		return self.isSha224()
	
	def isSha3_256(self):
		return self.isSha256()

	def isSha3_384(self):
		return self.isSha384()

	def isSha3_512(self):
		return self.isSha512()

	def isWhirlpool(self):
		return self.isSha512()

	def getHashLen(self):
		return len(self.getData())
	
	def getByteLen(self):
		return round(len(self.getData()) / 2)
	
	def getBitLen(self):
		return round(self.getByteLen() * 8)

	def getMethods(self):
		methods = []
		for meth in zip(self.hashes_encodings_functions, self.hashes_encodings):
			if meth[0]():
				methods.append(meth[1])
		return methods

	def __str__(self):
		methods = '\n\t'.join(['[?] ' + elt for elt in self.getMethods()])
		if self.isHex():
			content = f"""
 {OKGREEN}[+] Byte length : {self.getByteLen()}{RESET}
 {OKWHITE}[+] Bit length : {self.getBitLen()}{RESET}
 {OKMAGENTA}[+] Hash length : {self.getHashLen()}{RESET}

 {WARNING}[*] We only base theses results on the hash length{RESET}

 {OKGREEN}[???] Suggestion :\n\n\t{RESET}"""
		else:
 			content = f"""
 {WARNING}[!] Seem's it's not a hash, no problem, should be an encoding...{RESET}

 {OKGREEN} [???] Suggestion :\n\n\t{RESET}"""
		return content+methods+'\n'
