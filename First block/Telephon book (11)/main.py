from Person import Person


def create_list(N):
    l = []
    for i in range(N):
        name = input("Name - ")
        surname = input("Surname - ")
        birth_date = input("Birth_date - ")
        phone = input("Phone - ")
        l.append(Person(name, surname, birth_date, phone))
    return l


def print_list(people):
    for person in people:
        print(person.name)


if __name__ == "__main__":
    persons = create_list(int(input("Enter num of People - ")))
    print(p)
    print_list(persons)
    sorted(persons, key=lambda x: x.name)
    print_list(persons)
