"""
136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

"""

def singleNumber(self, nums) -> int:
    for i in range(len(nums)):
        if nums.count(nums[i])==1: 

            
            return nums[i]