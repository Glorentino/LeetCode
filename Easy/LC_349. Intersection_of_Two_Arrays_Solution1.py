"""
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
"""



def intersection(nums1, nums2):
    nums1,nums2 = set(nums1), set(nums2)
    lit = []
    for num in nums1:
        if num in nums2:
            lit.append(num)
    return lit