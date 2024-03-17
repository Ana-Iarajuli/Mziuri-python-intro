# # # heh = set({1, 2, 3})
# # # print(heh)
# # #
# # # my_set = set([1,3,2])
# # # my_set.add(5)
# # # print(my_set)
# # #
# # # my_set = set([1,3,2])
# # # my_set.update([12,19])
# # # print(my_set)
# # # my_set.update([4,5], {1,6,8})
# # # print(my_set)
# # #
# # # A = {1, 2, 3, 4, 5}
# # # B = {4, 5, 6, 7, 8}
# # # C = A ^ B
# # # print(C)
# # #
# # #
# # def reverse_word(a):
# #     b = a.split()
# #     n=[]
# #     for i in b:
# #         c = i[::-1]
# #         n.append(c)
# #     m=" ".join(n)
# #     return m
# #
# #         # print(c)
# #
# # print(reverse_word("nanebi gvinda"))
# #
# #
# #
# # print(ord("A"), ord("B"))
# #
#
# # def reverse_words(a):
# #     b = a.split()
# #     y = []
# #     for i in b:
# #         x = i[::-1]
# #         y.append(x)
# #     z = " ".join(y)
# #     return z
# # print(reverse_words("araferze shemtkiva guli"))
#
#
#  # ლექსიკონის შექმნა
#  # empty dictionary
# my_dict = {}
#
#  # dictionary with integer keys
# my_dict = {[1, 2, 3]: 'apple', 2: 'ball'}

# # dictionary with mixed keys
# my_dict = {'name': 'John', 1: [2, 4, 3]}
#
# students = {'John': 'A', 'Ann': 'B', 'Giorgi': 'A'}
# print(students)
#
# students = {'John':'A', 'Ann':'B', 'Giorgi':'A' }
#
# for i in students.items():
#     print(i)
# students.clear()
# print(students)
#
# squares = {1: 1, 9: 81, 3: 9, 7: 49}
# print(type(squares.keys()))
# print(squares.keys())
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict['b'])


# myfamily = {
#   "jasu" : {"name" : "Emil","year" : 2004},
#   "beki" : {"name" : "Tobias", "year" : 2007},
# }
# myfamily.clear()
# print(myfamily)

# print(myfamily["jasu"])
# # print(myfamily.get("jasur", "jasu ar aris chventan otaxshi"))
# myfamily["levani"] = "rodis damtavrdeba es mosawyeni gakvetili"
# print(myfamily["levani"])

# print(myfamily["jasu"])
# print(myfamily["mike"])

# sia = [1, 2, 3]
# print(sia[0])
#
# erekle = {"erekle": {"qvizi1": 100, "qvizi2": 100}}
# erekle2 = {"erekle": 100}
# print(erekle)
# # print(erekle2)
#
#
# dict1 = {'საჭმელი': {'ხინკალი': 99, 'ხაში': 0}, 8: 16}
# print(dict1)
# def average(*args):
#     return(sum(args)/len(args))
#
# res1 = average(4,6,8)
# print(res1)
# res2 = average(5, 16, 3, 12)
# print(res2)
# res3 = average(4, 7, 1, 10, 26, 30)
# print(res3)









# def average_numbers(*args):
#     return sum(args)//len(args)
#
# print(average_numbers(23,4,124,3214,123,4,342,6,23451,32,4))
# print(average_numbers(23,4,3214,123,4,342,6,23451,32,4))
















students = {
    "Alice": {"Math": 85, "Science": 90},
    "Bob": {"Math": 75, "History": 80}
}


def add_student(students, name, grades):
    pass

def update_grade(students, name, subject, grade):
    pass

def calculate_average(students, name):
    pass

# 4.
def display_student(students, name):
    pass



print("Options:")
print("1. Add Student")
print("2. Update Grade")
print("3. Display Student Information")
print("4. Calculate Average Grade")
print("5. Exit")
choice = input("Enter your choice: ")

if choice == "1":
    pass
elif choice == "2":
    pass








