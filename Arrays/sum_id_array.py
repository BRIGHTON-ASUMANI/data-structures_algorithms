'''
https://leetcode.com/problems/running-sum-of-1d-array/submissions/
'''


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(1, n):
            nums[i] = nums[i]+nums[i-1]
        return nums
