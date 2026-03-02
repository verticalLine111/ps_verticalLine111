from typing import List
from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = Counter()
        for n in nums:
            cnt[n] += 1
            if cnt[n] == 2:
                return True
        return False