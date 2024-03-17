# 1
squares = [x ** 2 for x in range(1, 11)]


# # 2
# num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# even_squares = [x ** 2 for x in num_list if x % 2 == 0]
#
# # 3
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
#
# common_elements = list(set(list1) & set(list2))
#
# print(common_elements)
#
# # 4
# # Create an empty list 'l'
# l = []
#
# # Check if the list 'l' is empty using the 'not' keyword
# if not l:
#     # If the list is empty, print the message "List is empty"
#     print("List is empty")
#
# # 5
# # Define a function called 'long_words' that takes an integer 'n' and a string 'str' as input
# def long_words(n, str):
#     # Create an empty list 'word_len' to store words longer than 'n' characters
#     word_len = []
#
#     # Split the input string 'str' into a list of words using space as the delimiter
#     txt = str.split(" ")
#
#     # Iterate through each word 'x' in the list of words 'txt'
#     for x in txt:
#         # Check if the length of the current word 'x' is greater than 'n'
#         if len(x) > n:
#             # If the word is longer than 'n' characters, add it to the 'word_len' list
#             word_len.append(x)
#
#     # Return the list of words longer than 'n' characters
#     return word_len
#
# # Call the 'long_words' function with an 'n' value of 3 and a string as input, and print the result
# print(long_words(3, "The quick brown fox jumps over the lazy dog"))
#
#
#
# # t = ['Good', 'Morning', 'Every', 'one']
# # delimiter = ''
# # s = delimiter.join(t[2:])
# # v = delimiter.join()
# # print(s)



numbs = [0, 12, 13, 69, 100]
print(sum(numbs), max(numbs), min(numbs), sum(numbs)/len(numbs), sep="\n")

sum = 0
max = 0
min = 0
for i in range(0, 5):
    sum += numbs[i]
    if numbs[i] > max:
        max = numbs[i]
    if numbs[i] < min:
        min = numbs[i]
print(sum, min, max, sum / 5)
