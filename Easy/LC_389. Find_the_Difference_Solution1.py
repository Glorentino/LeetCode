#LeetCode 389. Find the Difference
# Easy

#Input: s = "abcd", t = "abcde"
#Output: "e"
#Explanation: 'e' is the letter that was added.

def findTheDifference(self, s: str, t: str) -> str:
    t = sorted(t) 
    s = sorted(s)
    x = ""
    for i in t:
        if t.count(i) != s.count(i):
            return i
    return x