#LeetCode 905. Sort Array By Parity
# Easy

#Input: nums = [3,1,2,4]
#Output: [2,4,3,1]
#Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

nums = [3,1,2,4]

def sortArrayByParity(self, nums):
    nums1 = []
    for i in nums:
        if i%2==0:
            nums1.insert(0, i)
        else:
            nums1.append(i)
    return nums1