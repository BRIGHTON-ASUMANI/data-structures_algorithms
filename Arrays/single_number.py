'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?
'''


from collections import defaultdict


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_table = {}
        for x in nums:
            '''
            Time complexity =  O(n * 1)=O(n).
            '''
            try:
                # O(1) pop removes one element in an array no matter the input
                hash_table.pop(x)
            except:
                hash_table[x] = 1
        return hash_table.popitem()[0]  # constant O(1)


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1

        for i in hash_table:
            if hash_table[i] == 1:
                return i


'''
Time complexity =  O(n * 1)=O(n). contstans are always the same
Time complexity of for loop is O(n) --> increase in time according to the input(linear time)
Time complexity of hash table(dictionary in python) operation pop is O(1).
Space complexity : O(n). The space required by hash_table is == number of elements in nums.
'''


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)


'''
Time complexity : O(n+n)=O(n).
Space complexity : O(n+n)=O(n). set needs space for the elements in
'''
