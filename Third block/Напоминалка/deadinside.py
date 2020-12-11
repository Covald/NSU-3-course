import time
from datetime import datetime
import pickle

print(time.time())
_TIMER = 1


def _parse(line: list) -> dict:
    date = datetime(*map(int, (line.pop(0)).split("-")), *map(int, line.pop(0).split(":"))).
    value = " ".join(line)
    return {pickle.dumps(date): value}


def _load_from_file(file="Names and dates.txt"):
    test = {}
    with open(file, "r") as f:
        for line in f:
            l = line.split()
            test.update(_parse(l))
    return test


def send_email(item: dict):
    print(item)


def main():
    dict_of_file = _load_from_file()
    while True:
        now = datetime.now()
        if now.  in map(pickle.loads, dict_of_file.keys()):
            send_email(dict_of_file.get(pickle.dumps(now+_TIMER)))


if __name__ == '__main__':
    main()
