from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        smap = {}
        for i in range(len(numbers)):
            tToN = target - numbers[i]
            if tToN in smap:
                return [ smap[tToN] ,i+ 1]
            else:
                smap[numbers[i]] = i+1
        return []