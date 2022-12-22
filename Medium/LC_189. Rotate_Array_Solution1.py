"""
189. Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.

"""

def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = 0
    while i < k:
        x = nums.pop()
        nums.insert(0, x)
        i+= 1