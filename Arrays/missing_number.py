'''
https://leetcode.com/problems/missing-number/submissions/
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_exp = n*(n+1)//2
        sum_act = sum(nums)

        return sum_exp - sum_act
