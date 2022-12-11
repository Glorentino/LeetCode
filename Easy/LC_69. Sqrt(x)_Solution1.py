"""
69. Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

"""

def mySqrt(self, x: int) -> int:
    if x < 2:
        return x
    left, right = 2, x//2

    while left <= right:
        pivot = left + (right - left)//2
        mid = pivot * pivot

        if mid > x:
            right = pivot - 1
        elif mid < x:
            left = pivot + 1
        else:
            return pivot
    return right