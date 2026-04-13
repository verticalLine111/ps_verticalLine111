class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ziplist = list(zip(position, speed))
        ziplist.sort(reverse=True)
        stk = []
        for p,s in ziplist:
            time = (target - p) / s
            if not stk or stk[-1] < time:
                stk.append(time)
            
        return len(stk)