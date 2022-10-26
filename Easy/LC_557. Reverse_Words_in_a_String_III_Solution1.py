"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

"""
s = "Let's take LeetCode contest"

def reverseWords(self, s: str) -> str:
    sList = list(s.split())
    for i in range(len(sList)):
        sList[i] = sList[i][::-1]
    return " ".join(sList)