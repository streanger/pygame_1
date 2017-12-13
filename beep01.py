#!/usr/bin/python3
#just install beep package -> apt install beep

from termcolor import colored
import subprocess

def beep_up(freqStart, freqStop, delay=5):
    beepDelay = "-l" + str(delay)
    for x in range(freqStart, freqStop):
        freq = "-f" + str(x)
        subprocess.call(["beep", beepDelay, freq])

if __name__=="__main__":
    print(colored("close your ears!", "green"))
    beep_up(150, 490, 5)
