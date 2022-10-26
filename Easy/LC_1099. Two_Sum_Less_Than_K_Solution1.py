"""1099. Two Sum Less Than K
    Given an array nums of integers and integer k, 
    return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. 
    If no i, j exist satisfying this equation, return -1.
"""
nums = [34,23,1,24,75,33,54,8]
k = 60


def twoSumLessThanK(nums, k: int) -> int:
    nums = sorted(nums)
    sums = -1
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]  + nums[j] < k and nums[i] + nums[j] > sums:
                sums = nums[i]  + nums[j]
    return sums