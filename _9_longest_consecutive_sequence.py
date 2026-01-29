from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i, a in enumerate(numSet):
            if (a-1) in numSet:
                continue
            else:
                length=1
                while (a + length) in numSet:
                    length += 1
                longest = max(longest , length)

        return longest