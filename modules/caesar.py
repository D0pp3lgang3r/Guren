from lib.fileHandler import FileHandler

ASCII_LEN = 256 # Lenght of ascii table

class Caesar(FileHandler):

	def __init__(self, filename, offset=0):
		
		self.offset = offset
		
		super().__init__(filename)

		self.data = self.readFile()
	

	def encode(self):
		
		encoded_buffer = ""
		
		for char in self.data:
			
			if (ord(char) + self.offset > 256):
				
				encoded_buffer += chr(ord(char) + self.offset - 256)
			
			else:
				
				encoded_buffer += chr(ord(char) + self.offset)
		
		return encoded_buffer

	def decode(self):
		
		decoded_buffer = ""
		
		for char in self.data:
			
			if (ord(char) - self.offset < 0):
				
				decoded_buffer += chr(ord(char) - self.offset + 256)
			
			else:
				
				decoded_buffer += chr(ord(char) - self.offset)
		
		return decoded_buffer

	def bruteForce(self, file_out):
		
		for i in range(ASCII_LEN):
			
			self.offset = i
			
			rotated = ("Offset {%s} : {%s}\n" % (self.offset, self.decode()))
			
			file_out.write(rotated)
