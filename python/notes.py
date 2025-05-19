# numbers = [5, 2, 1, 1, 5, 10, 7, 4]
# numbers2 = numbers.copy()
# numbers2.remove(5 and 2)
# numbers.clear()
# numbers2.pop()
# numbers2.reverse()
# numbers.append(10)
#
# print(50 in numbers2)
# print(numbers2)
# print(numbers)
from tkinter.font import names


# numbers = [1,2,2,3,4,4,4,5,7,6,7,7,8,0,9]
# singleNumberList = []
# print(numbers)
#
# for number in numbers :
#     if number not in singleNumberList:
#         singleNumberList.append(number)
#
#
# numbers = singleNumberList.copy()
# print(numbers)
#
# numbers = (1,2,3)
# print(numbers[0])
# x, y, z = numbers
# print(x*y*z)

# customers = {
#     "name" : "John Smith",
#     "age" : 30,
#     "isVerified": True,
#     "birthdate" : "september eighth 2009"
# }
#
# customers["name"] = "jack smith"
#
# print(customers.get("birthdate", "march 7 2007"))
# print(customers.get("name", "march 7 2007"))
#
# numDict = {
#     "1" : "one ",
#     "2" : "two ",
#     "3" : "three ",
#     "4" : "four ",
#     "5" : "five ",
#     "6" : "six ",
#     "7" : "seven ",
#     "8" : "eight ",
#     "9" : "nine ",
#     "0" : "zero ",
# }
#
# phoneNumber = input(f"Phone: ")
# numberToText = ""
#
# for num in phoneNumber:
#     numberToText += numDict.get(num, "")
#
# print(numberToText)

