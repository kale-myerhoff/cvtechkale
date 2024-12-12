import random

uppercase = "abcdefghijklmnopqrstuvwxyz".upper()
lowercase = "abcdefghijklmnopqrstuvwxyz".lower()
digits = "0123456789"
symbols = "()[]{},;:.-_/\\?+*#!@$%^&="

lengthCheck= False
amountCheck= False

upper, lower, nums, syms = True, True, True, True


all = ""

if upper:
    all += uppercase
if lower:
    all += lowercase
if nums :
    all += digits
if syms :
    all += symbols

password = ('')
while lengthCheck == False:
    passwordLength = int(input("Choose a password length from 1 to 100> "))
    try:
        if passwordLength >= 1 and passwordLength<= 100:
            print(passwordLength)
            lengthCheck = True
        else: print('please select a valid number')
    except ValueError:
     print('please select a number')

while amountCheck == False:
    passwordAmount = int(input("Choose the amount of passwords from 1 to 100> "))
    try:
        if passwordAmount >= 1 and passwordAmount<= 100:
            print(passwordAmount)
            amountCheck = True
        else:
            print('please select a valid number')
    except ValueError:
        print('please select a valid number')

for x in range(passwordAmount):
    for y in range(passwordLength):
        password += random.choice(all)
    print(password)
    password= ""
