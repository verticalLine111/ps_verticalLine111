class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []
        for i, t in enumerate(temperatures):
            while stk and t > stk[-1][0]:
                stt , sti = stk.pop()
                res[sti] = i - sti
            stk.append((t, i))
        return res