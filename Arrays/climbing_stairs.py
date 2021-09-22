'''
https://leetcode.com/problems/climbing-stairs/submissions/
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        current = 0
        prev1 = 1
        prev2 = 2

        for i in range(2, n):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
        return current
