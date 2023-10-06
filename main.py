#!/usr/bin/python
# -*- coding: UTF-8 -*-


# Import various Python libraries and modules

import os                 # Operating system operations
import subprocess         # Subprocess management
import sys                # System-specific parameters and functions
import smtplib            # Simple Mail Transfer Protocol (SMTP) for sending emails
import urllib             # URL handling library
import tqdm               # Progress bar library
import random             # Random number generation
import json               # JSON (JavaScript Object Notation) handling
import threading          # Threading support for multi-threaded execution
import re                 # Regular expressions for pattern matching
import requests           # HTTP requests library
import platform           # System information retrieval
import shutil             # High-level file operations
import time               # Time-related operations
import pip                # Package installation and management

# Import specific functions and classes from Flask web framework
from time import sleep
from flask import Flask, request, render_template, jsonify

# Import the 'zipfile' module conditionally based on Python version
if sys.version_info >= (3, 6): import zipfile
else: import zipfile36 as zipfile


Current_Version = "1.0.9"


def color():
    global black,reset,blue,red,yellow,green,cyan,white,magenta,lightblack,lightblue,lightcyan,lightgreen,lightmagenta,lightred,lightwhite,lightyellow,bold
    if (subprocess.getoutput("printf \"color\"") == "color") :
        bold="\033[01m"
        black = '\033[30m'
        reset = '\033[39m'
        blue = '\033[34m'
        red = '\033[31m'
        if (os.name == "nt"): yellow = '\033[33m'
        else: yellow = '\033[92m'
        green = '\033[32m'
        cyan = '\033[36m'
        white = '\033[37m'
        magenta = '\033[35m'
        lightblack = '\033[90m'
        lightblue = '\033[94m'
        lightcyan = '\033[96m'
        lightmagenta = '\033[95m'
        lightred = '\033[91m'
        lightwhite = '\033[97m'
        lightyellow = '\033[93m'
    else:
        bold, black, reset, blue, red, yellow, green, cyan, white, magenta, lightblack, lightblue, lightcyan, lightgreen, lightmagenta, lightred, lightwhite, lightyellow = "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
color()

def prime_num(num):
    if num <= 1: return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: return False
    return True

def space(num, a= " "):
    return "".join([a for i in range(num)])

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
    global echo_top, echo, echo_bottom, min_area, max_area, clear, execute
    echo_top = lambda : center(box(red+"══", red+"╔", red+"╗", total_area(), "═"))
    echo = lambda text, right_char=red+"║", left_char=red+"║"+reset, raw=" ": center(box(text, right_char, left_char, total_area(), raw))
    echo_bottom = lambda : center(box(red+"══", red+"╚", red+"╝", total_area(), "═"))
    min_area = 50
    max_area = 80
    clear = lambda : os.system("cls") if (os.name == "nt") else os.system("clear")
    execute = lambda: "3" if (platform.system().lower() == "darwin") else ""
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
                subprocess.getoutput("termux-sms-send")
                subprocess.getoutput("termux-sms-list")
                return True
    else: return False

def internet():
    try: requests.get("https://google.com/"); return True  # send a GET request to https://google.com/
    except: return False

def check_version():
    version = requests.get("https://raw.githubusercontent.com/GreyTechno/sms_forwarder/main/.info").json()["version"]
    if (Current_Version != version):
        TRIAL, UPDATE= True, True
        try:
            fileData = json.loads(open(pip.__path__[0]+"\\SHFgIGHAQuHSHIHD.zip", "r").read())
            if (fileData.get("usageleft") == 0): TRIAL = False
            else:
                with open(pip.__path__[0]+"\\SHFgIGHAQuHSHIHD.zip", "w") as file: json.dump({"usageleft": int(fileData.get("usageleft")) - 1}, file)
        except: 
            with open(pip.__path__[0]+"\\SHFgIGHAQuHSHIHD.zip", "w") as file: file.write('{"usageleft": 2}')
        if (TRIAL):
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
            else: UPDATE = False
        else: UPDATE = True
        if (UPDATE): update()

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

def on_termux():
    banner()
    print()
    echo_top()
    echo(f"{reset}{bold}{white}Comming Soon...{reset}")
    echo_bottom()
    print()
    echo_top()
    echo(f"{reset}{bold}{lightcyan}For Back Press Enter{reset}")
    echo("══", red+"╠", "╝", "═")
    echo("  ", red+"║", " ")
    center_input(f"╚════► {yellow}")
    main_menu()

def on_telegram():
    banner()
    print()
    echo_top()
    echo(f"{reset}{bold}{white}Comming Soon...{reset}")
    echo_bottom()
    print()
    echo_top()
    echo(f"{reset}{bold}{lightcyan}For Back Press Enter{reset}")
    echo("══", red+"╠", "╝", "═")
    echo("  ", red+"║", " ")
    center_input(f"╚════► {yellow}")
    main_menu()

