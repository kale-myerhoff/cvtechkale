from string import capwords

weight = input("what is your weight? ")
unit = input("(L)bs or (K)g ")

if capwords(unit) == "L" :
    weight = int(weight) * 0.45359237
    total =f"you are {weight} kilograms"
elif capwords(unit) == "K" :
    weight = int(weight) * 2.20462
    total =f"you are {weight} pounds"
else:
    total = "error please only respond in L or K for unit"

print(total)



