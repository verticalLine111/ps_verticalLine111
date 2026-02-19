from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = [[] for i in range(len(nums) + 1)]
        freqMap = {}
        for n in nums:
            if n in freqMap:
                freqMap[n] += 1
            else:
                freqMap[n] = 0
        for key, val in freqMap.items():
            cnt[val].append(key)

        res = []
        for arr in cnt[::-1]:
            for v in arr:
                if len(res) < k:
                    res.append(v)

        return res