total_capture = 0
def localhost(password, port, jsonfile, loginfile, inboxfile, host="127.0.0.1"):
    app = Flask("sms_forwarder")
    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    set_password = password
    @app.route('/', methods=['GET', 'POST'])
    def index():
        global total_capture
        if (request.method == 'POST'):
            password = request.form['password']
            if (password == set_password):
                while True:
                    log_events = json.loads(open(jsonfile, "r").read())
                    len_data = len(log_events)
                    if total_capture > 99:
                        total_capture = 0
                        with open(jsonfile, "w") as file:
                            file.write("[]")
                        Inner_html = '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=1024, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">
        <title>Sms Forwarder - Inbox</title>
        <style>
            /* Reset some default styles */
            body, ul {
                margin: 0;
                padding: 0;
                list-style: none;
            }

            /* Global styles */
            body {
                font-family: Arial, sans-serif;
            }

            /* Header styles */
            header {
                background-color: #2d89ef;
                color: white;
                padding: 20px;
                text-align: center;
            }

            h1 {
                margin: 0;
                font-size: 24px;
            }

            /* Navigation styles */
            nav ul {
                background-color: #f0f0f0;
                text-align: center;
                padding: 10px;
            }

            nav li {
                display: inline;
                margin: 0 10px;
            }

            nav .reload-button {
                display: inline-block;
                background-color: #5e6e17fb;
                color: white;
                padding: 10px 100px;
                border-radius: 5px;
                text-decoration: none;
                cursor: pointer;
            }

            /* Email list styles */
            .email-list {
                padding: 20px;
            }

            .email-item {
                background-color: #fff;
                border: 1px solid #ddd;
                margin: 10px 0;
                padding: 15px;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                cursor: pointer;
                transition: background-color 0.3s, transform 0.3s;
            }

            .email-item:hover {
                background-color: #f5f5f5;
                transform: translateY(-2px);
            }

            .email-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 10px;
            }

            .sender {
                font-weight: bold;
            }

            .subject {
                flex-grow: 1;
                margin-left: 20px;
                overflow: hidden;
                white-space: nowrap;
                text-overflow: ellipsis;
            }

            .date {
                font-size: 12px;
                color: #888;
            }

            .email-details {
                display: none;
                background-color: #f0f0f0;
                border: 1px solid #ddd;
                padding: 10px;
                margin-top: 10px;
                border-radius: 5px;
            }

            .email-item.expanded .email-details {
                display: block;
            }

            a {
                text-decoration: none;
                color: #2d89ef;
                font-weight: bold;
            }
            /* Define the animation */
            @keyframes pulse {
            0% {
                transform: scale(1);
            }
            50% {
                transform: scale(0.5);
            }
            100% {
                transform: scale(0.1);
            }
            }

            /* Apply the animation class */
            .animate {
            animation: pulse 1s infinite;
            }
        </style>
    </head>
    <body>
        <header>
            <h1 style="font-family: algerian; font-size: 50px; color: black;">SMS FORWARDER</h1>
        </header>
        <nav>
            <ul>
                <li>
                    <a href="#" class="reload-button" id="reloadInbox">Refresh</a>
                </li>
            </ul>
        </nav>
        <main>
            <ul>
                <!-- hgcs_1 -->
                <!-- hgcs_2 -->
                <!-- hgcs_3 -->
                <!-- hgcs_4 -->
                <!-- hgcs_5 -->
                <!-- hgcs_6 -->
                <!-- hgcs_7 -->
                <!-- hgcs_8 -->
                <!-- hgcs_9 -->
                <!-- hgcs_10 -->
                <!-- hgcs_11 -->
                <!-- hgcs_12 -->
                <!-- hgcs_13 -->
                <!-- hgcs_14 -->
                <!-- hgcs_15 -->
                <!-- hgcs_16 -->
                <!-- hgcs_17 -->
                <!-- hgcs_18 -->
                <!-- hgcs_19 -->
                <!-- hgcs_20 -->
                <!-- hgcs_21 -->
                <!-- hgcs_22 -->
                <!-- hgcs_23 -->
                <!-- hgcs_24 -->
                <!-- hgcs_25 -->
                <!-- hgcs_26 -->
                <!-- hgcs_27 -->
                <!-- hgcs_28 -->
                <!-- hgcs_29 -->
                <!-- hgcs_30 -->
                <!-- hgcs_31 -->
                <!-- hgcs_32 -->
                <!-- hgcs_33 -->
                <!-- hgcs_34 -->
                <!-- hgcs_35 -->
                <!-- hgcs_36 -->
                <!-- hgcs_37 -->
                <!-- hgcs_38 -->
                <!-- hgcs_39 -->
                <!-- hgcs_40 -->
                <!-- hgcs_41 -->
                <!-- hgcs_42 -->
                <!-- hgcs_43 -->
                <!-- hgcs_44 -->
                <!-- hgcs_45 -->
                <!-- hgcs_46 -->
                <!-- hgcs_47 -->
                <!-- hgcs_48 -->
                <!-- hgcs_49 -->
                <!-- hgcs_50 -->
                <!-- hgcs_51 -->
                <!-- hgcs_52 -->
                <!-- hgcs_53 -->
                <!-- hgcs_54 -->
                <!-- hgcs_55 -->
                <!-- hgcs_56 -->
                <!-- hgcs_57 -->
                <!-- hgcs_58 -->
                <!-- hgcs_59 -->
                <!-- hgcs_60 -->
                <!-- hgcs_61 -->
                <!-- hgcs_62 -->
                <!-- hgcs_63 -->
                <!-- hgcs_64 -->
                <!-- hgcs_65 -->
                <!-- hgcs_66 -->
                <!-- hgcs_67 -->
                <!-- hgcs_68 -->
                <!-- hgcs_69 -->
                <!-- hgcs_70 -->
                <!-- hgcs_71 -->
                <!-- hgcs_72 -->
                <!-- hgcs_73 -->
                <!-- hgcs_74 -->
                <!-- hgcs_75 -->
                <!-- hgcs_76 -->
                <!-- hgcs_77 -->
                <!-- hgcs_78 -->
                <!-- hgcs_79 -->
                <!-- hgcs_80 -->
                <!-- hgcs_81 -->
                <!-- hgcs_82 -->
                <!-- hgcs_83 -->
                <!-- hgcs_84 -->
                <!-- hgcs_85 -->
                <!-- hgcs_86 -->
                <!-- hgcs_87 -->
                <!-- hgcs_88 -->
                <!-- hgcs_89 -->
                <!-- hgcs_90 -->
                <!-- hgcs_91 -->
                <!-- hgcs_92 -->
                <!-- hgcs_93 -->
                <!-- hgcs_94 -->
                <!-- hgcs_95 -->
                <!-- hgcs_96 -->
                <!-- hgcs_97 -->
                <!-- hgcs_98 -->
                <!-- hgcs_99 -->
                <!-- hgcs_100 -->
            </ul>
        </main>
        <script>
            // JavaScript to toggle email details visibility
            const emailItems = document.querySelectorAll('.email-item');
            
            emailItems.forEach(emailItem => {
                emailItem.addEventListener('click', () => {
                    emailItem.classList.toggle('expanded');
                });
            });
        
            // JavaScript to reload the inbox
            const reloadButton = document.getElementById('reloadInbox');
            reloadButton.addEventListener('click', () => {
                reloadButton.classList.add('animate');
                setTimeout(function() {
                    reloadButton.classList.remove('animate');
                }, 1000);
                location.reload();
            });
        
            // JavaScript to reload the inbox every 10 seconds
            const reloadEvery7Seconds = () => {
                location.reload();
            };
        
            // Call the reload function initially and then every 10 seconds
            setTimeout(reloadEvery7Seconds, 7000); // Call it initially
        </script>
        
    </body>
    </html>
    '''
                        with open(f"templates/{inboxfile}", "w") as file:
                                    file.write(Inner_html)
                    if (len_data != total_capture):
                            try:
                                unsended_info  = int(str(len_data - total_capture).replace("-", ""))
                                unsend_message = log_events[-unsended_info:]
                                for unsended_count in range(unsended_info):
                                    total_capture += 1

                                    name = unsend_message[unsended_count].get("sender")
                                    number = unsend_message[unsended_count].get("number")
                                    date = unsend_message[unsended_count].get("date")
                                    message = unsend_message[unsended_count].get("message")

                                    Html = open(f"templates/{inboxfile}").read()
                                    Items = f'''
                    <li class="email-item">
                        <div class="email-header">
                            <span class="sender">{name}</span>
                            <span class="subject">{number}</span>
                            <span class="date">{date}</span>
                        </div>
                        <div class="email-details">
                            <p>{message}</p>
                        </div>
                    </li>'''

                                    with open(f"templates/{inboxfile}", "w") as file:
                                        file.write(Html.replace(f"<!-- hgcs_{total_capture} -->", Items))
                            except IndexError: pass
                    else:
                        return render_template(inboxfile)
            else: return render_template(loginfile)
        return render_template(loginfile)
    app.run(debug=True, host=host, port=port)
    
    with open(jsonfile, "w") as file:
        file.write("[]")
    Inner_html = '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=1024, initial-scale=1.0, maximum-scale=1.0, user-scalable=0">
        <title>Sms Forwarder - Inbox</title>
        <style>
            /* Reset some default styles */
            body, ul {
                margin: 0;
                padding: 0;
                list-style: none;
            }

            /* Global styles */
            body {
                font-family: Arial, sans-serif;
            }

            /* Header styles */
            header {
                background-color: #2d89ef;
                color: white;
                padding: 20px;
                text-align: center;
            }

            h1 {
                margin: 0;
                font-size: 24px;
            }

            /* Navigation styles */
            nav ul {
                background-color: #f0f0f0;
                text-align: center;
                padding: 10px;
            }

            nav li {
                display: inline;
                margin: 0 10px;
            }

            nav .reload-button {
                display: inline-block;
                background-color: #5e6e17fb;
                color: white;
                padding: 10px 100px;
                border-radius: 5px;
                text-decoration: none;
                cursor: pointer;
            }

            /* Email list styles */
            .email-list {
                padding: 20px;
            }

            .email-item {
                background-color: #fff;
                border: 1px solid #ddd;
                margin: 10px 0;
                padding: 15px;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                cursor: pointer;
                transition: background-color 0.3s, transform 0.3s;
            }

            .email-item:hover {
                background-color: #f5f5f5;
                transform: translateY(-2px);
            }

            .email-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 10px;
            }

            .sender {
                font-weight: bold;
            }

            .subject {
                flex-grow: 1;
                margin-left: 20px;
                overflow: hidden;
                white-space: nowrap;
                text-overflow: ellipsis;
            }

            .date {
                font-size: 12px;
                color: #888;
            }

            .email-details {
                display: none;
                background-color: #f0f0f0;
                border: 1px solid #ddd;
                padding: 10px;
                margin-top: 10px;
                border-radius: 5px;
            }

            .email-item.expanded .email-details {
                display: block;
            }

            a {
                text-decoration: none;
                color: #2d89ef;
                font-weight: bold;
            }
            /* Define the animation */
            @keyframes pulse {
            0% {
                transform: scale(1);
            }
            50% {
                transform: scale(0.5);
            }
            100% {
                transform: scale(0.1);
            }
            }

            /* Apply the animation class */
            .animate {
            animation: pulse 1s infinite;
            }
        </style>
    </head>
    <body>
        <header>
            <h1 style="font-family: algerian; font-size: 50px; color: black;">SMS FORWARDER</h1>
        </header>
        <nav>
            <ul>
                <li>
                    <a href="#" class="reload-button" id="reloadInbox">Refresh</a>
                </li>
            </ul>
        </nav>
        <main>
            <ul>
                <!-- hgcs_1 -->
                <!-- hgcs_2 -->
                <!-- hgcs_3 -->
                <!-- hgcs_4 -->
                <!-- hgcs_5 -->
                <!-- hgcs_6 -->
                <!-- hgcs_7 -->
                <!-- hgcs_8 -->
                <!-- hgcs_9 -->
                <!-- hgcs_10 -->
                <!-- hgcs_11 -->
                <!-- hgcs_12 -->
                <!-- hgcs_13 -->
                <!-- hgcs_14 -->
                <!-- hgcs_15 -->
                <!-- hgcs_16 -->
                <!-- hgcs_17 -->
                <!-- hgcs_18 -->
                <!-- hgcs_19 -->
                <!-- hgcs_20 -->
                <!-- hgcs_21 -->
                <!-- hgcs_22 -->
                <!-- hgcs_23 -->
                <!-- hgcs_24 -->
                <!-- hgcs_25 -->
                <!-- hgcs_26 -->
                <!-- hgcs_27 -->
                <!-- hgcs_28 -->
                <!-- hgcs_29 -->
                <!-- hgcs_30 -->
                <!-- hgcs_31 -->
                <!-- hgcs_32 -->
                <!-- hgcs_33 -->
                <!-- hgcs_34 -->
                <!-- hgcs_35 -->
                <!-- hgcs_36 -->
                <!-- hgcs_37 -->
                <!-- hgcs_38 -->
                <!-- hgcs_39 -->
                <!-- hgcs_40 -->
                <!-- hgcs_41 -->
                <!-- hgcs_42 -->
                <!-- hgcs_43 -->
                <!-- hgcs_44 -->
                <!-- hgcs_45 -->
                <!-- hgcs_46 -->
                <!-- hgcs_47 -->
                <!-- hgcs_48 -->
                <!-- hgcs_49 -->
                <!-- hgcs_50 -->
                <!-- hgcs_51 -->
                <!-- hgcs_52 -->
                <!-- hgcs_53 -->
                <!-- hgcs_54 -->
                <!-- hgcs_55 -->
                <!-- hgcs_56 -->
                <!-- hgcs_57 -->
                <!-- hgcs_58 -->
                <!-- hgcs_59 -->
                <!-- hgcs_60 -->
                <!-- hgcs_61 -->
                <!-- hgcs_62 -->
                <!-- hgcs_63 -->
                <!-- hgcs_64 -->
                <!-- hgcs_65 -->
                <!-- hgcs_66 -->
                <!-- hgcs_67 -->
                <!-- hgcs_68 -->
                <!-- hgcs_69 -->
                <!-- hgcs_70 -->
                <!-- hgcs_71 -->
                <!-- hgcs_72 -->
                <!-- hgcs_73 -->
                <!-- hgcs_74 -->
                <!-- hgcs_75 -->
                <!-- hgcs_76 -->
                <!-- hgcs_77 -->
                <!-- hgcs_78 -->
                <!-- hgcs_79 -->
                <!-- hgcs_80 -->
                <!-- hgcs_81 -->
                <!-- hgcs_82 -->
                <!-- hgcs_83 -->
                <!-- hgcs_84 -->
                <!-- hgcs_85 -->
                <!-- hgcs_86 -->
                <!-- hgcs_87 -->
                <!-- hgcs_88 -->
                <!-- hgcs_89 -->
                <!-- hgcs_90 -->
                <!-- hgcs_91 -->
                <!-- hgcs_92 -->
                <!-- hgcs_93 -->
                <!-- hgcs_94 -->
                <!-- hgcs_95 -->
                <!-- hgcs_96 -->
                <!-- hgcs_97 -->
                <!-- hgcs_98 -->
                <!-- hgcs_99 -->
                <!-- hgcs_100 -->
            </ul>
        </main>
        <script>
            // JavaScript to toggle email details visibility
            const emailItems = document.querySelectorAll('.email-item');
            
            emailItems.forEach(emailItem => {
                emailItem.addEventListener('click', () => {
                    emailItem.classList.toggle('expanded');
                });
            });
        
            // JavaScript to reload the inbox
            const reloadButton = document.getElementById('reloadInbox');
            reloadButton.addEventListener('click', () => {
                reloadButton.classList.add('animate');
                setTimeout(function() {
                    reloadButton.classList.remove('animate');
                }, 1000);
                location.reload();
            });
        
            // JavaScript to reload the inbox every 10 seconds
            const reloadEvery7Seconds = () => {
                location.reload();
            };
        
            // Call the reload function initially and then every 10 seconds
            setTimeout(reloadEvery7Seconds, 7000); // Call it initially
        </script>
        
    </body>
    </html>
    '''
    with open(f"templates/{inboxfile}", "w") as file:
            file.write(Inner_html)

