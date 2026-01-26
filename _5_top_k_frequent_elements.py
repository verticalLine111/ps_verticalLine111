from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countArr = [[] for _ in range(len(nums) +1)]
        freqMap = {}
        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1
        for key,val in freqMap.items():
            countArr[val].append(key)
        res = []
        count = 0
        for arr in countArr[::-1]:
            if len(arr) > 0:
                for num in arr:
                    res.append(num)
                    count +=1
            if count == k:
                return res
        return res