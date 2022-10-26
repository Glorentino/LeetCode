"""
Given an integer array nums sorted in non-decreasing order and an integer target, return true if target is a majority element, or false otherwise.

A majority element in an array nums is an element that appears more than nums.length / 2 times in the array.

"""
nums = [2,4,5,5,5,5,5,6,6]

target = 5

def isMajorityElement(nums, target: int) -> bool:
    map1 = {}
    for i, v in enumerate(nums):
        if v not in map1:
            map1[v] = 1
        else:
            map1[v] += 1
    x = max(map1.values())
    if target in map1:
        if map1[target] == x and map1[target] > len(nums)/2:
            return True
        else:
            return False
    return False