# message = input(">")
# def emoji_converter(message):
#     words = message.split(' ')
#
#     emojis = {':‑)': '\U0001F600',
#               ':)': '\U0001F600',
#               ':-]': '\U0001F642',
#               ':]': '\U0001F642',
#               ':->': '\U0001F60A',
#               ':>': '\U0001F60A',
#               '8-)': '\U0001F913',
#               '8)': '\U0001F913',
#               ':-}': '\U0001F642	',
#               ':}': '\U0001F642	',
#               ':^)': '\U0001F642	',
#               '=]': '\U0001F603',
#               '=)': '\U0001F603',
#
#
#               ':‑D': '\U0001F604',
#               ':D': '\U0001F604',
#               '8‑D': '\U0001F913',
#               '8D': '\U0001F913',
#               '=D': '\U0001F601',
#               '=3': '\U0001F63A	',
#               'B^D': '\U0001F60E',
#               'c:': '\U0001F643',
#               'C:': '\U0001F643',
#
#               'x‑D': '\U0001F606	',
#               'xD': '\U0001F606	',
#               'X‑D': '\U0001F606	',
#               'XD': "\U0001F606	",
#
#               ':-))': '\U0001F917',
#               ':))' : "\U0001F917",
#
#               ':‑(': '\U0001F61F	',
#               ':(': '\U00002639',
#               ':‑c': '\U00002639',
#               ':c': '\U00002639',
#             #   ':‑<': '',
#             #   ':<': '',
#             #   ':‑[': '',
#             #   ':[': '',
#             #   ':-||': '',
#             #   ':{': '',
#             #   ':@': '',
#             #   ";("
#             #
#             #   ":'‑(": '',
#             #   ":'(": '',
#             #   ":=(:'‑)": '',
#             #   ":')": '',
#             #   ':"D>:(': '',
#             #   '>:[': '',
#             #   "D‑':": '',
#             #   'D:<': '',
#             #   'D:': '',
#             #   'D8': '',
#             #   'D;': '',
#             #   'D=': '',
#             #   'DX': '',
#             #   ':‑O': '',
#             #   ':O': '',
#             #   ':‑o': '',
#             #   ':o': '',
#             #   ':-0': '',
#             #   ':0': '',
#             #
#             #   '8‑0': '',
#             #
#             #   '>:O': '',
#             #
#             #   '=O': '',
#             #
#             #   '=o': '',
#             #
#             #   '=0': '',
#             #
#             #   ':-3': '',
#             #
#             #   ':3': '',
#             #
#             #   'x3': '',
#             #
#             #   'X3>:3': '',
#             #
#             #   ':-*': '',
#             #
#             #   ':*': '',
#             #
#             #   '': '',
#             #
#             #   ':x': '',
#             #
#             #   ';‑)': '',
#             # ';)': '',
#             # '*-)': '',
#             # '*)': '',
#             #   ';‑]': '',
#             #   ';]': '',
#             #   ';^)': '',
#             #   ';>': '',
#             #   ':‑,': '',
#             #   ';D': '',
#             #   ';3': '',
#             #   ':‑P': '',
#             #   ':P': '',
#             #   'X‑P': '',
#             #   'XP': '',
#             #   'x‑p': '',
#             #   'xp': '',
#             #   ':‑p': '',
#             #   ':p': '',
#             #   ':‑Þ': '',
#             #   ':Þ': '',
#             #   ':‑þ': '',
#             #   ':þ': '',
#             #   ':‑b': '',
#             #   ':b': '',
#             #   'd:': '',
#             #   '=p': '',
#             #   '>:b': '',
#             #   ':-/': '',
#             #   ':/': '',
#             #   "',:^I": '',
#             #   '>:\\': '',
#             #   '>:/': '',
#             #   ':\\': '',
#             #   '=/': '',
#             #   '=\\': '',
#             #   ':L': '',
#             #   '=L': '',
#             #   ':S': '',
#             #   ':‑|': '',
#             #   ':|': '',
#             #   ':$': '',
#             #   '://)': '',
#             #   '://3:‑X': '',
#             #   ':X': '',
#             #   ':‑#': '',
#             #   ':#': '',
#             #   ':‑&': '',
#             #   ':&': '',
#             #   'O:‑)': '',
#             #   'O:)': '',
#             #   '0:‑3': '',
#             #   '0:3': '',
#             #   '0:‑)': '',
#             #   '0:)': '',
#             #   '0;^)': '',
#             #   '>:‑)': '',
#             #   '>:)': '',
#             #   '}:‑)': '',
#             #   '}:)': '',
#             #   '3:‑)': '',
#             #   '3:)': '',
#             #   '>;‑)': '',
#             #   '>;)': '',
#             #   '>:3': '',
#             #   '>;3': '',
#             #   '|;‑)': '',
#             #   '|‑O': '',
#             #   'B-) :‑J': '',
#             #   '#‑)': '',
#             #   '%‑)': '',
#             #   '%):‑###..': '',
#             #   ':###..': '',
#             #   '<:‑|': '',
#             #   "',:-|": '',
#             #   "',:-l": '',
#             #   ':E': '',
#             #   '8-X': '',
#             #   '8=X': '',
#             #   'x-3': '',
#             #   'x=3': '',
#             #   '~:>': '',
#             #   '@};-': '',
#             #   '@}->--': '',
#             #   "@}‑;‑'‑‑‑": '',
#             #   '@>‑‑>‑‑': '',
#             #   '8====D': '',
#             #   '8===D': '',
#             #   '8=D': '',
#             #   '3=D': '',
#             #   '8=>': '',
#             #   '8===D~~~': '',
#             #   '*<|:‑)': '',
#             #   '</3': '',
#             #   '<\\3': '',
#             #   '<3': '',
#             #   's2': '',
#             #   '><>': '',
#             #   '<><': '',
#             #   '<*)))‑{': '',
#             #   '><(((*>': '',
#             #   '\\o/': '',
#             #   '*\\0/*': '',
#             #   'o7': '',
#             #   'v.v': '',
#             #   '._.': '',
#             #   '._.;': '',
#             #   ';-;': '',
#             #   'T_T': '',
#             #   'T-T': '',
#             #   'QQ': '',
#             #   'Qq': '',
#             #   'qqX_X': '',
#             #   'x_x': '',
#             #   '+_+': '',
#             #   'X_x': '',
#             #   'x_X<_<': '',
#             #   '>_>': '',
#             #   '<.<': '',
#             #   '>.>': '',
#             #   'O_O': '',
#             #   'o_o': '',
#             #   'O-O': '',
#             #   'o‑o': '',
#             #   'O_o': '',
#             #   'o_O': '',
#             #   '>.<': '',
#             #   '>_<': '',
#             #   '^5': '',
#             #   'o/\\o': '',
#             #   '>_>^ ^<_<': '',
#             #   'V.v.V': '',
#             #   'V=(° °)=V': '',
#             #   '(^^^)': '',
#             #   '(::[]::)': ''
#               }
#     output =""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output
# message = input(">")
# print(emoji_converter(message))
# # running = True
# # while running:
# #     message = input(">  ")
# #
# #     emoticon = message.split(" " and "\t")
# #
# #     if message != "stop":
# #         for face in emoticon:
# #             emojis[face] = ""
# #
# #
# #
# #
# #     else:
# #         running=False
# # print(emojis)
#
# output = ""
# for word in words:
#     output += emojis.get(word, word) + " "
# print(output)

