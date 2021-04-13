#coded by ACHIXTAR

#Modules

import requests, json

import sys

from sys import argv

import os

#colours used

red = '\033[31m'

yellow = '\033[1;33m'

lgreen = '\033[92m'

clear = '\033[0m'

bold = '\033[01m'

cyan = '\033[96m'

green = '\033[1;32m'

os.system("clear")

print (red+"""

                       ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
                       ───█▒▒░░░░░░░░░▒▒█───
                       ────█░░█░░░░░█░░█────
                       ─▄▄──█░░░▀█▀░░░█──▄▄─
                       █░░█─▀▄░░░░░░░▄▀─█░░█
                      █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
                      █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
                      █░░║║║╠─║─║─║║║║║╠─░░█
                      █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
                      █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█""")

print ("\n")

IP=input(green+"[+]ENTER THE VICTIM'S IP YOU WANT TO LOCATE : ")

os.system("clear")

print (red+"""┌──────────────────────────────────────────────────┐
│                                                  │
│ ▄▄▄ ▗▄▄▖      ▗▖    ▗▄▖   ▄▄   ▄  ▗▄▄▄▖ ▗▄▖ ▗▄▄▖ │
│ ▀█▀ ▐▛▀▜▖     ▐▌    █▀█  █▀▀▌ ▐█▌ ▝▀█▀▘ █▀█ ▐▛▀▜▌│
│  █  ▐▌ ▐▌     ▐▌   ▐▌ ▐▌▐▛    ▐█▌   █  ▐▌ ▐▌▐▌ ▐▌│
│  █  ▐██▛      ▐▌   ▐▌ ▐▌▐▌    █ █   █  ▐▌ ▐▌▐███ │
│  █  ▐▌    ██▌ ▐▌   ▐▌ ▐▌▐▙    ███   █  ▐▌ ▐▌▐▌▝█▖│
│ ▄█▄ ▐▌        ▐▙▄▄▖ █▄█  █▄▄▌▗█ █▖  █   █▄█ ▐▌ ▐▌│
│ ▀▀▀ ▝▘        ▝▀▀▀▘ ▝▀▘   ▀▀ ▝▘ ▝▘  ▀   ▝▀▘ ▝▘ ▝▀│
│                                                  │
│                                           v 1.0  │
└──────────────────────────────────────────────────┘

coded by ACHIXTAR""")
print ("\n")

os.system("sleep 1")

print (cyan+"         [*]GATHERED INFORMATION BELOW :  \n"+clear)

print ("\n")

ip = IP

api = "http://ip-api.com/json/"

try:

        data = requests.get(api+ip).json()

        sys.stdout.flush()

        a = "√"

        b = "™"

        print (yellow+"IP ADDRESS      >    ", green+data['query'])

        print (yellow+"Country code    >    ", green+data['countryCode'])

        print (yellow+"Country         >    ", green+data['country'])

        print (yellow+"ISP             >    ", green+data['isp'])

        print (yellow+"Organisation    >    ", green+data['org'])

        print (yellow+"City            >    ", green+data['city'])

        print (yellow+"Region code     >    ", green+data['region'])

        print (yellow+"Region          >    ", green+data['regionName'])

        print (yellow+"Longitude       >    ", data['lon'])

        print (yellow+"Latitude        >    ", data['lat'])

        print (yellow+"Time zone       >    ", green+data['timezone'])

        print (yellow+"Zip code        >    ", green+data['zip'])

        print (" "+yellow)

except KeyboardInterrupt:

        print ('Terminating, Bye'+lgreen)

        sys.exit(0)

except requests.exceptions.ConnectionError as e:

        print (red+"[~]"+" check your internet connection!"+clear)

sys.exit(1)
