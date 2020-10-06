class Person:
    def __init__(self, name=None, surname=None, birth_date=None, phone_number=None):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.phone_number = phone_number

    def get_name(self):
        return self.name
