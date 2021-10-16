'''
https://leetcode.com/problems/add-to-array-form-of-integer/submissions/
'''


class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        x = ''.join([str(elem) for elem in num])
        ans = int(x)+k
        return [int(elem) for elem in str(ans)]
