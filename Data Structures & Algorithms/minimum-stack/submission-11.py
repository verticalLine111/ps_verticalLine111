class MinStack:

    def __init__(self):
        self.stk = []
        self.minstk = []

    def push(self, val: int) -> None:
        if not self.minstk:
            self.minstk.append(val)
            self.stk.append(val)
        else:
            if self.minstk[-1] > val:
                self.minstk.append(val)
                self.stk.append(val)
            else:
                self.minstk.append(self.minstk[-1])
                self.stk.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.minstk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minstk[-1]