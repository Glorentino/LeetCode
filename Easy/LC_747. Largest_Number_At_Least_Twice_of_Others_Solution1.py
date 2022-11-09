"""
747. Largest Number At Least Twice of Others

You are given an integer array nums where the largest integer is unique.

Determine whether the largest element in the array is at least twice as much as every other number in the array. If it is, return the index of the largest element, or return -1 otherwise.
"""


nums = [3,6,1,0]

def dominantIndex(self, nums) -> int:
    maxNum = max(nums)
    for i in nums:
        if i != maxNum and i+i > maxNum:
            return -1
    return nums.index(maxNum)