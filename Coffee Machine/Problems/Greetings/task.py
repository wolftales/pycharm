class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        print(f'Hello, I am {self.name}!')


person = input()
my_greeting = Person(person)
my_greeting.greet()
