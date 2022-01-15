
from gamefield import GameField


class FileParser:

    DEAD = "."
    ALIVE = "#"

    def __init__(self, filename: str):
        self.filename = filename
        self.data = self._parse()

    def _parse(self):
        field = list()

        with open(self.filename, "r") as f:
            for line in f:
                row = list()
                for char in line:
                    if char == self.DEAD:
                        row.append(False)
                    elif char == self.ALIVE:
                        row.append(True)
                    else:
                        if char == "\n": continue

                        raise ImportError(f"invalid character: {char}")

                field.append(row)
        return field

    def getField(self) -> GameField:
        return GameField(
            len(self.data[0]),
            len(self.data),
            self.data)
