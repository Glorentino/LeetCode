"""
374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

"""

def guessNumber(self, n: int) -> int:
    low = 0
    high = n
    while low <= high:
        mid = (high+low) // 2
        res = guess(mid)

        if res == 1:
            low = mid + 1
        elif res == 0:
            return mid     
        elif res == -1:
            high = mid - 1