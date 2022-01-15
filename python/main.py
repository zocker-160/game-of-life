
import sys
import time
import argparse

from file_parser import FileParser
from gamefield import GameField

def cliParams():
    parser = argparse.ArgumentParser(description="A CLI GOL implementation")

    parser.add_argument("STARTFILE", help="File that defines the first generation")

    parser.add_argument("-n", "--numGens", dest="numGen", default=0,  type=int, help="Number of generations to calculate")
    parser.add_argument("-d", "--delay", dest="delay", default=1, type=int, help="Delay between generations")
    parser.add_argument("-f", "--file", dest="file", action="store_true", help="Write game field to file")

    return parser.parse_args()

def sleep(delay):
    try:
        time.sleep(delay)
    except KeyboardInterrupt:
        print("exitting....")
        sys.exit()

def main(filename: str, numGens=0, writeToFile=False, delay=1):
    parser = FileParser(filename)
    gamefield: GameField = parser.getField()

    print(gamefield.getMatrix())

    if numGens > 0:
        for _ in range(numGens):
            gamefield.calcNextGeneration()

            if writeToFile:
                with open(f"gen_{gamefield.generation}.txt", "w") as f:
                    f.writelines(gamefield.getMatrix(False))
            else:
                print(gamefield.getMatrix())
                sleep(delay)

    else:
        while True:
            gamefield.calcNextGeneration()
            print(gamefield.getMatrix())

            sleep(delay)

if __name__ == "__main__":
    cliArgs = cliParams()

    main(
        filename=cliArgs.STARTFILE,
        numGens=cliArgs.numGen,
        writeToFile=cliArgs.file,
        delay=cliArgs.delay
    )
