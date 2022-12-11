"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

"""

def searchRange(self, nums: List[int], target: int) -> List[int]:
    if nums == []:
        return [-1, -1]


    low, high = 0, len(nums)-1
    x = []
    while low <= high:
        mid = (high + low)//2

        if nums[high] == target and nums[low] == target:
            return [low, high]
        if nums[high] > target:
            high -= 1
        elif nums[low] < target:
            low += 1
        
    return [-1, -1]