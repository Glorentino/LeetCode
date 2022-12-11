"""
162. Find Peak Element

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
"""

def findPeakElement(self, nums) -> int:
    if len(nums) == 1:
        return 0
    low, high = 0, len(nums)-1
    bound_ind = float('-inf')
    while low <= high:
        mid = (low + high)//2
        if nums[mid] >= nums[high]:
            bound_ind = mid
            high -= 1
        else:
            low += 1
    return bound_ind