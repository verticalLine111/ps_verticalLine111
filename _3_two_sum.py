from typing import List, Counter

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nmap = Counter()
        for i in range(len(nums)):
            if target - nums[i] in nmap:
                return [nmap[target - nums[i]], i]
            else:
                nmap[nums[i]] = i
