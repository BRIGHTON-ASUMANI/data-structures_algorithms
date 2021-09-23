'''
https://leetcode.com/problems/length-of-last-word/submissions/
'''


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len((s.strip().split(' ')[-1]))


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = 0

        # String a is 'final'-- can not be modified
        # So, create a copy and trim the spaces from
        # both sides
        x = s.strip()

        for i in range(len(x)):
            if x[i] == " ":
                l = 0
            else:
                l += 1
        return l
