"""
50. Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

"""
x = 2.00000
n = 10
def myPow(self, x: float, n: int) -> float:
    if n == 0 :
        return 1
    else:
        return x**n
    return myPow(x, n-1)