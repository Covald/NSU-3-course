from __future__ import print_function
import time
from datetime import datetime
import pickle
import smtplib
import os
import envi

HOST = "smtp.gmail.com"
PORT = 465
TO = "rezin.p@gmail.com"
FROM = "p.rezin@g.nsu.ru"

LOGIN = os.environ.get("LOGIN")
PASSWORD = os.environ.get("PASSWORD")


def _parse(line: list) -> dict:
    date = datetime(*map(int, (line.pop(0)).split("-")), *map(int, line.pop(0).split(":")))
    value = " ".join(line)
    return {pickle.dumps(date): value}


def _load_from_file(file="Names and dates.txt"):
    test = {}
    with open(file, "r") as f:
        for line in f:
            print(line)
            l = line.split()
            test.update(_parse(l))
    return test


def create_message(sender, to, subject, message_text):
    sent_from = sender
    to = [to]
    subject = subject
    body = message_text

    email_text = """\
    From: %s
    To: %s
    Subject: %s
    
    %s
    """ % (sent_from, ", ".join(to), subject, body)
    return email_text


def send_email(item):
    print('asd') # abxnntlgzzkccdpe
    LOGIN = os.environ.get("LOGIN")
    PASSWORD = os.environ.get("PASSWORD")

    sent_from = LOGIN
    to = ['me@gmail.com', 'bill@gmail.com']
    subject = 'OMG Super Important Message'
    body = item

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        #server.starttls()
        server.login(LOGIN, PASSWORD)
        server.sendmail(LOGIN, TO, email_text)
    except Exception as err:
        print(f"\n Error - {err} \n")



def main():
    envi.setenv()
    dict_of_file = _load_from_file()
    print(dict_of_file)
    while True:
        now = datetime.now()
        print(f"now - {now}")
        send = []
        for date in list(map(pickle.loads, dict_of_file.keys())):
            print(date)
            print(f"{date.timestamp()} + {60 * 60} = {date.timestamp() + 60 * 60} --- {now.timestamp()}")
            if date.timestamp() + 60 * 60 <= now.timestamp():
                print(f"send date - {date}")
                send.append(dict_of_file.get(pickle.dumps(date)))

        for i in send:
            send_email(i)
        time.sleep(1)


if __name__ == '__main__':
    main()
