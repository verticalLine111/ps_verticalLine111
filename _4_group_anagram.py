from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqMap = defaultdict(list)
        for s in strs:
            k = [0] * 26
            for c in s:
                k[ord(c) - ord('a')] += 1
            freqMap[tuple(k)].append(s)
        return list(freqMap.values())