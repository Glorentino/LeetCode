"""
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

"""



def arraysIntersection(arr1, arr2, arr3):
    arr = []
    for i in arr1:
        if i in arr2 and i in arr3:
            arr.append(i)
    return arr

arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]


arraysIntersection(arr1, arr2, arr3)