"""
599. Minimum Index Sum of Two Lists

Given two arrays of strings list1 and list2, find the common strings with the least index sum.

A common string is a string that appeared in both list1 and list2.

A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.

Return all the common strings with the least index sum. Return the answer in any order.
"""
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        list3 = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if list3 == []:
                        list3.append(list1[i])
                        list3.append(i+j)
                    elif i+j == list3[-1]:
                        list3.append(list1[i])
                        list3.append(i+j)
                    elif i+j < list3[-1]:
                        list3 = []
                        list3.append(list1[i])
                        list3.append(i+j)

        for i in range(len(list3)-1, -1, -1):
            if i%2==1:
                list3.pop(i)

        return list3