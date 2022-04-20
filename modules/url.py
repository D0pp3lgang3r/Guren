from lib.fileHandler import FileHandler
from urllib.parse import unquote, quote

class URL(FileHandler):

	def __init__(self, filename):
		super().__init__(filename)
		self.data = self.readFileAsBinary()

	def encode(self):
		return quote(self.data)

	def decode(self):
		return unquote(self.data)