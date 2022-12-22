"""
70. Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

"""

class Solution:
    def climbStairs(self, n: int) -> int:
        steps = {}
        def recur(N):
            if N in steps:
                return steps[N]

            if N < 3:
                res = N
            else:
                res =  recur(N-1) + recur(N-2)
            
            steps[N] = res

            return res
  
        return recur(n)