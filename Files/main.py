# 1
# file1 = open("exercise1.txt", "w")
# file1.write("this is exercise 1 and i already hate it")
# file1.close()


#2
# file1 = open("exercise1.txt", "r")
# content = file1.read()
# print(len(content))
# file1.close()


#3
# file1 = open("exercise1.txt", "a")
# file1.write("this is added text")
# file1.close()


#4
# file1 = open("exercise1.txt", "r") # შეამოწმე ეს ვერსიაც
# file1 = open("exercise1.txt", "r", encoding="utf-8")
# content = file1.read()
# file2 = open("copyFile.txt", "w", encoding="utf-8")
# file2.write(content)
# file1.close()
# file2.close()


#5
# file1 = open("exercise1.txt", "r", encoding="utf-8")
# file2 = open("copyFile.txt", "r", encoding="utf-8")
# content1 = file1.read()
# content2 = file2.read()
# content = content1 + content2
#
# file3 = open("unionFile.txt", "w", encoding="utf-8")
# file3.write(content)
#
# file1.close()
# file2.close()
# file3.close()


# with open("exercise1.txt", "r", encoding="utf-8") as file1:
#     content1 = file1.read()
#
# with open("copyFile.txt", "r", encoding="utf-8") as file2:
#     content2 = file2.read()
#
# content = content1 + "\n" + content2
# with open("unionFile.txt", "w", encoding="utf-8") as file3:
#     file3.write(content)


#6
# with open("exercise1.txt", "r", encoding="utf-8") as file1:
#     content = file1.read()
#
# print(content.upper())


#7
# with open("data.txt", "w") as file1:
#     while True:
#         text = input("Enter any text (0 to exit): ")
#         if text == "0":
#             break
#         file1.write(text + "\n")


#9
# file = open('data.txt', 'r')
#
# lines = 0
# words = 0
# symbols = 0
# 
# for each in file:
#     word = each.split()
#     lines += 1
#     words += len(word)
#     symbols += len(each)
#
# file.close()
# print(lines, words, symbols)


# with open('data.txt', 'r') as file:
#     lines = 0
#     words = 0
#     symbols = 0
#
#     for line in file:
#         lines += 1
#         words += len(line.split())
#         symbols += len(line)
#
# print(lines, words, symbols)




# file = open("ana.txt", "w")
# file.write("rodis damtavrdeba es gakvetili")
# file.close()

# file = open("ana.txt", "r")
# content = file.read()
# print(content)
# file.close()


# with open("ana.txt", "r") as file:
#     for line in file:
#         print(line)

# data_file = "C:/Users/Artemis/PycharmProjects/Mziuri1/functions/new.txt"
# file = open(data_file, "r")
# content = file.read()
# file.close()
#
# file2 = open("ana.txt", "a+")
# file2.write("\n" + content)
# file2.close()
# file2 = open("ana.txt", "a+")
# content2 = file2.read()
# print(content2)



#A)
# file1 = open('clients.txt', 'r')
# file2 = open('SpainAndGermany.txt', 'w')
# born_2011 = []
# country = {'i'}
#
# for each in file1:
#     eachPart = each.split(';')
#     if eachPart[2] == 'Germany' or eachPart[2] == 'Spain':
#         file2.write(eachPart[0] + '\n')
# #B)
#     if "2011" in eachPart[3]:
#         born_2011.append(eachPart[1])
# # #C)
#     country.add(eachPart[2])
#     country.discard('i')
# print(list(country))
#
# print(born_2011)
#
# file2.close()


