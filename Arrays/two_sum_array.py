'''
https://leetcode.com/problems/two-sum/submissions/
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for i in range(len(nums)):
            # check for the value in look up
            if nums[i] in lookup:
                # print(lookup)
                # print([lookup[nums[i]], i])
                return [lookup[nums[i]], i]
            # if not add value lookup
            else:
                # print(lookup)
                lookup[target-nums[i]] = i
        return None


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in lookup:
                return [lookup[diff], i]
            lookup[n] = i
        return
