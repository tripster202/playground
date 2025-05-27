# standard imports
from email.message import EmailMessage
import smtplib
import random
import time
import string

# date imports
from datetime import datetime as dt
# from datetime import timedelta
from zoneinfo import ZoneInfo

# third party imports
# NONE

# local imports
# NONE

def mail_update(subject, content):
   # https://docs.python.org/3/library/email.examples.html

   recipient = "vulcanfire12@gmail.com"
   sender = "symshadow224@gmail.com"

   message = EmailMessage()
   message["Subject"] = subject
   message["To"] = recipient
   message["From"] = sender

   # timestamp = dt.now().strftime("%H:%M:%S")
   timestamp = dt.now(ZoneInfo('America/New_York')).strftime("%H:%M:%S")
   footer = "\n-- Succeed with Purpose --"

   message.set_content(f"{timestamp} EST\n\n{content}\n{footer}")

   server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
   # 2FA App Password # venmo meat room 224
   server.login(sender,"fgyxdvrxbkbzfppj")
   server.send_message(message)
   server.quit()


def generate_random_strings(num_strings, length):
   return chr(32).join([str().join(random.choices(string.ascii_uppercase, k=length)) for _ in range(num_strings)])


if __name__ == "__main__":

    print(dt.now(ZoneInfo('America/New_York')).strftime("%H:%M:%S"))
    print("BEGIN PERSISTENT EMAIL")

    while(True):

        # 24-hour clock
        now = dt.now(ZoneInfo('America/New_York'))

        if(now.minute % 2 > 0):
            time.sleep(random.randint(30,40))
        else:
            mail_update(f"{now.hour}{now.minute} Cycle Check",generate_random_strings(3,4))
            time.sleep(60)