class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1] # 인덱스를 저장 (계산을 편하게 하기 위해 -1을 먼저 넣음)
        max_area = 0
        heights.append(0) # 마지막에 높이 0 추가 (스택 청소용)
        
        for i in range(len(heights)):
            # 현재 높이가 스택 top의 높이보다 낮으면, 스택에서 꺼내며 넓이 계산
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()] # 꺼낸 막대의 높이
                w = i - stack[-1] - 1    # 너비 계산
                max_area = max(max_area, h * w)
            
            stack.append(i)
            
        return max_area