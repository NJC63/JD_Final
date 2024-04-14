# def binarySearch_strings(array, x):
#     i = 0
#     length = len(array)

#     while(i <= length):
#         midpoint = i + ((length - 1) // 2)

#         if(x == array[midpoint]):
#             return midpoint
        
#         elif(x > array[midpoint]):
#             i = midpoint + 1

#         else:
#             length = midpoint - 1
#     return -1


def binSearch(sorted_list, target):
    min = 0
    max = len(sorted_list) - 1

    while(min <= max):

        midpt = (min + max)//2

        if(sorted_list[midpt] == target):
            return midpt
        elif(sorted_list[midpt] > target):
            max = midpt - 1
        elif(sorted_list[midpt] < target):
            min = midpt + 1
    return -1   

    
