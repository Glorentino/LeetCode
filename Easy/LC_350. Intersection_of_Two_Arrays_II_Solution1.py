"""
350. Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

"""

def intersect(self, nums1, nums2):
    lit = []
    for num in range(len(nums1)):
        if nums1[num] in nums2:
            lit.append(nums1[num])
            nums2.remove(nums1[num])
    return lit