#LeetCode 242. Valid Anagram
# Easy

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

s = "anagram" 
t = "nagaram"
#Return true

def isAnagram(self, s: str, t: str) -> bool:
        
        map1 = {}
        map2 = {}
        
        for ch in s:
            if ch not in map1:
                map1[ch] = 1
            elif ch in map1:
                map1[ch]+=1
        
        for ch in t:
            if ch not in map2:
                map2[ch] = 1
            elif ch in map2:
                map2[ch] +=1
        
        if map1 ==  map2:
            return True
        else:
            return False