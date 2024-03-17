# squares = {1: 1, 9: 81, 3: 9, 7: 49}
# print(squares.keys())
#
# for i in squares.keys():
#     print(i)

squares = {1: 1, 9: 81, 3: 9, 7: 49}
print(squares.items())

for key, value in squares.items():
    print(key, value)

dict1 = {1: 1, 9: 81, 3: 9, 7: 49}
dict2 = {2: 4, 6: 36}
dict1.update(dict2)
print(dict1)
dict1.update({8: 64})
print(dict1)