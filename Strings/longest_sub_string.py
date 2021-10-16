class Solution(object):
    def lengthOfLongestSubstring(self, s):
        i = 0
        j = 0
        d = {}
        ans = 0
        while j < len(s):
            if s[j] not in d or i > d[s[j]]:
                ans = max(ans, (j-i+1))
                d[s[j]] = j
            else:
                i = d[s[j]]+1
                ans = max(ans, (j-i+1))
                j -= 1
            # print(ans)
            j += 1
        return ans


ob1 = Solution()
print(ob1.lengthOfLongestSubstring("ABCABCBQWERTYU"))


def withoutRepeating(str):
    visited = [False] * 128
    for ch in str:
        if visited[ord(ch)]:
            return False
        else:
            visited[ord(ch)] = True
    return True


def longestSubstringWithoutRepeating(str):
    maxLength = 0
    for i in range(len(str)):
        for j in range(i, len(str)):
            substr = str[i:j+1]
            if withoutRepeating(substr) and len(substr) > maxLength:
                maxLength = len(substr)
    return maxLength
