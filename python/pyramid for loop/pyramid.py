import math
from math import floor

user_number = int(input("choose a number greater than 1 > "))
#
output = "1"
space_number= user_number
space = " " * space_number

print(space   +output+ space)
for x in range(2, user_number+1):



    space_number -= 1

    space = " " * space_number

    output =  str(x) + output +str(x)
    print(space +output+ space)









# pyramid_list = []
#
# if user_number >= 3 and user_number <= 10:
#     print(user_number)
#     i=0
#     while i < user_number:
#         i += 1
#
#         if i == 1:
#             pyramid_list.append(i)
#             print(pyramid_list)
#         else:
#             pyramid_list.append(i)
#
#             pyramid_list.insert(0, i)
#             print(pyramid_list)
