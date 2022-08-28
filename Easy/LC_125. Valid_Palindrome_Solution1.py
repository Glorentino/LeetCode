#LeetCode 21. Merge Two Sorted Lists
# Easy

#A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. 
# Alphanumeric characters include letters and numbers.
#If target exists, then return its index. Otherwise, return -1.

#Given a string s, return true if it is a palindrome, or false otherwise.

s = "A man, a plan, a canal: Panama"

def isPalindrome(s):
    str1 = ""
    for i in s:
        if i.isalnum():
            str1 += i.lower()
    str2 = str1[::-1]
    
    if str2 == str1:
        return True
    else:
        return False