class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()                      # 핵심 1: 먼저 정렬
        res = []
        n = len(nums)

        for i in range(n - 2):
            if nums[i] > 0:                          # 최적화: 양수면 합 0 불가능
                break
            if i > 0 and nums[i] == nums[i - 1]:     # i 중복 건너뛰기
                continue

            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # left, right 중복 건너뛰기
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif s < 0:
                    left += 1    # 합이 작으면 왼쪽을 키운다
                else:
                    right -= 1   # 합이 크면 오른쪽을 줄인다

        return res