def on_webpage():
    def sms_read(jsonfile):
        Identity = ""
        while True:
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
        print()
        echo_top()
        echo(f"{reset}{bold}{white}Cloudflared Not Found..{reset}")
        echo_bottom()
        print()
        print()
        echo_top()
        echo(f"{reset}{bold}{yellow}For Install Press Enter{reset}")
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
        if len(str(user_port)) == 4: break
        else:
            echo_top()
            echo(f"{reset}{bold}{white}Enter 4 Digit Port Number{reset}")
            echo_bottom()
            sleep(2)

    
    jsonfile     = "templates/data.json"
    loginfile    = "sms_forwarder-authentication.html"
    inboxfile    = "sms_forwarder-inbox.html"
    host         = "127.0.0.1"

    with open(jsonfile, "w") as file:
        file.write("[]")

    localserver = localhost(user_password, user_port, jsonfile, loginfile, inboxfile, host), sleep(2)
    _localserver = threading.Thread(target=localserver)
    try: _localserver.start()
    except: pass

    banner()
    while _localserver.is_alive():
        for _anim in ['⠋  Starting Python Server...', '⠙  Starting Python Server...', '⠹  starting Python Server...', '⠸  STarting Python Server...', '⠼  StArting Python Server...', '⠴  StaRting Python Server...', '⠦  StarTing Python Server...', '⠧  StartIng Python Server...', '⠇  StartiNg Python Server...', '⠏  StartinG Python Server...', '⠋  Starting Python Server...', '⠙  Starting python Server...', '⠹  Starting PYthon Server...', '⠸  Starting PyThon Server...', '⠼  Starting PytHon Server...', '⠴  Starting PythOn Server...', '⠦  Starting PythoN Server...', '⠧  Starting Python Server...', '⠇  Starting Python server...', '⠏  Starting Python SErver...', '⠋  Starting Python SeRver...', '⠙  Starting Python SerVer...', '⠹  Starting Python ServEr...', '⠸  Starting Python ServeR...', '⠼  Starting Python Server...']:
            bar  = _anim.split(" ")[0]
            text = " ".join(_anim.split(" ")[2:6])
            sys.stdout.write(f"\r{center(f'{yellow}{bar}  {white}{text}', False)}")
            sys.stdout.flush()
            sleep(0.05)
    

    banner()
    try: os.remove("cloudflared.log")
    except: pass

    start_cloudflared = lambda host, port : os.system(f"./cloudflared tunnel -url {host}:{port} --logfile cloudflared.log > /dev/null 2>&1"), sleep(10)
    _start_cloudflared = threading.Thread(target=start_cloudflared)
    try: _start_cloudflared.start()
    except: pass

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
            _start_cloudflared.join()
            _localserver.join()
        except: pass
        main_menu()
    else:
        banner()
        print()
        echo_top()
        echo(f"{reset}{bold}{red}ERROR...!!!{reset}")
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
        on_webpage()

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
    else:
        banner()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
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
            echo(f"{bold}{white}Total Messages Received {magenta}[ {cyan}{total_recived}{magenta}]{reset}")
            echo("══", red+"╠", "╣", "═")
            echo(f"{bold}{white}Total Messages Forward {magenta}[ {cyan}{total_send}{magenta}]{reset}")
            echo("══", red+"╠", "╣", "═")
            echo(f"{bold}{white}Total Messages Failed {magenta}[ {cyan}{total_failed}{magenta}]{reset}")
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
            echo(f"{bold}{white}Total Messages Received {magenta}[ {cyan}{total_recived}{magenta}]{reset}")
            echo("══", red+"╠", "╣", "═")
            echo(f"{bold}{white}Total Messages Forward {magenta}[ {cyan}{total_send}{magenta}]{reset}")
            echo("══", red+"╠", "╣", "═")
            echo(f"{bold}{white}Total Messages Failed {magenta}[ {cyan}{total_failed}{magenta}]{reset}")
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

