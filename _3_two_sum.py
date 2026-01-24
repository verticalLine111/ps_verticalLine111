from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    prevMap = {}
    for i in range(0, len(nums)):
        diff = target - nums[i]
        if diff in prevMap:
            return [ prevMap[diff] , i ]
        else:
            prevMap[nums[i]] = i
    