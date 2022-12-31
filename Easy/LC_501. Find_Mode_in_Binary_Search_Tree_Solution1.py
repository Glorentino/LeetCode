"""
501. Find Mode in Binary Search Tree

Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

If the tree has more than one mode, return them in any order.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

"""

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        hashMap = {}
        list1 = []
        def dfs(root):
            if not root:
                return [0]
            if root.val not in hashMap:
                hashMap[root.val] = 1
            else:
                hashMap[root.val] += 1
        
            return dfs(root.left) and dfs(root.right)
        dfs(root)
        for i, x in hashMap.items():
            if list1 == []:
                list1.append(i)
                list1.append(x)
            elif x == list1[-1]:
                list1.append(i)
                list1.append(x)
            elif x > list1[-1]:
                list1 = []
                list1.append(i)
                list1.append(x)
        if len(list1) <= 2:
            list1.pop(1)
        else:
            for i in range(len(list1)-1, -1, -1):
                if i%2==1:
                    list1.pop(i)
        return list1