def update():
    banner()
    version = requests.get("https://raw.githubusercontent.com/GreyTechno/sms_forwarder/main/.info").json()["version"]
    main_work = True
    if (Current_Version == version):
        echo_top()
        echo(f"{bold}{white}Already you are using latest version {blue}'{yellow}{Current_Version}{blue}'{reset}")
        echo_bottom()
        echo_top()
        echo(f"{bold}{white}Do you want's continue {red}({white}Y{red}/{white}n{red}){reset}")
        echo("══", red+"╠", "╝", "═")
        echo("  ", red+"║", " ")
        _update = center_input(f"╚════► {yellow}").lower()
        if (_update == "y") or (_update == "yes"): main_work = True
        else: main_work = False
    if (main_work):
        current_path = os.getcwd()
        if not "TWK5XME9V704" in current_path.split("\\"):
            os.chdir("..")
            shutil.rmtree("sms_forwarder")
            repository_list = requests.get("https://raw.githubusercontent.com/GreyTechno/gtci/main/programs/.programs").json()
            repository_name = "sms_forwarder"
            url = repository_list[repository_name]['zipurl'] + "?raw=true"
            dependencies = repository_list[repository_name]['dependencies']
            rname = "".join(random.sample("abcdefghijklmnopqrstuvwxyz", 7))
            zipname = url.split("/")[4] +"$"+ url.split("/")[-1].split(".")[0]
            toolname = zipname.split("$")[0]
            block_size = 1024
            response = requests.get(url, stream=True)
            E = True
            for i in range(15):
                try: E, total_size = True, int(urllib.request.urlopen(urllib.request.Request(url, method='HEAD')).headers['Content-Length']) ; break
                except TypeError: E = False
            if not (E):
                banner()
                print()
                echo_top()
                echo(f"{bold}{white}Something went's wrong try again later.{reset}")
                echo_bottom()
                with open(pip.__path__[0]+"\\SHFgIGHAQuHSHIHD.zip", "w") as file: file.write('{"usageleft": 2}')
                sleep(2)
            with open(f"{rname}.zip", 'wb') as f:
                for data in tqdm(iterable = response.iter_content(chunk_size = block_size),total = total_size/block_size, unit = ' KB', desc=f"{bold}{magenta}[{yellow}+{magenta}] {white}Downloading "):
                    f.write(data)
            with zipfile.ZipFile(f"{rname}.zip", "r") as zip: zip.extractall(f"{rname}")
            os.remove(f"{rname}.zip")
            shutil.copytree(f"{os.getcwd()}\\{rname}\\{zipname.replace('$', '-')}", toolname)
            shutil.rmtree(rname)
            Dependencies = lambda: [subprocess.getoutput(f"pip{execute()} install {i}") for i in dependencies]
            DEPENDENCIES = threading.Thread(target=Dependencies)
            DEPENDENCIES.start()
            while DEPENDENCIES.is_alive():
                animation = [f'{reset}{bold}{yellow}⠋  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠙  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠹  {white}installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠸  {white}INstalling Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠼  {white}InStalling Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠴  {white}InsTalling Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠦  {white}InstAlling Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠧  {white}InstaLling Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠇  {white}InstalLing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠏  {white}InstallIng Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠋  {white}InstalliNg Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠙  {white}InstallinG Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠹  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠸  {white}Installing building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠼  {white}Installing BUilding Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠴  {white}Installing BuIlding Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠦  {white}Installing BuiLding Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠧  {white}Installing BuilDing Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠇  {white}Installing BuildIng Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠏  {white}Installing BuildiNg Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠋  {white}Installing BuildinG Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠙  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠹  {white}Installing Building dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠸  {white}Installing Building DEpendencies{blue}...{reset}', f'{reset}{bold}{yellow}⠼  {white}Installing Building DePendencies{blue}...{reset}', f'{reset}{bold}{yellow}⠴  {white}Installing Building DepEndencies{blue}...{reset}', f'{reset}{bold}{yellow}⠦  {white}Installing Building DepeNdencies{blue}...{reset}', f'{reset}{bold}{yellow}⠧  {white}Installing Building DepenDencies{blue}...{reset}', f'{reset}{bold}{yellow}⠇  {white}Installing Building DependEncies{blue}...{reset}', f'{reset}{bold}{yellow}⠏  {white}Installing Building DependeNcies{blue}...{reset}', f'{reset}{bold}{yellow}⠋  {white}Installing Building DependenCies{blue}...{reset}', f'{reset}{bold}{yellow}⠙  {white}Installing Building DependencIes{blue}...{reset}', f'{reset}{bold}{yellow}⠹  {white}Installing Building DependenciEs{blue}...{reset}', f'{reset}{bold}{yellow}⠸  {white}Installing Building DependencieS{blue}...{reset}', f'{reset}{bold}{yellow}⠼  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠴  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠦  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠧  {white}Installing Building Dependencies{blue}...{reset}']
                for anim in animation:
                    sys.stdout.write(center(anim, False)+'\r')
                    sleep(0.05)
            DEPENDENCIES.join()
            with open(pip.__path__[0]+"\\SHFgIGHAQuHSHIHD.zip", "w") as file: file.write('{"usageleft": 2}')
            banner()
            echo_top()
            echo(f"{reset}{bold}{white}Update sucessfully completed{reset}")
            echo(f"{reset}{bold}{white}for start now just type{reset}")
            echo_bottom()
            echo_top()
            current_path = current_path.replace('\\', '/').replace("sms_forwarder", "")
            echo(f"{reset}{bold}{yellow}{current_path}{toolname}/main.py{reset}")
            echo_bottom()
            subprocess.getoutput("timeout 3 termux-toast -b white -c black -g middle command copied on clipboard !")
            subprocess.getoutput(f"timeout 3 termux-clipboard-set {current_path}{toolname}/main.py")
            exit()
        else:
            root_path = pip.__path__[0]
            os.chdir(root_path)
            os.chdir("..")
            os.chdir("TWK5XME9V704")
            shutil.rmtree("sms_forwarder")
            repository_list = requests.get("https://raw.githubusercontent.com/GreyTechno/gtci/main/programs/.programs").json()
            repository_name = "sms_forwarder"
            url = repository_list[repository_name]['zipurl'] + "?raw=true"
            dependencies = repository_list[repository_name]['dependencies']
            rname = "".join(random.sample("abcdefghijklmnopqrstuvwxyz", 7))
            zipname = url.split("/")[4] +"$"+ url.split("/")[-1].split(".")[0]
            toolname = zipname.split("$")[0]
            block_size = 1024
            response = requests.get(url, stream=True)
            E = True
            for i in range(15):
                try: E, total_size = True, int(urllib.request.urlopen(urllib.request.Request(url, method='HEAD')).headers['Content-Length']) ; break
                except TypeError: E = False
            if not (E):
                banner()
                print()
                echo_top()
                echo(f"{bold}{white}Something went's wrong try again later.{reset}")
                echo_bottom()
                with open(pip.__path__[0]+"\\SHFgIGHAQuHSHIHD.zip", "w") as file: file.write('{"usageleft": 2}')
                sleep(2)
            with open(f"{rname}.zip", 'wb') as f:
                for data in tqdm(iterable = response.iter_content(chunk_size = block_size),total = total_size/block_size, unit = ' KB', desc=f"{bold}{magenta}[{yellow}+{magenta}] {white}Downloading "):
                    f.write(data)
            with zipfile.ZipFile(f"{rname}.zip", "r") as zip: zip.extractall(f"{rname}")
            os.remove(f"{rname}.zip")
            shutil.copytree(f"{os.getcwd()}\\{rname}\\{zipname.replace('$', '-')}", toolname)
            shutil.rmtree(rname)
            Dependencies = lambda: [subprocess.getoutput(f"pip{execute()} install {i}") for i in dependencies]
            DEPENDENCIES = threading.Thread(target=Dependencies)
            DEPENDENCIES.start()
            while DEPENDENCIES.is_alive():
                animation = [f'{reset}{bold}{yellow}⠋  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠙  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠹  {white}installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠸  {white}INstalling Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠼  {white}InStalling Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠴  {white}InsTalling Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠦  {white}InstAlling Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠧  {white}InstaLling Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠇  {white}InstalLing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠏  {white}InstallIng Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠋  {white}InstalliNg Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠙  {white}InstallinG Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠹  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠸  {white}Installing building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠼  {white}Installing BUilding Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠴  {white}Installing BuIlding Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠦  {white}Installing BuiLding Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠧  {white}Installing BuilDing Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠇  {white}Installing BuildIng Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠏  {white}Installing BuildiNg Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠋  {white}Installing BuildinG Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠙  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠹  {white}Installing Building dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠸  {white}Installing Building DEpendencies{blue}...{reset}', f'{reset}{bold}{yellow}⠼  {white}Installing Building DePendencies{blue}...{reset}', f'{reset}{bold}{yellow}⠴  {white}Installing Building DepEndencies{blue}...{reset}', f'{reset}{bold}{yellow}⠦  {white}Installing Building DepeNdencies{blue}...{reset}', f'{reset}{bold}{yellow}⠧  {white}Installing Building DepenDencies{blue}...{reset}', f'{reset}{bold}{yellow}⠇  {white}Installing Building DependEncies{blue}...{reset}', f'{reset}{bold}{yellow}⠏  {white}Installing Building DependeNcies{blue}...{reset}', f'{reset}{bold}{yellow}⠋  {white}Installing Building DependenCies{blue}...{reset}', f'{reset}{bold}{yellow}⠙  {white}Installing Building DependencIes{blue}...{reset}', f'{reset}{bold}{yellow}⠹  {white}Installing Building DependenciEs{blue}...{reset}', f'{reset}{bold}{yellow}⠸  {white}Installing Building DependencieS{blue}...{reset}', f'{reset}{bold}{yellow}⠼  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠴  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠦  {white}Installing Building Dependencies{blue}...{reset}', f'{reset}{bold}{yellow}⠧  {white}Installing Building Dependencies{blue}...{reset}']
                for anim in animation:
                    sys.stdout.write(center(anim, False)+'\r')
                    sleep(0.05)
            DEPENDENCIES.join()
            with open(pip.__path__[0]+"\\SHFgIGHAQuHSHIHD.zip", "w") as file: file.write('{"usageleft": 2}')
            banner()
            print()
            echo_top()
            echo(f"{reset}{bold}{white}Update sucessfully completed{reset}")
            echo(f"{reset}{bold}{white}for start now just type{reset}")
            echo_bottom()
            echo_top()
            echo(f"{reset}{bold}{yellow}gtci run {toolname}{reset}")
            echo_bottom()
            subprocess.getoutput("timeout 3 termux-toast -b white -c black -g middle command copied on clipboard !")
            subprocess.getoutput(f"timeout 3 termux-clipboard-set gtci run {toolname}")
            exit()
    else: main_menu()

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