# def greet_user(first_name, last_name):
#     print(f"hiiiiii {first_name} { last_name}")
#     print("welcome")
#
#
# print("start")
# greet_user("john", "smith")
# greet_user(last_name="poopyhead", first_name="poo")
# calc_cost(total=50, shipping=5, discount=0.1)
# print("finish")

# def square(number):
#     return number*number
#
# def broken_square(number):
#     print( number*number)
#
# print(3 + square(2))
# print(broken_square(2))


# try:
#     age = int(input("age: "))
#     income = 20000
#     risk= income/age
#     print(age)
# except ZeroDivisionError:
#     print("ERROR! Unable to use 0 for age")
# except ValueError:
#     print("ERROR! invalid value")

#comments are for whys and hows

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# # point1 = Point()
# # point1.x = 10
# # point1.y = 20
# # print(point1.x)
# # point1.draw()
#
# point = Point(10, 20)
# print(point.x)

# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def talk(self):
#         print(f"i am talking and my name is {self.name}")
#
#
# john = Person("john")
# # john.name = "johnny"
# john.talk()
#
# bob = Person('bob')
# bob.name = "bobbert"
# bob.talk()
#
# class Mammal:
#     def walk(self):
#         print("walk")
#
# class Dog(Mammal):
#     def bark(self):
#         print("arf")
#     pass
#
# hughbert = Dog()
# hughbert.walk()
# hughbert.bark()
#
# class Cat(Mammal):
#     def meow(self):
#         print("meow")
#     pass
#
# kimberly = Cat()
# kimberly.walk()
# kimberly.meow()

# from ecommerce.shipping import calc_shipping
# from ecommerce import shipping
#
# shipping.calc_shipping()
# shipping.calc_tax()
# calc_shipping()

# import random
#
# for i in range(3):
#     print(random.randint(10, 20))
#
# members = ['john', 'Mary', 'bob', 'mosh']
#
# leader = random.choice(members)
#
# print(leader)

# import random
#
# class Dice:
#     def roll_two_D6(self):
#         first = random.randint(1,6)
#         second = random.randint(1,6)
#         return first, second
#
# myDice = Dice()
#
# print(myDice.roll_two_D6())


# serialnumber = str(5555)
# print(serialnumber)

from pathlib import Path

#absolute path
#c:\Program Files\Microsoft
#relative path
#/user/local/bin

path = Path()
# print(path.glob('*.py')) #mkdir stands for make directory rmdir for removing it
for file in path.glob('*.py'):
    print(file)

