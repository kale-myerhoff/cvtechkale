class Person:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def name(self):
        print('name')
    def talk(self):
        print("self")

person = Person(10, 20)
print(person.x)