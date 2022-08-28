#LeetCode 242. Valid Anagram
# Easy

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.

nums = [2,7,11,15]
target = 9

def twoSum(nums, target):
    
    map1 = {}
    for index,val in enumerate(nums):
        map1[val] = index
    
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in map1:
            if i != map1[diff]:
                return [i, map1[diff]]