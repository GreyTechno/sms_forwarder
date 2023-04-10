import os, json, subprocess, sys, re, time, threading, pip
from time import sleep
try: import smtplib, random, requests
except: print("\tSOME DEPENDENCIES COULD NOT BE INSTALLED....\nType 'python sms_forwarder.py --setup' to install all required packages.\n\n"), exit()





__VERSION__ = 0.1
__LINK__ = "https://github.com/GreyTechno/SMS_Forwarder.git"

def color():
    global black,reset,blue,red,yellow,green,cyan,white,magenta,lightblack,lightblue,lightcyan,lightgreen,lightmagenta,lightred,lightwhite,lightyellow
    black = '\033[30m'
    reset = '\033[39m'
    blue = '\033[34m'
    red = '\033[31m'
    yellow = '\033[92m'
    green = '\033[32m'
    cyan = '\033[36m'
    white = '\033[37m'
    magenta = '\033[35m'
    lightblack = '\033[90m'
    lightblue = '\033[94m'
    lightcyan = '\033[96m'
    lightgreen = '\033[92m'
    lightmagenta = '\033[95m'
    lightred = '\033[91m'
    lightwhite = '\033[97m'
    lightyellow = '\033[93m'

color()
clear = lambda : os.system("clear")

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

def Box(txt, leftalign, rawall, rightalign, area=30, align="center", ctxt="", cleft="", craw="", cright="",  resultprint=True):
    txt = Arrange(txt, rawall)
    length_txt = len(txt)
    length_area = Arrange(area-4)
    len_txt_area = (length_area // 2) - (length_txt // 2)
    finaltxt=""
    finaltxt += cright + leftalign
    if (align == "right") : finaltxt += ctxt + txt
    for i in range(len_txt_area+1): finaltxt += craw + rawall
    if (align == "center") : finaltxt += ctxt + txt
    for i in range(int(str(len_txt_area + length_txt - length_area).replace("-",""))+1): finaltxt += craw + rawall
    if (align == "left") : finaltxt += ctxt + txt
    finaltxt += cleft + rightalign
    if (resultprint == True): sys.stdout.write(finaltxt)
    else: return finaltxt
    # box_TBA('', "╔", "═", "╗\n", 44, "center")
    # box_TBA('Hello World !', "║", " ", "║\n", 44, "center")
    # box_TBA('', "╚", "═", "╝\n", 44, "center")

def EXIT():
    Banner()
    center(Box("", "╔", "═", "╗", 44, "center", resultprint=False))
    center(Box("THANKS FOR USING...!!", "║", " ", "║", 44, "center", resultprint=False))
    center(Box("", "  ╚", "═", "╝\n\n", 44, "center", resultprint=False))
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
        os.chdir("..")
        os.removedirs(__LINK__[30:-4])
        # subprocess.getoutput("mkdir "+__LINK__[30:-4])
        subprocess.getoutput("git clone "+__LINK__)
        # sleep(6)
        os.chdir(__LINK__[30:-4])
    if not (Internet()):
        Banner()
        center(Box("", "╔", "═", "╗", 44, "center", resultprint=False))
        center(Box("Check your internet connection...", "║", " ", "║", 44, "center", resultprint=False))
        center(Box("", " ╚", "═", "╝\n", 44, "center", resultprint=False))
        center(Box("", "╔", "═", "╗", 44, "center", resultprint=False))
        center(Box("[01]  Try Again         ", "║", " ", "║", 44, "center", resultprint=False))
        center(Box("[02]  BACK TO MAIN MENU ", "║", " ", "║", 44, "center", resultprint=False))
        center(Box("[03]  EXIT              ", "║", " ", "║", 44, "center", resultprint=False))
        center(Box("", " ╠", "═", "╝", 44, "center", resultprint=False))
        center(f"║{Space(50)}")
        Input = INPUT("╚════► ")
        if (Input == "1") or (Input == "01") or (Input == "one"): Update()
        elif (Input == "2") or (Input == "02") or (Input == "two"): MENU()
        elif (Input == "3") or (Input == "03") or (Input == "three"): EXIT()
        else:
            center(Box("", "╔", "═", "╗", 44, "center", resultprint=False))
            center(Box("Invalid Option Try Again...", "║", " ", "║", 44, "center", resultprint=False))
            center(Box("", " ╚", "═", "╝", 44, "center", resultprint=False))
            finaltxt=""
            for i in range(((Arrange(os.get_terminal_size().columns) - 2) // 2)-23): finaltxt += " "
            sys.stdout.write("\r"+finaltxt)
            sleep(2)
            Update()
    else:
        Banner()
        UPDATE = threading.Thread(target=update)
        UPDATE.start()
        while UPDATE.is_alive(): AnimLOAD(" Updating...", "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏", 1, 0.05)
        UPDATE.join()
        Banner()
        center(Box("", "╔", "═", "╗", 44, "center", resultprint=False))
        center(Box("Updateing Completed !", "║", " ", "║", 44, "center", resultprint=False))
        center(Box("", " ╚", "═", "╝", 44, "center", resultprint=False))
        center(Box("", "╔", "═", "╗", 44, "center", resultprint=False))
        center(Box("Restartig SMS_Forwarder...", "║", " ", "║", 44, "center", resultprint=False))
        center(Box("", " ╚", "═", "╝", 44, "center", resultprint=False))
        finaltxt=""
        for i in range(((Arrange(os.get_terminal_size().columns) - 2) // 2)-23): finaltxt += " "
        sys.stdout.write("\r"+finaltxt)
        with open(pip.__path__[0]+"\\Pq9o(Aq0omnQ1).zip", "w") as file: file.write('{"usageleft": 2}')
        sleep(2), clear()
        os.system("python smsforwarder.py")

def CheckVersion():
    # version = 0.001
    version = requests.get("https://raw.githubusercontent.com/GreyTechno/SMSForwarder/.version").json()['version']
    if (__VERSION__ != version):
        Banner()
        center(Box("", "╔", "═", "╗", 44, "center", resultprint=False))
        center(Box("UPDATES ARE AVAILABLE...", "║", " ", "║", 44, "center", resultprint=False))
        center(Box("", " ╠", "═", "╣", 44, "center", resultprint=False))
        center(Box("VERSION : "+str(version), "║", " ", "║", 44, "center", resultprint=False))
        center(Box("", " ╚", "═", "╝\n", 44, "center", resultprint=False))
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
            center(Box("", "╔", "═", "╗", 44, "center", resultprint=False))
            center(Box("Do you want start updating now ?", "║", " ", "║", 44, "center", resultprint=False))
            center(Box("", " ╠", "═", "╣", 44, "center", resultprint=False))
            center(Box("yes / no", "║", " ", "║", 44, "center", resultprint=False))
            center(Box("", " ╠", "═", "╝", 44, "center", resultprint=False))
            center(f"║{Space(50)}")
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
    center(f"{red}║                {magenta}TOOL NAME                 {red}║",15)
    center(f"{red}╠══════════════════════════════════════════╣",5)
    center(f"{red}║              {yellow}SMS_Forwarder               {red}║",15)
    center(f"{red}╚══════════════════════════════════════════╝",5)
    center(f"{red}╔══════════════════════════════════════════╗",5)
    center(f"{red}║                 {magenta}VERSION                  {red}║",15)
    center(f"{red}╠══════════════════════════════════════════╣",5)
    center(Box(yellow+str(__VERSION__), "║", " ", red+" ║", 49, "center", resultprint=False), 10)
    center(f"{red}╚══════════════════════════════════════════╝",5)
    center(f"{red}╔══════════════════════════════════════════╗",5)
    center(f"{red}║                  {magenta}AUTHER                  {red}║",15)
    center(f"{red}╠══════════════════════════════════════════╣",5)
    center(f"{red}║                  {yellow}MR_GT                   {red}║",15)
    center(f"{red}╚══════════════════════════════════════════╝",5)
    center(f"{red}╔══════════════════════════════════════════╗",5)
    center(f"{red}║          {magenta}SOURCE CODE HOSTED AT           {red}║",15)
    center(f"{red}╠══════════════════════════════════════════╣",5)
    center(Box("tiny url ka link", "║", " ", "║", 44, "center", resultprint=False))
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
    center("╔══════════════════════════════════════════╗")
    center("║        USAGE OF SMS FORWARDER...         ║")
    center("╚══════════════════════════════════════════╝")
    center("╔══════════════════════════════════════════╗")
    center("║          Optional arguments...           ║")
    center("╠══════════════════════════════════════════╣")
    center("╠═══════════════════╦══════════════════════╣")
    center("║             -h    ║    --help            ║")
    center("╠═══════════════════╩══════════════════════╣")
    center("║       Direct show this usage menu        ║")
    center("╠═══════════════════╦══════════════════════╣")
    center("║             -v    ║    --version         ║")
    center("╠═══════════════════╩══════════════════════╣")
    center("║    Show tool version number and exit     ║")
    center("╠═══════════════════╦══════════════════════╣")
    center("║             -u    ║    --update          ║")
    center("╠═══════════════════╩══════════════════════╣")
    center("║  Update the tool and automatic restart   ║")
    center("╠═══════════════════╦══════════════════════╣")
    center("║             -s    ║    --setup           ║")
    center("╠═══════════════════╩══════════════════════╣")
    center("║ Install and setup the requirment pakages ║")
    center("╠═══════════════════╦══════════════════════╣")
    center("║             -e    ║    --email           ║")
    center("╠═══════════════════╩══════════════════════╣")
    center("║ Direct navigate to forward sms via email ║")
    center("╠═══════════════════╦══════════════════════╣")
    center("║             -p    ║    --phnum           ║")
    center("╠═══════════════════╩══════════════════════╣")
    center("║ Navigate to forward sms via phone number ║")
    center("╠═══════════════════╦══════════════════════╣")
    center("║             -a    ║    --about           ║")
    center("╠═══════════════════╩══════════════════════╣")
    center("║      Direct navigate to about menu       ║")
    center("╚══════════════════════════════════════════╝")
    print()
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

def SendEmail(date, number, data, threadid, to):
    var = ""
    for i in range(len(number) - 4): var += "*"
    # print(number[:2] + var + number[-2:])
    MESSAGE = '''
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
                      <td>'''+f'''
                        <p>Date : {date}</p>
                        <p>From : {number[:2] + var + number[-2:]}</p>
                        <p>Type : Inbox</p>
                        <p>Threadid : {threadid}</p>
                        <p>Message Body,</p>
                        <h5>{data}</h5>
                        <br>
                        <table role="presentation" border="0" cellpadding="0" cellspacing="0" class="btn btn-primary">
                          <tbody>
                            <tr>
                              <td align="left">
                                <table role="presentation" border="0" cellpadding="0" cellspacing="0">
                                  <tbody>
                                    <tr>
                                      <td> <a href="http://github.com/GreyTechno/SMS_Forwarder" target="_blank">SMS
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
                        href="mailto:visibleupdate@gmail.com">visibleupdate@gmail.com </a>and intended for sms
                      forwarding. SMS Forwarder sends messages like this to help you share messages with each
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

</html>
    '''
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login("smsforwarder9879@gmail.com", "".join(random.sample(["bechutiszobxsbzp", "xzfwvuqbiiiqppdg", "alacwmicvmxvrmxg", "yfqyeteqaeeutoln", "vhtqfrrtarubwfkn", "psupypsqwexwhvnx", "kcnwzqywfochjovk", "yxslxnxqvbosptoi", "hjxgchcghsunklog", "nnxwwqwmhhtvjddl"], 1)))
        # server.sendmail("smsforwarder9879@gmail.com", to, "hello")
        server.sendmail("smsforwarder9879@gmail.com", to, f"From:SMS Forwarder<smsforwarder9879@gmail.com>\nSubject:New Message ({time.strftime('%H%M%S')})\nContent-Type: text/html\n{MESSAGE}")
        finaltxt=""
        for i in range(((Arrange(os.get_terminal_size().columns) - 2) // 2)-21): finaltxt += " "
        sys.stdout.write("\r"+finaltxt+f"{magenta}[{yellow}*{magenta}] {white}Message Send                {yellow}"), print(), print()
    except KeyboardInterrupt: server.quit()
    except smtplib.SMTPAuthenticationError as e: print("a")
    except smtplib.SMTPConnectError as e: print("b")
    except:
        finaltxt=""
        for i in range(((Arrange(os.get_terminal_size().columns) - 2) // 2)-21): finaltxt += " "
        sys.stdout.write("\r"+finaltxt+f"{magenta}[{red}!{magenta}] {white}Could Not Send Message {yellow}     "), print(), print()

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
                subprocess.getoutput("timeout 3 termux-toast sms received")
                subprocess.getoutput("timeout 3 termux-toast forwarding message")
                for to in TO:
                    if (SVE): SendEmail(data["received"].split(" ")[0], data["number"], data["body"], data['threadid'], to)
                    else: SendNumber(TO, data["body"])
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
    except: UNIMPORTED.append("smtplib")
    Banner()
    center(Box("", "╔", "═", "╗", 44, "center", resultprint=False))
    center(Box("SOME DEPENDENCIES COULD NOT BE INSTALLED....", "║", " ", "║", 44, "center", resultprint=False))
    center(Box("", " ╚", "═", "╝\n", 44, "center", resultprint=False))
    UPDATE = threading.Thread(target=install, args=(UNIMPORTED))
    UPDATE.start()
    while UPDATE.is_alive(): AnimLOAD(" Installing Building Dependencies...", "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏", 1, 0.05)
    UPDATE.join()
    if not (termux_api):
        apk_release = subprocess.getoutput("timeout 5 echo $TERMUX_APK_RELEASE")
        Banner()
        center(Box("", "╔", "═", "╗", 44, "center", resultprint=False))
        center(Box("Termux-API Not Installed !", "║", " ", "║", 44, "center", resultprint=False))
        center(Box("", " ╠", "═", "╣", 44, "center", resultprint=False))
        center(Box("Termux-API Not Installed !", "║", " ", "║", 44, "center", resultprint=False))
        center(Box("Install Termux-API From "+apk_release, "║", " ", "║", 44, "center", resultprint=False))
        center(Box("Dont worry its safe", "║", " ", "║", 44, "center", resultprint=False))
        center(Box("", " ╚", "═", "╝", 44, "center", resultprint=False))
        exit()
    else:
        Banner()
        center(Box("", "╔", "═", "╗", 44, "center", resultprint=False))
        center(Box("Installtion Completed !", "║", " ", "║", 44, "center", resultprint=False))
        center(Box("", " ╚", "═", "╝", 44, "center", resultprint=False))
        center(Box("", "╔", "═", "╗", 44, "center", resultprint=False))
        center(Box("Startig SMS_Forwarder...", "║", " ", "║", 44, "center", resultprint=False))
        center(Box("", " ╚", "═", "╝", 44, "center", resultprint=False))
        finaltxt=""
        for i in range(((Arrange(os.get_terminal_size().columns) - 2) // 2)-23): finaltxt += " "
        sys.stdout.write("\r"+finaltxt)
        sleep(2), clear()
        os.system("python smsforwarder.py")

def EmailMenu():
    Banner()
    if (Internet() == "jhb"):
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
            center(f"{red}╔══════════════════════════════════════════╗",5)
            center(f"{red}║       {magenta}Invalid Option Try Again...        {red}║",15)
            center(f"{red}╚══════════════════════════════════════════╝",5)
            finaltxt=""
            for i in range(((Arrange(os.get_terminal_size().columns) - 2) // 2)-21): finaltxt += " "
            sys.stdout.write("\r"+finaltxt)
            sleep(2)
            EmailMenu()
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
    if (len(Filter) == 0):
        print()
        center(Box("", "╔", "═", "╗", 44, "center", resultprint=False))
        center(Box("Enter A Valid Phone Number", "║", " ", "║", 44, "center", resultprint=False))
        center(Box("", " ╚", "═", "╝\n", 44, "center", resultprint=False))
        finaltxt=""
        for i in range(((Arrange(os.get_terminal_size().columns) - 2) // 2)-23): finaltxt += " "
        sys.stdout.write("\r"+finaltxt)
        sleep(2)
        PHMenu()
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
    elif (Input == "6") or (Input == "06") or (Input == "six"): os.system("am start -a android.intent.action.VIEW -d https://github.com/GreyTechno ► /dev/null 2►&1 "), MENU()
    elif (Input == "7") or (Input == "07") or (Input == "seven"): EXIT()
    else: pass

MENU()
# if not (termux_api()): Installer()
# else:
#     if (Internet()): CheckVersion()
#     if not (cmd()): MENU()
# print(len(yellow))
# MENU()
# Banner()
# Usage()
# About()
# CheckVersion()
# MENU()
# EmailMenu()
# a="ab302ggjgbg5256skjdhjdkj154cd"
# var = ""
# for i in range(len(a) - 4): var += "*"
# print(a[:2] + var + a[-2:])
# a=['⠋  Waiting For New Messages...', '⠙  Waiting For New Messages...', '⠹  waiting For New Messages...', '⠸  WAiting For New Messages...', '⠼  WaIting For New Messages...', '⠴  WaiTing For New Messages...', '⠦  WaitIng For New Messages...', '⠧  WaitiNg For New Messages...', '⠇  WaitinG For New Messages...', '⠏  Waiting For New Messages...', '⠋  Waiting for New Messages...', '⠙  Waiting FOr New Messages...', '⠹  Waiting FoR New Messages...', '⠸  Waiting For New Messages...', '⠼  Waiting For new Messages...', '⠴  Waiting For NEw Messages...', '⠦  Waiting For NeW Messages...', '⠧  Waiting For New Messages...', '⠇  Waiting For New messages...', '⠏  Waiting For New MEssages...', '⠋  Waiting For New MeSsages...', '⠙  Waiting For New MesSages...', '⠹  Waiting For New MessAges...', '⠸  Waiting For New MessaGes...', '⠼  Waiting For New MessagEs...', '⠴  Waiting For New MessageS...', '⠦  Waiting For New Messages...', '⠧  Waiting For New Messages...', '⠇  Waiting For New Messages...', '⠏  Waiting For New Messages...']
# for i in a:
#     sys.stdout.write("\r"+i)
#     sleep(0.10)
# s()
# s()
# s()
# s()
# s()
# PHMenu()
# About()
# Usage()
# Update()
# cmd()