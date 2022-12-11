"""
154. Find Minimum in Rotated Sorted Array II

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.

"""

def findMin(self, nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    low, high = 0, len(nums)-1
    bound_inx = 0

    while low <= high:
        mid = (low + high) //2
        if nums[high] >= nums[mid]:
            bound_inx = nums[mid]
            high -= 1
        else:
            low += 1
    return bound_inx