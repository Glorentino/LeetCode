"""
599. Minimum Index Sum of Two Lists

Given two arrays of strings list1 and list2, find the common strings with the least index sum.

A common string is a string that appeared in both list1 and list2.

A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.

Return all the common strings with the least index sum. Return the answer in any order.
"""
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        dic = {}
        lit = []
        for ind, string in enumerate(list1):
            if string in list2:
                dic[string] = ind
        
        for ind, string in enumerate(list2):
            if string in dic:
                dic[string] += ind
        
        for string, ind in dic.items():
            if lit == []:
                lit.append(string)
                lit.append(ind)
            elif ind == lit[-1]:
                lit.append(string)
                lit.append(ind)
            elif ind < lit[-1]:
                lit = []
                lit.append(string)
                lit.append(ind)
        for i in range(len(lit)-1, -1, -1):
            if i%2==1:
                lit.pop(i)
        
        return lit