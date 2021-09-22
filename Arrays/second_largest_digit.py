'''
https://leetcode.com/problems/second-largest-digit-in-a-string
'''
import re

class Solution:
    def secondHighest(self, s: str) -> int:
        x = re.findall(r'\d+', s)
        y = ''.join(x)
        ys = set(y)
        w = len(list(ys))

        if(w < 2):
            return -1

        yz = sorted(list(set([int(x) for x in y])))

        listedY = yz[-2]
        return listedY
