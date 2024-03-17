num = int(input("Enter an integer: "))
count = 0
temp_num = num

while temp_num > 0:
    temp_num = temp_num // 10
    count += 1

print(f"The number of digits in {num} is: {count}")


#1
# for num in range(2, 1001):
#     is_prime = True
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(num)



#2
# a, b = 0, 1
#
# # for _ in range(12): 12 fibonachis ricxvi gvxvdeba 100-mde
# #     print(a, end=' ')
# #     a, b = b, a + b
#
# while a < 100:
#     print(a, end=' ')
#     a, b = b, a + b

#3
# num = int(input("Enter an integer: "))
# count = 0
# temp_num = num
#
# while temp_num > 0:
#     temp_num = temp_num // 10
#     count += 1
#

# num = int(input("Enter an integer: "))
# count = 0
# pos_num = abs(num)
#
# for digit in str(pos_num):
#     count += 1
#
# print(f"The number of digits in {num} is: {count}")

# for i in "1005":
#     count += 1
#     print(i, end='-')
# print(count)


#4
# num = int(input("Enter an integer: "))
# sum_of_digits = 0
# # #
# # while num > 0:
# #     digit = num % 10
# #     sum_of_digits += digit
# #     num //= 10
# #
# # using for loop
# for digit in str(abs(num)):
#     sum_of_digits += int(digit)
#
# print(f"The sum of digits is: {sum_of_digits}")


#5
# num = input("Enter a number: ")
# num = int(input("Enter a number: "))
#
# for digit in str(num): #"123"
#     print(f"The first digit is: {digit}")
#     break
