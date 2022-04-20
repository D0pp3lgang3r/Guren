from lib.fileHandler import FileHandler

class Cell():
    def __init__(self, num):
        self.num = num
        self.edges = []
        self.visited = False

class DeadFishInterpreter(FileHandler):

    def __init__(self, filename):
        
        super().__init__(filename)
        self.data = self.readFile()
        self.cells = [Cell(i) for i in range(256)]

        for i in range(1, 16):
            self.cells[i].edges.append((self.cells[i-1], 'd'))
            self.cells[i].edges.append((self.cells[i+1], 'i'))
            self.cells[i].edges.append((self.cells[i**2], 's'))

        for i in range(16, 255):
            self.cells[i].edges.append((self.cells[i-1], 'd'))
            self.cells[i].edges.append((self.cells[i+1], 'i'))

        self.cells[0].edges.append((self.cells[0], 'd'))
        self.cells[0].edges.append((self.cells[1], 'i'))
        self.cells[255].edges.append((self.cells[255], 'd'))
        self.cells[255].edges.append((self.cells[0], 'i'))
        self.cells[16].edges.append((self.cells[0], 's'))

        self.tmp_dict = {}

    def encodeCells(self, s, t):
        if (s, t) in self.tmp_dict:
            return self.tmp_dict[(s, t)] + 'o'

        for cell in self.cells:
            cell.visited = False

        queue = [(self.cells[s], '')]
        while queue:
            cell, path = queue.pop(0)
            cell.visited = True

            if cell.num == t:
                self.tmp_dict[(s, t)] = path
                return path + 'o'

            for (ce, c) in cell.edges:
                if not ce.visited:
                    queue.append((ce, path+c))
                    self.tmp_dict[(s, ce.num)] = path+c


    def encode(self):
        buffer = [0] + [ord(c) for c in self.data]
        out = ""
        for i in range(len(self.data)):
            out += self.encodeCells(buffer[i], buffer[i+1])
        return out


    def decode(self):
        decoded = ""
        accumulator = 0
        for instruction in self.data:
            if instruction == 'i':
                accumulator += 1
            elif instruction == 'd':
                accumulator -= 1
            elif instruction == 'o':
                decoded += chr(accumulator)
            elif instruction == 's':
                accumulator *= accumulator

            if accumulator == 256 or accumulator == -1:
                accumulator = 0

        return decoded