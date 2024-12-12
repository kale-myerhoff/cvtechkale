
vowel = ["a", "e", "i", "o", "u", 'y']

sent = input("Enter a sentence: ").lower()
vow_numb = 0
a = 0
e = 0
i = 0
o = 0
u = 0
y = 0

for character in sent:
    if character.lower() in vowel:
        if character.lower() in vowel[0] :
            a += 1
        if character.lower() in vowel[1] :
            e += 1
        if character.lower() in vowel[2] :
            i += 1
        if character.lower() in vowel[3] :
            o += 1
        if  character.lower() in vowel[4] :
            u += 1
        if  character.lower() in vowel[5] :
            y += 1
        vow_numb += 1



print('total number of vowels: ', vow_numb)
print('a = ', a)
print('e = ', e)
print('i = ', i)
print('o = ', o)
print('u = ', u)
print('y = ', y)