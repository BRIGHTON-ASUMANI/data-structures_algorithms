import random
'''
https://leetcode.com/problems/shuffle-an-array/
'''


class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        :type size: int
        """
        self.nums = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        # Time complexity: O(n)
        # Space complexity: O(1)
        nums = self.nums
        last_index = len(nums)-1
        while last_index > 0:

            # Get the random index
            rand_index = random.randint(0, last_index)

            # store value temporarily
            temp = nums[rand_index]
            # Swap last index with the random index
            nums[rand_index] = nums[last_index]
            #
            nums[last_index] = temp
            last_index -= 1
        return nums

  # Shuffle array using random.shuffle
    def shuffleRandom(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        nums = list(self.nums)
        random.shuffle(nums)
        return nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
