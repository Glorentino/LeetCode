"""
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""

def firstUniqChar(self, s: str) -> int:
    
    for i in s:
        if s.count(i) == 1:
            return s.index(i)
        
    return -1
    