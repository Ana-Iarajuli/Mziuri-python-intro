# # num1 = int(input("Enter a num1:"))
# # num2 = int(input("Enter a num2:"))
# # x = min(num1, num2)
# # for i in range(1, x + 1):
# #     if num1 % i == 0 and num2 % i == 0:
# #         print(i)
#
# #
# # num = int(input("enter Any number:"))
# # if num > 1:
# #     for i in range(2, int((num ** 0.5)) + 1):
# #         if num % i == 0:
# #             print("arari martivi")
# #             break
# #     else:
# #         print("martivia")
# #
# # else:
# #     print("araris martivi")
#
# num=int(input("num"))
# divisors=0
#
# for i in range(1,num +1):
#     if num % i == 0:
#         divisors +=1
#
# if divisors > 2:
#     print(f"{num} araa martivi")
# else:
#     print(f"{num} martivia")




# num1 = int(input("enter a first number: "))
# num2 = int(input("enter a second number: "))
# x = min(num1, num2)
# gcd = 1
# for i in range(1, x + 1):
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i
# print(f"saerto gamyofia {gcd}")


# num1 = int(input("Enter the first positive number: "))
# num2 = int(input("Enter the second positive number: "))
#
# max_num = max(num1, num2)
# min_num = min(num1, num2)
#
# while min_num:
#     max_num, min_num = min_num, max_num % min_num
#     # max_num = min_num
#     # min_num = max_num % min_num
#
# print(f"The greatest common divisor is: {max_num}")

# num1 = int(input("Enter the first positive number: "))
# # num2 = int(input("Enter the second positive number: "))
# #
# # max_num = max(num1, num2)
# # min_num = min(num1, num2)
# #
# # lcm = max_num
# #
# # for i in range(1, min_num + 1):
# #     if (lcm * i) % min_num == 0:
# #         lcm = lcm * i
# #         break
# #
# # print(f"The least common multiple is: {lcm}")

# 5. შეიყვანეთ 10 რიცხვი ციკლის გამოყენებით. იპოვეთ რიცხვებს შორის უდიდესი კენტი რიცხვი
# და დაბეჭდეთ. თუ კენტი რიცხვი არ შეგხვდათ, გამოიტანეთ შესაბამისი შეტყობინება.

# max_odd = 0
# for i in range(10):
#     x = int(input("enter the number: "))
#     if x % 2 != 0 and x > max_odd:
#         max_odd = x
# if max_odd != 0:
#     print(max_odd)
# else:
#     print("ciklshi kenti ricxvi araa")


# sum_total = 0
# x = 1
# count = 0
#
# while count < 20:
#     sum_total += x
#     x += 2
#     count += 1
#
# print(sum_total)

# n = 0
# while n < 100:
#     n += 1
#     if n % 5 == 0:
#         continue
#     print(n)

# 5.	დაწერეთ პროგრამა for ციკლის გამოყენებით, რომელიც
# ბეჭდავს ლუწ რიცხვებს 1-დან 30-მდე. გამოიყენეთ continue კენტი რიცხვების გამოსატოვებლად. (15 ქულა)


# for i in range(1, 30, 1):
#     if i % 2 != 0:
#         continue
#     print(i)


# x = int(input("semoiyvanet pirveli ricxvi: "))
# y = int(input("semoiyvanet pirveli ricxvi: "))
# if x > y:
#     print(f"maqsimaluri ricxvia {x}")
# else:
#     print(f"maqsimaluri ricxvia {y}")




