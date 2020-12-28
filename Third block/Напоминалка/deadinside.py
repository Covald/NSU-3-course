from __future__ import print_function
import time
from datetime import datetime
import pickle
import smtplib
import os
from authenticate import LOGIN, PASSWORD

HOST = "smtp.gmail.com"
PORT = 465
TO = ["rezin.p@gmail.com"]
FROM = "p.rezin@g.nsu.ru"
SUBJECT = "Subject"


def _parse(line: list) -> dict:
    """
    Парсим строку с напоминанием и составляем словарь вида {дамп объекта datetime : текст напоминания}
    """
    date = datetime(*map(int, (line.pop(0)).split("-")), *map(int, line.pop(0).split(":")))
    value = " ".join(line)
    return {pickle.dumps(date): value}


def _load_from_file(file: str = "Names and dates.txt") -> dict:
    """
    Собираем из файла все строки, парсим и
    формируем конечный словарь вида {дамп объекта datetime : текст напоминания}
    """
    test = {}
    with open(file, "r") as f:
        for line in f:  # type: str
            print(line)
            split_line = line.split()
            test.update(_parse(split_line))
    return test


def create_message(sender: str, to: list, subject: str, message_text: str) -> str:
    """
    Собираем сообщение по формату
    """
    sent_from = sender
    to = to
    subject = subject
    body = message_text

    email_text = """\
    From: %s
    To: %s
    Subject: %s
    
    %s
    """ % (sent_from, ", ".join(to), subject, body)
    return email_text


def send_email(item: str) -> None:
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        print(server.ehlo())
        email_text = create_message(FROM, TO, SUBJECT, item)
        print(email_text)
        print(server.login(LOGIN, PASSWORD))
        server.sendmail(FROM, TO, email_text)
    except Exception as err:
        print(f"\n Error - {err} \n")


def main():
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
