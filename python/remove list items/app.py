from enum import unique
from os import remove

numbers = [5, 2, 1, 5, 7, 4]
uniques = []
# for number in numbers :
#         if numbers.count(number) > 1:
#             numbers.remove(number)


for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

