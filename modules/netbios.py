from lib.fileHandler import FileHandler

OFFSET_MAX = 256 # You can change it if you want to brute force more offset.

class Netbios(FileHandler):

	def __init__(self, filename, offset):
		
		self.offset = offset
		
		super().__init__(filename)
		
		self.data = self.readFile()

	def decode(self):
		
		decoded = ""
		
		for i in range(1, len(self.data), 2):
			decoded += chr(((ord(self.data[i-1])-self.offset)<<4)+((ord(self.data[i])-self.offset)&0xF))
		
		return decoded


	def encode(self):
		
		encoded = ""
		
		for idx, val in enumerate(self.data):
			encoded += chr((ord(self.data[idx])>>4)+self.offset)+chr((ord(self.data[idx])&0xF)+self.offset)
		
		return encoded

	def bruteForce(self, output):

		for offset in range(OFFSET_MAX):
			self.offset = offset
			try:
				data = "Offset {%s} : {%s}\n" % (self.offset, self.decode())
				output.write(data)
			except:
				pass # In some case, the char can't be decoded as utf-8, so it creates error but we just keep on.