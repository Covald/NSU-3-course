import pickle
import string
import random
import json

import numpy


class Person:
    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return f"{self.name} {self.surname} {self.phone}"


def buildblock(size):
    return ''.join(random.choice(string.ascii_letters) for i in range(size))


def create_list(N):
    l = []
    for i in range(N):
        name = buildblock(6)
        surname = buildblock(10)
        phone = ''.join(map(str, numpy.random.randint(0, 10, 11)))
        l.append(Person(name=name, surname=surname, phone=phone))  # ''', 'surname': surname, 'phone': phone'''))
    return l


def print_list(l: list):
    print("-" * 10)
    for p in l:
        print(p)
    print("-" * 10)


def save_p(l: list) -> None:
    with open("persons", "wb") as f:
        pickle.dump(l, f)


def load_p() -> list:
    with open("persons", "rb") as f:
        return pickle.load(f)


def save(l: list) -> None:
    with open('people', "w") as f:
        for p in l:
            f.write(str(p) + "\n")


def load() -> list:
    l = []
    with open('people', "r") as f:
        for line in f:
            s = line.strip().split()
            print(s)
            l.append(Person(name=s[0], surname=s[1], phone=s[2]))
    return l


if __name__ == "__main__":
    persons = create_list(int(input("Enter num of People - ")))

    print_list(persons)

    persons = sorted(persons, key=lambda x: x.name)
    print_list(persons)

    save(persons)
    print_list(load())

    save_p(persons)
    print_list(load_p())
