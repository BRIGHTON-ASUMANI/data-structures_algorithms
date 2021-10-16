'''
https://leetcode.com/problems/longest-common-prefix/
'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # strs.sort()
        str_start = strs[0]
        str_last = strs[-1]
        count = 0
        for i in range(len(str_start)):
            if (str_start[i] != str_last[i]):
                break
            else:
                count += 1
        if count == 0:
            return ""
        else:
            return str_start[:count]
