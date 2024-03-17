# a = int(input("ricxvi: "))
# b = int(input("ricxvi: "))
# gamyofi = 0
#
# for gamyofi in range(0, a):
#     gamyofi += 1
#     if a % gamyofi == 0 and b % gamyofi == 0:
#         print(gamyofi)

#
# max = 0
# number1 = int(input("put number"))
# number2 = int(input("put number"))
# for x in range(1, number1 + 1):
#     if number1 % x == 0 and number2 % x == 0:
#         max = x
# print(max)


# num1 = int(input("Enter the first positive number: "))
# num2 = int(input("Enter the second positive number: "))
#
# min_num = min(num1, num2)
# gcd = 1
# for i in range(2, min_num + 1):
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i
#
# print(f"The greatest common divisor is: {gcd}")

# num1 = int(input("num1: "))
# num2 = int(input("num2: "))
# while num2:
#     num1, num2 = num1, num2 % num2
# print(num1)
# x = 0
# b = int(input())
# c = int(input())
# min_num = max(b,c)
# for y in range(1, min_num + 1):
#     if b % y == 0 and c % y == 0:
#         x = max(range(1,y+1))
# print((b * c)/x)



# num1 = int(input("Enter the first positive number: "))
# num2 = int(input("Enter the second positive number: "))
#
# max_num = max(num1, num2)
# min_num = min(num1, num2)
#
# lcm = max_num
#
# for i in range(1, min_num + 1):
#     if (lcm * i) % min_num == 0:
#         lcm = lcm * i
#         break
#
# print(f"The least common multiple is: {lcm}")


# biggest_odd = 0
#
# for i in range(10):
#     num = int(input(f"enter num {i}: "))
#
#     if num % 2 != 0 and num > biggest_odd:
#         biggest_odd = num
#
# if biggest_odd:
#     print(biggest_odd)
# else:
#     print("no odd numbers")

#
# num = int(input("Enter a number: "))
#
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print(f"{num} is not a prime number.")
#             break
#     else:
#         print(f"{num} is a prime number.")
# else:
#     print(f"{num} is not a prime number.")

# sum_odd = 0
# for x in range(1, 40):
#     if x % 2 != 0:
#         sum_odd += x
# print(sum_odd)
#
# x=0
# sum_odd1 = 0
# while x < 40:
#     x += 1
#     if x % 2 != 0:
#         sum_odd1 += x
# print(sum_odd1)

# count = 0
# sum_odd = 0
# current_number = 1
#
# while count < 20:
#     sum_odd += current_number
#     current_number += 2
#     count += 1
#
# print("The sum is:", sum_odd)
#
# count = 0
# kenti = 0
# jami = 0
# while count < 40:
#     count +=1
#     kenti +=1
#     if kenti % 2 != 0:
#         jami += kenti
# print(jami)

# n = 0
# while n < 100:
#     n += 1
#     if n % 5 == 0:
#         continue
#     print(n)



# for x in range(1, 30):
#     if x % 2 != 0:
#         continue
#     print(x)



# count = 0
# sum_odd = 0
# current_number = 1
#
# while count < 20:
#     sum_odd += current_number
#     current_number += 2
#     count += 1
#
# print("The sum is:", sum_odd)





# x = int(input("shemoitane ricxvi: "))
# y = int(input("shemoitane ricxvi: "))
# if x > y:
#     print(f"max aris {x}")
# else:
#     print(f"max aris {y}")

# x = 5
# print(f"x aris {x}")


num = 1
for x in range(1, 10):
    if x % 2 == 1:
        num = max(x, num)
print(num)

file1 = open("C:\Users\Artemis\PycharmProjects\Mziuri1\Homework 5", "")



