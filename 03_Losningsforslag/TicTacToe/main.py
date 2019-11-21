import time
import os
import numpy as np
import pyfiglet


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_brett(brett):
    clear()
    ascii_banner = pyfiglet.figlet_format(" Tic Tac Toe")
    print(ascii_banner)
    print("")
    print(f"       |-----|-----|-----|")
    print(f"       |{brett[0][0]:^5}|{brett[0][1]:^5}|{brett[0][2]:^5}| ")
    print(f"       |-----|-----|-----|")
    print(f"       |{brett[1][0]:^5}|{brett[1][1]:^5}|{brett[1][2]:^5}| ")
    print(f"       |-----|-----|-----|")
    print(f"       |{brett[2][0]:^5}|{brett[2][1]:^5}|{brett[2][2]:^5}| ")
    print(f"       |-----|-----|-----|")
    print("\n\n")


def tre_paa_rad(brett, spiller):
    sum = spiller*3
    return kolonner(brett, sum) or rader(brett, sum) or diagonal1(brett, sum) or diagonal2(brett, sum)


def kolonner(brett, sum):
    return np.any(np.sum(brett, axis=0) == sum)


def rader(brett, sum):
    return np.any(np.sum(brett, axis=1) == sum)


def diagonal1(brett, sum):
    return np.sum(np.diagonal(brett)) == sum


def diagonal2(brett, sum):
    return np.sum(np.diagonal(np.rot90(brett))) == sum


def datatrekk(brett):
    ledig = True
    while ledig:
        x = np.random.randint(0, 3)
        y = np.random.randint(0, 3)
        if np.isnan(brett[x][y]):
            ledig = False
            brett[x][y] = 0
            time.sleep(1)
            return brett


def main():
    brett = np.zeros(shape=(3, 3))*np.nan
    print_brett(brett)

    while True:
        valg = input("velg rute (x,y): ")
        x = int(valg[0])
        y = int(valg[2])
        if np.isnan(brett[x][y]):
            brett[x][y] = 1
            print_brett(brett)
            if tre_paa_rad(brett, 1):
                print("Du vant! Tre på rad!")
                break
            datatrekk(brett)
            print_brett(brett)

            if tre_paa_rad(brett, 0):
                print("Dataen vant! Tre på rad!")
                break

        else:
            print("Velg en ledig rute")


main()
