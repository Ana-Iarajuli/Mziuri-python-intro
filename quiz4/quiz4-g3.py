# with open("titanic.txt", 'r') as f:
#     female_quantity = 0
#     passenger_quantity = -1
#     male_quantity = 0
#     f_survive = 0
#     sum = 0
#     deaths = 0
#
#     for i in f:
#         monacemebi = i.split(",")
#         passenger_quantity += 1
#         if monacemebi[5] != "Age":
#             sum += float(monacemebi[-3])
#
#         if monacemebi[4] == "female":
#             female_quantity += 1
#             if monacemebi[1] == '1':
#                 f_survive += 1
#
#         if monacemebi[4] == "male":
#             male_quantity += 1
#
#         if monacemebi[1] == "0":
#             deaths += 1
#
#     print(sum / passenger_quantity)
#     print(female_quantity)
#     print(male_quantity)
#     print((f_survive/female_quantity)*100,'% survived')
#     print(passenger_quantity)
#     print(deaths)
#
#
#
# dict = {
#     "females": female_quantity,
#     "passengers": passenger_quantity
# }
#
# print(dict)


# class Ticket:
#     def __init__(self, title, price, ticket, language="geo"):
#         self.title = title
#         self.price = price
#         self.ticket = ticket
#         self.language = language
#
#     def __str__(self):
#         return f"title: {self.title}, price: {self.price}"
#
#     def __lt__(self, other):
#         return self.ticket_left > other
# 
#
# class User:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance
#
#     def __str__(self):
#         return f"name: {self.name}, balance: {self.balance}"
#
#     def deposit(self, tanxa):
#         return self.balance + tanxa


















