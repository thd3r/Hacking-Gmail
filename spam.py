import smtplib, sys
from email.message import EmailMessage

class SendMail:
    def __init__(self, email, password, to_mail, subject, message):
        self.email = email
        self.password = password
        self.to_mail = to_mail
        self.subject = subject
        self.message = message

    def main(self):
        mail = self.email
        passwd = self.password
        to = self.to_mail
        subject = self.subject
        message = self.message

        msg = EmailMessage()
        msg.set_content(message)

        msg['Subject'] = subject
        msg['From'] = mail
        msg['To'] = to

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        try:
            server.login(mail, passwd)
        except smtplib.SMTPAuthenticationError:
            print("Invalid email or password!")
            sys.exit()
        while True:
            try:
                server.send_message(msg)
                print("Successfully to sent!")
            except KeyboardInterrupt:
                sys.exit()
            except:
                print("\nFailed sent!")
                server.quit()
                break

if len(sys.argv) < 3:
    print("\n\033[93mSpam Email\033[0m\n")
    print("Usage:")
    print("\tpython3 spam.py <your email> <your password>")

else:
    mail = sys.argv[1]
    passwd = sys.argv[2]
    to = input("To: ")
    subject = input("Subject: ")
    msg = input("Message: ")

    exp = SendMail(email=mail, password=passwd, to_mail=to, subject=subject, message=msg)
    exp.main()