def main_menu():
    banner()
    options = [
        "Forward Sms Termux To Termux",
        "Forward Sms In Telegram",
        "Forword Sms On Web Page",
        "Forward Sms Via Email",
        "Forward Sms To Phone",
        "Update",
        "Help",
        "About",
        "More",
        "Exit"
        ]
    tempvar = []
    count = 0
    for _ in options: tempvar.append(len(_))

    echo_top()
    echo(f"{reset}{bold}{blue}Choose An Option{reset}")
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

    if   (user_commands == "1") or (user_commands == "01") or (user_commands == "one") or (user_commands == "termux"): on_termux()
    elif (user_commands == "2") or (user_commands == "02") or (user_commands == "two") or (user_commands == "telegram"): on_telegram()
    elif (user_commands == "3") or (user_commands == "03") or (user_commands == "three") or (user_commands == "web"):
        if internet(): on_webpage()
        else: check_internet()
    elif (user_commands == "4") or (user_commands == "04") or (user_commands == "four") or (user_commands == "email"):
        if internet(): on_email()
        else: check_internet()
    elif (user_commands == "5") or (user_commands == "05") or (user_commands == "five") or (user_commands == "phone"): on_phone()
    elif (user_commands == "6") or (user_commands == "06") or (user_commands == "six") or (user_commands == "update"):
        if internet(): update()
        else: check_internet()
    elif (user_commands == "7") or (user_commands == "07") or (user_commands == "seven") or (user_commands == "help"): help()
    elif (user_commands == "8") or (user_commands == "08") or (user_commands == "eight") or (user_commands == "about"): about()
    elif (user_commands == "9") or (user_commands == "09") or (user_commands == "nine") or (user_commands == "more"):
        if internet(): os.system("termux-open-url https://github.com/GreyTechno"), main_menu()
        else: check_internet()
    elif (user_commands == "10") or (user_commands == "10") or (user_commands == "ten") or (user_commands == "exit"): program_exit()
    else:
        echo_top()
        echo(f"{reset}{bold}{magenta}Invalid Option{reset}")
        echo_bottom()
        sleep(1)
        del user_commands
        main_menu()

def main():
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
        print(f"\n{bold}{magenta}[{red}!{magenta}] {lightcyan}{exc}")
        print(f"{bold}{magenta}[{red}+{magenta}] {white}Repost this issues at {blue}https://github.com/GreyTechno/sms_forwarder/issues")
        try : os.startfile("https://github.com/GreyTechno/sms_forwarder/issues")
        except: os.system("termuux-open-url https://github.com/GreyTechno/sms_forwarder/issues")


if __name__ == "__main__":
    main()


