import subprocess, os, threading
from sms_forwarder import *


def Installer():
    try:
        def install(*args):
            for i in args: os.system("pip insall "+i)
        UNIMPORTED = []
        try: import requests
        except: UNIMPORTED.append("requests")
        try: import smtplib
        except: UNIMPORTED.append("secure-smtplib")
        if (len(UNIMPORTED) != 0):
            Banner()
            center(f"{red}╔══════════════════════════════════════════╗", 5)
            center(f"{red}║ {yellow}SOME DEPENDENCIES COULD NOT BE INSTALLED {red}║", 15)
            center(f"{red}╚══════════════════════════════════════════╝", 5)
            INSTALL = threading.Thread(target=install, args=(UNIMPORTED))
            INSTALL.start()
            while INSTALL.is_alive(): AnimLOAD(f" {yellow}Installing Building Dependencies...{white}", "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏", 1, 0.05)
            INSTALL.join()
            Installer()
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
            if (len(UNIMPORTED) == 0):
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

Installer()