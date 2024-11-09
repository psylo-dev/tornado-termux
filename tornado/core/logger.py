from datetime import datetime
from importlib.metadata import version
from colorama import Fore as clr, Style

# Time and Date
now = datetime.now()
time_now = now.strftime("%d-%m-%Y %H:%M:%S")

# Colors
cyan = clr.CYAN
green = '\033[92m'  # Hellgrün
yellow = '\033[93m'  # Hellgelb
purple = '\033[35m'
red = clr.RED  # Hellrot
bright = Style.BRIGHT
blue = clr.BLUE
reset = Style.RESET_ALL
grey = '\033[37m'  # Hellgrau
Datetime = ("[" + cyan + time_now + reset + "]")

# Header with updated details (Program name, version, build date)
banner = f"""
{grey}=============================================
  PROGRAM NAME: Tornado Engine
  VERSION: {version('tornado')}
  BUILD DATE: {time_now}
============================================={reset}
"""

# Logging functions
def good(msg):
    print("[" + green + bright + 'SUCCESS' + reset + '] ' + msg)

def goodt(msg):
    print(Datetime + " [" + green + bright + 'SUCCESS' + reset + '] ' + msg)

def error(msg):
    print("[" + red + bright + 'ERR' + reset + '] ', msg)

def errort(msg):
    print(Datetime + " [" + red + bright + 'ERR' + reset + '] ', msg)

def info(msg):
    print("[" + blue + 'INF' + reset + "] " + msg)

def input(msg):
    print("[" + purple + 'INPUT' + reset + "] " + msg)

def infot(msg):
    print(Datetime + " [" + blue + 'INF' + reset + "] " + msg)

def warn(msg):
    print("[" + yellow + 'WRN' + reset + "] " + msg)

def warnt(msg):
    print(Datetime + " [" + yellow + 'WRN' + reset + "] " + msg)

# Display banner
print(banner)
