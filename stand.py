from operator import indexOf
import random
import aiofiles

def pick():
    icao = input("What ICAO are you controlling?")
    if icao == "egss":
        airline = input("What is the airlines ICAO? I.e RYR?")
        if airline == "RYR":
            standr = random.choice(range(10,150))
            print(standr)
        else:
            if airline == "EZY":
                stand = random.choice(range(10,50))
                print(stand)
    else:
        print("sorry no can do")


pick()