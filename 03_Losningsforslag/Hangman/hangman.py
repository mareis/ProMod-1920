import ord
import os


tilgeldig_ord = ord.trekk_ord()
losning = tilgeldig_ord[0]

for i in range(len(tilgeldig_ord)-1):
    losning += "_"


def clr():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\n \n')


def print_ord():
    clr()
    for tegn in losning:
        if tegn == "_":
            print("___ ", end="")
        else:
            print(tegn+" ", end="")
    print('')


def


print_ord()
