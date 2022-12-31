"""
108. Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.

"""
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        def helper(nums, low, high):
            if low > high:
                return None
            mid = (low + high)//2
            root = TreeNode(nums[mid])
            root.left = helper(nums, low, mid-1)
            root.right = helper(nums, mid+1, high)
            return root
        
        return helper(nums, 0, len(nums)-1)