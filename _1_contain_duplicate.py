from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqMap = {}
        for i in range(len(nums)):
            if nums[i] in freqMap:
                return True
            else:
                freqMap[nums[i]] = 1
        return False