"""
1207. Unique Number of Occurrences
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique, or false otherwise.

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

"""    
arr = [1,2,2,1,1,3]

def uniqueOccurrences(arr) -> bool:
        map1 = {}
        lit = []
        for i,v in enumerate(arr):
            if v not in map1:
                map1[v] = 1
            elif v in map1:
                map1[v] += 1
        
        for i in map1:
            if map1[i] not in lit:
                lit.append(map1[i])
            elif map1[i] in lit:
                return False
        return True 