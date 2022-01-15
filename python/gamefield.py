
import copy

class GameField:

    def __init__(self, width: int, height: int, data: list):
        self.width = width
        self.height = height
        self.data = data
        self.generation = 0

    def calcNextGeneration(self):
        newGen = copy.deepcopy(self.data)

        for x, row in enumerate(self.data):
            for y, col in enumerate(row):
                s = self._getSumLiving(x, y)
                #print(s, x, y, col, self._calcDead(col, self._getSumLiving(x, y)) )
                newGen[x][y] = self._calcDead(col, self._getSumLiving(x, y))
        
        self.data = newGen
        self.generation += 1

    def _calcDead(self, state: bool, value: int) -> bool:
        if state == False:
            if value == 3:
                return True
            else:
                return False
        else:
            if value < 2: return False
            if 2 <= value <= 3: return True
            if value > 3: return False

    def _getSumLiving(self, x, y) -> int:
        neigh = list()
        neigh.append(self._getState(x-1, y-1))
        neigh.append(self._getState(x, y-1))
        neigh.append(self._getState(x+1, y-1))
        neigh.append(self._getState(x-1, y))
        neigh.append(self._getState(x+1, y))
        neigh.append(self._getState(x-1, y+1))
        neigh.append(self._getState(x, y+1))
        neigh.append(self._getState(x+1, y+1))

        return sum(neigh)

    def _getState(self, col, row) -> int:
        if 0 <= row < self.width and 0 <= col < self.height:
            #print("on position", x, y, "is", self.data[x][y])
            return 1 if self.data[col][row] == True else 0
        else:
            return 0

    def printMatrix(self):
        from file_parser import FileParser
        for row in self.data:
            _row = ""
            for char in row:
                if char == True:
                    _row += FileParser.ALIVE
                else:
                    _row += FileParser.DEAD
            print(_row)
        print("---- generation", self.generation)

    def __str__(self):
        output = ""
        for row in self.data:
            output += str(row) + "\n"
        
        output += "---\n"
        output += f"width: {self.width} height: {self.height}"

        return output
