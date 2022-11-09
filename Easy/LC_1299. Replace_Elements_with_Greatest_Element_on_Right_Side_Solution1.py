"""
1299. Replace Elements with Greatest Element on Right Side

Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.


"""

arr = [17,18,5,4,6,1]


def replaceElements(self, arr):
    if len(arr) == 1:
        return [-1]
    for i in range(1,len(arr)):
        arr[i] = max(arr[i:])
    arr.pop(0)
    arr.append(-1)
    return arr