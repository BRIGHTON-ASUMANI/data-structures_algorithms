'''
https://leetcode.com/problems/plus-one/submissions/
'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = ''.join([str(i) for i in digits])
        res = list(str(int(l)+1))
        return [int(i) for i in res]
