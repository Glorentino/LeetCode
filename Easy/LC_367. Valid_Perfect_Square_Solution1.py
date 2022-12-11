"""
367. Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

"""

def isPerfectSquare(self, num: int) -> bool:

    low = 1
    high = num
    while low <= high:
        mid = low + (high - low)//2

        if mid == num**.5:
            return True
        if mid > num**.5:
            high = mid - 1
        else:
            low = mid + 1
    return False