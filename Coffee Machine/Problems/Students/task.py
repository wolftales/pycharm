class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here

    def id(self):
        print(f'{self.name[0]}{self.last_name}{int(self.birth_year)}')


name = input()
last_name = input()
birth_year = input()

student01 = Student(name, last_name, birth_year)

student01.id()


