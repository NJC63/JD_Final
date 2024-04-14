import functions

import pandas as pd


# # testing the sorted() function
# list = ["a", "c", "z", "p", "d", "b", "o", "i", "q", "t", "g", "s", "r", "u", "j", "k", "v", "e", "f", "w", "x", "n", "y", "l", "h", "m"]
# sorted_list = sorted(list)
# print(sorted_list)


# # testing floor division
# print(10 // 2)
# print(10 // 3)
# print(10 // 4)


# # testing array equality
# array = [1, 2, 3, 4]
# x = 3

# print(x == array[0])


# # testing binary_search for strings
# print(binary_search.binarySearch_strings(array, 1))


# testing binsearch
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
words = ["a", "b", "c", "d", "e"]

print(functions.binSearch(nums, 0))

print(functions.binSearch(words, "d"))



# testing working with csv files
file = pd.read_csv("cities.csv")
headers = file.columns

print(headers)