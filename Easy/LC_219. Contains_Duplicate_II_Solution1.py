"""
219. Contains Duplicate II

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

"""
nums = [1,2,3,1]
k = 3
def containsNearbyDuplicate(self, nums, k) -> bool:
        
    checker = {}
    for i, x in enumerate(nums):
        if x in checker and abs(i-checker[x]) <= k:
            return True
        checker[x] = i