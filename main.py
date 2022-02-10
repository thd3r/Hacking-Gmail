#!/usr/bin/env python3

import shutil
import sys
import os
from getpass import getpass
from time import sleep

try:
    print("Cleaning up cache...")
    sleep(1)
    shutil.rmtree('Bot/__pycache__')
    shutil.rmtree('src/__pycache__')
except:
    print("\033[91mError can't clear cache!\033[0m")
    sleep(0.8)
    pass

if os.name in ['nt', 'win32']:
    os.system('cls')
else:
    os.system('clear')

try:
    from colorama import Fore
except ImportError:
    print(Fore.RED + "Please install library \n command > python3 -m pip install -r requirments.txt" + Fore.WHITE)

def startMessage():
    start = getpass(prompt=Fore.YELLOW + "Code To Unlock The Tool: " + Fore.WHITE)
    xyz = "999666"
    try:
        if start != xyz:
            sleep(0.5)
            print(Fore.RED + '[X] Wrong Code' + Fore.WHITE)
            print(Fore.BLUE + '''
1. Go to telegram
2. Join https://t.me/codebytexbot
3. Send #GetCode In Bot
4. You Will Get Code For Free
5. Next time come with code and use this tool
''' + Fore.WHITE)
            try:
                ask = input("Do you want to get the code? (N/y) ")
                if ask == 'y' or ask == 'Y':
                    from bot import Bot
                    print("\n")
                    print(Fore.YELLOW + "Thank You!" + Fore.WHITE)
                    exit()
                elif ask == 'n' or ask == 'N':
                    startMessage()
                else:
                    print(Fore.RED + "Invalid input!\n" + Fore.WHITE)
                    startMessage()

            except KeyboardInterrupt:
                print("")
                sys.exit()
        else:
            sleep(1)
            print("")
            print(Fore.GREEN + "Successfully Unlocked Tool!" + Fore.WHITE)
            pass
    except KeyboardInterrupt:
        print("")
        sys.exit()


if __name__ == '__main__':
    startMessage()
    try:
        print("""
1. Brute Force Email
2. Spam Chat Email
""")
        input1 = input("(\033[96muse\033[0m)/> ")
        if input1 == '1':
            email = input("(\033[96muse/BruteForceEmail/Email\033[0m)/> ")
            wordlist = input("(\033[96muse/BruteForceEmail/Wordlist\033[0m)/> ")
            from src.BruteForceEmail import bruteForce
            print("\nProceeding with wordlist: {}".format(wordlist))
            bruteForce(email, wordlist)
            print("Session completed.")

        elif input1 == '2':
            mail = input("(\033[96muse/SpamChatEmail/YourEmail\033[0m)/> ")
            password = getpass(prompt="(\033[96muse/SpamChatEmail/Password\033[0m)/> ")
            target = input("(\033[96muse/SpamChatEmail/TargetEmail\033[0m)/> ")
            subject = input("(\033[96muse/SpamChatEmail/Subject\033[0m)/> ")
            msg = input("(\033[96muse/SpamChatEmail/Message\033[0m)/> ")
            jum = input("(\033[96muse/SpamChatEmail/HowMuch\033[0m)/> ")
            from src.SpamChatEmail import spam
            print("\nSend by message: {}".format(msg))
            spam(mail, password, target, subject, msg, jum)
            print("Session completed.")

    except KeyboardInterrupt:
        try:
            print("\n\nCleaning up cache...")
            sleep(1)
            shutil.rmtree('Bot/__pycache__')
            shutil.rmtree('src/__pycache__')
            print("Done!!!")
            print("Goodbye!")
            sys.exit()

        except:
            print(Fore.RED + "Error can't clear cache!" + Fore.WHITE)
            print("Goodbye!")
            pass





