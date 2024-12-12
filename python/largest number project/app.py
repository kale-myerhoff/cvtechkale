from random import randint

numbers = [randint(1, 100), randint(1, 100),randint(1, 100),randint(1, 100)]
print(numbers)
max = numbers[0]
for x_count in numbers :
     if max < x_count :
        max = x_count

print(max)



