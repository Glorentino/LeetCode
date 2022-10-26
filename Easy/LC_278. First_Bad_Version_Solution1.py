#278. First Bad Version
# Easy

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def isBadVersion(n):
        if n:
            return True # No part of the solution

    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n
        x = 0
        while low <= high:
            mid = (low + high) // 2
            if self.isBadVersion(mid) == True:
                x = mid
                high = mid - 1
            else:
                low = mid + 1
        return x