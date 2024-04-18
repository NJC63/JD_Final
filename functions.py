import pandas as pd

def binarySearch(sorted_list, target):
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


def clean(raw_df):

    column_names = raw_df.columns.values.tolist()


    return 1
    
def zipsInOrder(zip):
    zip = str(zip)
    zip.rsplit("-")
    initial = original_list[0][0]
    final = original_list[0][1]

    count = initial
    i = 1
    final_list = [initial, final]
    while(count < final):
        count = count + 1
        final_list.insert(i, count)
        return final_list
    return zip
    

