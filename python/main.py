
import sys
import time
from file_parser import FileParser
from gamefield import GameField


def main(filename: str):
    parser = FileParser(filename)
    gamefield: GameField = parser.getField()

    gamefield.printMatrix()

    while True:
        gamefield.calcNextGeneration()
        gamefield.printMatrix()
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print("exitting....")
            sys.exit()

if __name__ == "__main__":
    #try:
    main(sys.argv[1])
    #except IndexError:
    #    print("please specify a filename for the starting board")
