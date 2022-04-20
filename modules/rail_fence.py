from lib.fileHandler import FileHandler
from lib.components import *

class RailFence(FileHandler):

	def __init__(self, filename, key, offset=0):

		super().__init__(filename)
		self.data = self.readFile()
		self.offset = offset
		if key is not None:
			self.key = key
			self.rows = len(self.key)
		self.columns = len(self.data)
	
	def encode(self):
		tab = [[None] * self.columns for _ in range(self.rows)]
		row_index, col_index = 0, 0
		i = 1
		ciphered = ""
		for char in self.data:
			if row_index + i < 0 or row_index + i >= len(tab):
				i *= -1
			tab[row_index][col_index] = char
			row_index += i
			col_index += 1

		return ''.join([char for row in tab for char in row if char != None])

	def decode(self):
		tab = [[""] * self.columns for _ in range(self.rows)]

		index = 0
		i = 1

		for row_index in range(len(tab)):
			row=0
			for col in range(len(tab[row])):
				if row + i < 0 or row + i >= len(tab):
					i *= -1
				if row == row_index:
					tab[row][col] += self.data[index]
					index+=1
				row += i
		
		tab = self.reverseTab(tab)
		return ''.join([char for lign in tab for char in lign if char != ""])

	def reverseTab(self, tab):
		new_tab = [[None] * self.rows for _ in range(self.columns)]

		for i in range(len(tab)):
			for j in range(len(tab[0])):
				new_tab[j][i] = tab[i][j]
		return new_tab