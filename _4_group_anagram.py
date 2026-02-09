from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        amap = defaultdict(list)
        for s in strs:
            alpha = [0] * 26
            for c in s:
                alpha[ord(c) - ord('a')] += 1
            amap[tuple(alpha)].append(s)
        return list(amap.values())