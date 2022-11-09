"""
941. Valid Mountain Array

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

"""



def validMountainArray(self, arr) -> bool:
    max1 = max(arr)
    max1ind = arr.index(max1)
    up = False
    down = False
    if len(arr) >= 3:
        if arr[0] == max1:
            return False
        for i in range(1,max1ind+1):
            print(arr[i])
            if arr[i-1] > arr[i] or arr[i-1] == arr[i] or i == len(arr)-1:
                return False
            
        up = True
        for i in range(max1ind, len(arr)):
            if arr[i] == max1 and i == max1ind:
                continue
            elif arr[i-1] < arr[i] or arr[i-1] == arr[i] :
                return False
        down = True
        return up == down
