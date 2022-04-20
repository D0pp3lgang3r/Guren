from lib.fileHandler import FileHandler
POLYBE_SQUARE_ROW = 5
POLYBE_SQUARE_COL = 5

class Polybe(FileHandler):

	def __init__(self, filename, key=""):
		super().__init__(filename)
		self.data = self.readFile()
		if key is not None and len(key) == 25:
			self.key = key

	def setMatrix(self):
		self.matrix = [[self.key[i+j*POLYBE_SQUARE_ROW] for i in range(POLYBE_SQUARE_ROW)] for j in range(POLYBE_SQUARE_COL)]

	def getMatrixIndex(self, char):
		return ''.join([str(i) + str(j) for i in range(POLYBE_SQUARE_ROW) for j in range(POLYBE_SQUARE_COL) if char == self.matrix[i][j]])
	
	def encode(self):
		self.setMatrix()
		return ''.join([self.getMatrixIndex(char) for char in self.data])

	def decode(self):
		self.setMatrix()
		decoded = ""
		for i in range(0, len(self.data), 2):
			x, y = self.data[i:i+2][0], self.data[i:i+2][1] # get row and col number of the matrix.
			decoded += self.matrix[int(x)][int(y)]
		return decoded
