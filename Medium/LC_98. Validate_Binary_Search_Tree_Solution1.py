"""
98. Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

"""
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, low=-math.inf, high=math.inf):
            if not root:
                return True
            if root.val <= low or root.val >= high:
                return False
            return helper(root.right,  root.val, high) and helper(root.left, low, root.val)  
        
        return helper(root)
         