'''
https://leetcode.com/problems/roman-to-integer/
'''

class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I': 1, 'V' : 5, 'X': 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' :1000}
        s = s[::-1]
        total = 0
        highest = 0
        buffer = ""
        for char in s:
            value = map[char]
            if value >= highest:
                highest = value
                total += value
            else:
                total -= value
        return total