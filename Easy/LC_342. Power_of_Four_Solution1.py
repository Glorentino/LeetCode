"""
342. Power of Four

Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.

Input: n = 16
Output: true

Input: n = 5
Output: false

"""    

def isPowerOfFour(self, n: int) -> bool:
    if n == 0:
        return False
    if n == 1:
        return True
    if n != int(n):
        return False
    
    return self.isPowerOfFour(n/4)