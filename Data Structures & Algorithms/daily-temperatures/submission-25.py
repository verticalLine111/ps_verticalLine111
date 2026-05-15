class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)
        for i , t in enumerate(temperatures):
            while stk and stk[-1][1] < t:
                sti, stt = stk.pop()
                res[sti] = i - sti
            stk.append((i,t))

        return res