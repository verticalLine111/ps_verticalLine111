from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = [[] for i in range(len(nums) + 1)]
        fmap = {}
        for n in nums:
            if n in fmap:
                fmap[n] += 1
            else:
                fmap[n] = 1
        for key,val in fmap.items():
            cnt[val].append(key)
        res=[]
        for arr in cnt[::-1]:
            for i in arr:
                if len(res) < k:
                    res.append(i)

        return res