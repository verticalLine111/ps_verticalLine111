class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, fixed in enumerate(nums):
            # 첫 번째 수가 양수면 세 수의 합이 0이 될 수 없음
            if fixed > 0:
                break

            # 같은 값 건너뛰기 (중복 triplet 방지)
            if i > 0 and fixed == nums[i - 1]:
                continue

            # 투 포인터로 나머지 두 수 찾기
            left, right = i + 1, len(nums) - 1
            target = -fixed

            while left < right:
                two_sum = nums[left] + nums[right]

                if two_sum < target:
                    left += 1
                elif two_sum > target:
                    right -= 1
                else:
                    res.append([fixed, nums[left], nums[right]])
                    # 중복 건너뛰기
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res