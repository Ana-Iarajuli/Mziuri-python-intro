

# pirveli

# def sityvis_sigrze(stringi):
#     return [len(s) for s in stringi]
#
# s=["frfefeferfr","fefrfrfrr"]
# print(sityvis_sigrze(s))
# 10 ქულა




# meore


# def elementebi(list1, list2):
#     set1=set(list1)
#     set2=set(list2)
#
#
#     common_elements=set1.intersection(set2) # განსხვავებული ელემენტები გვინდოდა და არა საერთო
#
#     return list(common_elements)
#
#
# list1=[1,2,3,4,5]
# list2=[1,5,3,7,9]
# print(elementebi(list1,list2))
# 12 ქულა


# mesame

# def mesame(list1):
#     dict1=dict( list1 )
#     return dict1
#
#
# y_list=[("gia", 25), ("goga", 30), ("sani", 22)]
#
# h_dict=mesame( y_list )
#
# for name, age in h_dict.items():
#     print(f"{name}: {age}")
# 25 ქულა - სფეისებია გამოსასწორებელი


# meotxe

# def meotxe(product_dict):
#     tapli = []
#
#     for product, quantity in product_dict.items():
#         status="enough" if quantity >= 5 else "not enough"
#         tapli.append((product,status))
#
#     return tapli
#
#
# products={'ბადრიჯანი': 3, 'ხახვი': 6, 'კომბოსტო': 2}
#
# result= meotxe( products )
#
# for product, status in result:
#    print(f"{product}:{status}")
# 30 ქულა


# mexute


# def mexute(string_list):
#     words_dict={}
#     for word in string_list:
#          if word.startswith('a'):
#              words_dict[word]=len(word)
#     return words_dict
#
#
# my_strings=["apple", "banana","grape", "avocado"]
# result_dict=mexute(my_strings)
#
#
# for word,length in result_dict.items():
#     print(f"{word}:{length}")
# 20 ქულა                                                                    bonusebi
#
# meeqvse
#
# discard( )
# remove( )
# pop( )
#
# meshvide
# სიისგან განსხვავებით
# ელემენტები არაა დალაგებული ინდექსის მიხედვით.
#
# ლექსიკონის ელემენტები მოთავსებულია ფიგურულ ფრჩხილებში
# {} - აქ tuple-სა და სიას შორის განსხვავებაზეა საუბარი და არა ლექსიკონზე
# meerve
# union( )
# intersection( )
# difference( )
# symmetric_difference( )
#
# mecxre
# students = {'John':'A', 'Ann':'B', 'Giorgi':'A' }
# students['Ann']='C'
# print(students)
#
# თუ მითითებული key არ არსებობს, ახალი წყვილი (key:value) ემატება ლექსიკონს.
#
# meate
# items( )
#
# metertmete
# *args
