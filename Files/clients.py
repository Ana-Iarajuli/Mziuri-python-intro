# 1
# f1 = open("clients1.txt", "w")
# with open("clients.txt", "r") as f:
#     for i in f:
#         ragaca = i.split(";")
#         if ragaca[2] == "Germany" or ragaca[2] == "Spain":
#             f1.write(ragaca[0] + "\n")



# 2
# meilebi = []
# with open('clients.txt', 'r') as s:
#     for line in s:
#         a = line.strip()
#         info = a.split(';')
#         meili = info[1]
#         tarigi = info[3]
#         trg2 = tarigi.split('/')
#         if trg2[2] == '2011':
#             meilebi.append(meili)
# print(meilebi)



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


#1
# countries = set()
# emails = []
# f_w = open("clients5.txt", "w")
# with open("clients.txt", "r") as f:
#     for i in f:
#         splited_line = i.split(";")
#         if "Germany" in splited_line or "Spain" in splited_line:
#             f_w.write(splited_line[0] + "\n")
#         if "2011" in splited_line[-1]:
#             emails.append(splited_line[1] + "\n")
#         countries.add(splited_line[2])
# result = list(countries)
# print(sorted(result))
#
# f_w.close()
# print(emails)









