import string
import random
import json

class Person:
    def __init__(self, name=None, surname=None, birth_date=None, phone_number=None):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.phone_number = phone_number

    def get_name(self):
        return self.name


def buildblock(size):
    return ''.join(random.choice(string.ascii_letters) for i in range(size))


def create_list(N):
    l = []
    for i in range(N):
        name = buildblock(6)
        l.append(Person(name))
    return l


def print_list(people):
    l = []
    for person in people:
        l.append(person.name)
    print(l)


if __name__ == "__main__":
    persons = create_list(int(input("Enter num of People - ")))
    print(persons)
    print_list(persons)
    persons = sorted(persons, key=lambda x: x.name)
    print_list(persons)
    file = open("persons")
    json.dump(persons, file)
    print(persons)