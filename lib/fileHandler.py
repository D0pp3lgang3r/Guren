#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

class FileHandler:
	
	def __init__(self, filename):
		self.filename = filename

	def readFile(self, encoding="utf-8"):
		with open(self.filename, "r", encoding=encoding) as file:
			buffer = file.read().strip()
		return buffer

	def readFileAsBinary(self):
		with open(self.filename, "rb") as file:
			buffer = file.read()
		return buffer

	def fileExist(self):
		if Path(self.filename).is_file():
			return True
		return False