'''
https://leetcode.com/problems/group-anagrams/submissions/
'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        lookup = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            lookup[key].append(s)

        dups = []
        for l in lookup.values():
            dups.append(l)

        return dups


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        lookup = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            lookup[key].append(s)

        return [l for l in lookup.values()]
