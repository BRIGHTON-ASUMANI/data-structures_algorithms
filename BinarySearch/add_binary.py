'''
https://leetcode.com/problems/add-binary/
'''


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x = int(a, 2) + int(b, 2)
        # y = "{0:b}".format(x)
        y = format(x, "b")
        # y = (str(bin(x)).replace('0b',''))
        return y
