#!/usr/bin/env python3

import smtplib
import sys
import threading
from email.message import EmailMessage

threadLock = threading.Lock()
threads = []

def spam(email, password, to_mail, subject, message, num):
    msg = EmailMessage()
    msg.set_content(message)

    msg['Subject'] = subject
    msg['From'] = email
    msg['To'] = to_mail

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    try:
        threadLock.acquire()
        server.login(email, password)
        threadLock.release()
    except smtplib.SMTPAuthenticationError:
        threadLock.acquire()
        print("Invalid email or password!")
        threadLock.release()
        sys.exit()
    for x in range(int(num)):
        try:
            threadLock.acquire()
            server.send_message(msg)
            print("\033[92mSuccessfully sent!\033[0m")
            threadLock.release()

        except KeyboardInterrupt:
            print("")
            sys.exit()

        except:
            print("\nFailed sent!")
            server.quit()
            break

if __name__ == '__main__':
    t = threading.Thread(target=spam())
    threads.append(t)
    t.start()

    for i in threads:
        i.join()
    print("\nDone!")
