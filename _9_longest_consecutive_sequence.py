from collections import Counter
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nmap = Counter(nums)
        res = 0
        for n in nums:
            l = 1
            while n + l in nmap:
                l+= 1
            res = max(res, l)
        return res