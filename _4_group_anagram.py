from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        amap = defaultdict(list)
        for s in range(len(strs)):
            alpha = [0] * 26
            for c in strs[s]:
                alpha[ord(c) - ord('a')] += 1
            amap[tuple(alpha)].append(strs[s])
        res = []
        for k, v in amap.items():
            res.append(v)
        return res

