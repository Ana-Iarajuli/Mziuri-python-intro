#1
# def words_length(words):
#     words_len = []
#     for word in words:
#         words_len.append(len(word))
#     return words_len
#
#
# words_list = ["jasu", "shaurma", "naci"]
# print(words_length(words_list))
#
#
# #2
# # def unique_elems(nums1, nums2):
# #     set1 = set(nums1)
# #     set2 = set(nums2)
# #
# #     unique_elems1 = set1 - set2
# #     unique_elems2 = set2 - set1
# #
# #     unique_elems = list(unique_elems1 | unique_elems2)
# #     return unique_elems
# #
# # list1 = [1, 2, 2, 3, 4]
# # list2 = [3, 4, 5, 6]
# # print(unique_elems(list1, list2))
#
#
# #3
# # def dict_info(arr):
# #     info = {}
# #     for i in arr:
# #         info[i[0]] = i[1]
# #     return info
# #
# # list_of_tuples = [("ana", 21), ("jasu", 22)]
# # print(dict_info(list_of_tuples))
#
#
# #4
# # def product_info(dict):
# #     list_of_tuples = []
# #
# #     for key, value in dict.items():
# #         if value >= 5:
# #             list_of_tuples.append((key, "საკმარისია"))
# #         else:
# #             list_of_tuples.append((key, "არაა საკმარისი"))
# #
# #     return list_of_tuples
# #
# # product_dict = {'ბადრიჯანი': 3, 'ხახვი': 6, 'კომბოსტო': 2}
# # print(product_info(product_dict))
#
#
# #5
# # def a_words_length(words):
# #     word_dict = {}
# #
# #     for word in words:
# #         if word.startswith('a'):
# #             word_dict[word] = len(word)
# #     return word_dict
# #
# #
# # words_list = ["ana", "shaurma", "jasu", "hitleri", "atomuri"]
# # print(a_words_length(words_list))
#
#
#
#
#
# # #1
# # def savarjishoerti(n):
# #     return [len(i) for i in n]
# #
# # a = ["datvi", "spiolo", "nazi", "ragac"]
# # k = savarjishoerti(a)
# # print(k)
#
# # #2
# # def task2(a, b):
# #     set1 = set(a)
# #     set2 = set(b)
# #     c = set1 - set2
# #     d = set2 - set1
# #     return list(c|d)
# # a = [1, 2, 3, 4, 5]
# # b = [4, 5, 6, 7, 8]
# # res = task2(a, b)
# # print(res)
#
# #3
# # def savarjisho3(arr):
# #     result_dict = {}
# #
# #     for i in arr:
# #         result_dict[i[0]] = i[1]
# #     for key,value in result_dict.items():
# #         print(key,value)
# # list1 = [("iva",14),('natia',16)]
# # savarjisho3(list1)
#
#
#
# #4
# # def convert_to_tuple(dict):
# #     list1 = []
# #     for key,value in dict.items():
# #         if value >= 5:
# #             list1.append((key, "enough"))
# #         else:
# #             list1.append((key, "not enough"))
# #     return list1
# #
# # dictionry={
# #     "ბადრიჯანი":0.2546,
# #     "ხახვი":-123,
# #     "კომბოსტო":7,
# # }
# #
# # res=convert_to_tuple(dictionry)
# # print(res)
#
#
# #5
# def savarjisho5(list_of_strings):
#     dict1 = {}
#     for i in list_of_strings:
#         if i.startswith("a"):
#             dict1[i] = len(i)
#     return dict1
#
# strings = ["mwvadi", "ananasi", "atami", "khinkali"]
# res = savarjisho5(strings)
# print(res)
#
#
#
#
#
#
#
#
#
#
