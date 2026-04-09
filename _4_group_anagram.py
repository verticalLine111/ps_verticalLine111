from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        fmap = defaultdict(list)
        for i in range(len(strs)):
            alph = [0] * 26
            for c in strs[i]:
                alph[ord(c) - ord('a')] += 1
            # fmap[alph].append(strs[i])
            fmap[tuple(alph)].append(strs[i])
        print(fmap)
        return res