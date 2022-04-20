from lib.fileHandler import FileHandler
from lib.exceptions import DecodingError
import requests
ASCII_LEN = 256

class BrainFuckInterpreter(FileHandler):

	def __init__(self, filename):
		super().__init__(filename)
		self.data = self.readFile().strip()
		self.chars_list = ['+', '-', '>', '<', '[', ']', '.', ',']
		self.instruction_pointor = 0
		self.cell_index = 0
		self.cells = [0]
		self.stack_brackets = []
		self.loop_repetition = {}


	def setLoopRep(self):
		for pointor, instruction in enumerate(self.data):
			if instruction == "[":
				self.stack_brackets.append(pointor)
			elif instruction == "]":
				index = self.stack_brackets.pop(0)
				self.loop_repetition[index] = pointor
				self.loop_repetition[pointor] = index

	def encode(self):
		# To upgrade not the best way to encode with brainfuck.
		buffer = [ord(char) for char in self.data]
		encoded = ""
		for elt in buffer:
			for j in range(elt):
				encoded += "+"
			encoded += "."
			for i in range(elt):
				encoded += "-"
		return encoded

	def decode(self):
		self.setLoopRep()
		decoded = ""
		while self.instruction_pointor < len(self.data):
			instruction = self.data[self.instruction_pointor]
			if instruction not in self.chars_list:
				raise DecodingError({"message" : "[*] It seem's it's not brainfuck encoded language..."})
				return

			if instruction == "+":
				self.cells[self.cell_index] += 1
				if self.cells[self.cell_index] == ASCII_LEN:
					self.cells[self.cell_index] = 0
			
			elif instruction == "-":
				self.cells[self.cell_index] -= 1
				if self.cells[self.cell_index] == -1:
					self.cells[self.cell_index] = 255
			
			elif instruction == "<":
				self.cell_index -= 1
			
			elif instruction == ">":
				self.cell_index += 1
				if self.cell_index == len(self.cells):
					self.cells.append(0)

			elif instruction == ".":
				decoded += chr(self.cells[self.cell_index])

			elif instruction == ",": # Assume that this char is not use.
				pass

			elif instruction == "[":
				if not self.cells[self.cell_index]:
					self.instruction_pointor = self.loop_repetition[self.instruction_pointor]
			
			elif instruction == "]":
				if self.cells[self.cell_index]:
					self.instruction_pointor = self.loop_repetition[self.instruction_pointor]


			self.instruction_pointor += 1
		return decoded