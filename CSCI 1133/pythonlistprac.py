import math, turtle

def product_of_list(myList):
    sum = 1
    for val in myList:
        sum *= val
    return sum

def secondsmallest(numList):
    numList.sort()
    return numList[1]