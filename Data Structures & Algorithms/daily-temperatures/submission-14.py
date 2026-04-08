class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # 스택에 있는게 이전것. temp[i]는 현재 지나가는 인덱스
                # 지금이 더 크다면
                prev = stack.pop()
                # 스택에서 인덱스를 팝
                res[prev] = i - prev
                # 결과에 그 "더 크다" 라는게 발생한 인덱스의 숫자를 기록
            stack.append(i)
        # 결과리턴
        return res