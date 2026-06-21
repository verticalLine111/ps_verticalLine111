class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []                 # 높이가 증가하는 순서로 '인덱스'를 저장
        max_area = 0
        heights = heights + [0]    # 끝에 0(보초값) → 마지막에 스택을 전부 비우는 트리거

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                top = stack.pop()
                height = heights[top]
                left = stack[-1] if stack else -1
                width = i - left - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area