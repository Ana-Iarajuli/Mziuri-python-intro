# f_survived = 0
# all = 0
# first_class = 0
# female_quantity = 0
# average = 0
# with open("titanic.txt", "r") as f:
#     next(f)
#     for line in f:
#         all += 1
#         info = line.split(",")
#         average += float(info[-3])
#         if info[4] == "male":
#             if info[1] == "1":
#                 f_survived += 1
#             female_quantity += 1
#         if info[2] == "1":
#             first_class += 1
#
# print(round(female_quantity / all * 100))
# print(round(f_survived / female_quantity * 100))
# print(first_class)
# print(average/ all )
#
#

class Ticket:
    def __init__(self, title, price, quantity, language = "Geo"):
        self.title = title
        self.price = price
        self.quantity = quantity
        self.language = language

    def __str__(self):
        return f"title: {self.title}, price: {self.price}"

    def __lt__(self, other):
        if self.quantity > other:
            return f"{self.title} is more than {other}"
        


class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"name: {self.name}, balance: {self.balance}"

    def deposit(self, money):
        self.balance += money

    def get_balance(self):
        return self.balance


user1 = User("Jasu", 89)
user1.deposit(11)
print(user1.get_balance())