# 3
# num = []
# for i in range(10):
#     x = int(input("Enter the number: "))
#     num.append(x)
# print(num)        # სახე გაეძრო ეგრევე!!!

# 4
# fruits = ["orange", "grape", "watermelon", "banana", "apple"]
# fruits.sort()
# fruits.reverse()
# print(fruits)

# 5
# x = [1, 3, 5132, 723, 612, 631124, 13, 13, 331, 837, 2939]
# for i in x:
#     if i % 2 != 0:
#         x.remove(i)
# print(x)

# x = [1, 3, 5132, 723, 612, 631124, 13, 13, 331, 837, 2939]
# x = [num for num in x if num % 2 == 0]
# print(x)


# t = list(range(1, 40, 2))
# print(t)
#
# nums = []
# for i in range(1, 40):
#     if i % 2 != 0:
#         nums.append(i)
# print(nums)

# s = "I lovekhinkali more than mtsvadi"
# t = s.split()
# print(t)

# s = "spam-text-here"
# delimiter = " "
# t = s.split(delimiter)
# print(t)


# t = ['Good', 'Morning', 'Everyone']
# delimiter = ''
# s = delimiter.join(t)
# print(s)

# t = [4, 5, 7, 8]
# p = (4, 5, 7, 8)
# s = 4, 5, 7, 8
# print(type(t))
# print(type(p))
# print(type(s))
# double1 = []
# for i in range(10):
#     if i % 2 == 1:
#         double1.append(i * i)
# print(double1)

double = [i*i for i in range(10) if i % 2 == 1]
print(double, "shaurma", "maswavlebelma daigviana fu")
