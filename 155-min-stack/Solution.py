# Medium
# Tags: stack, design

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        mn = self.getMin()
        if mn == None or val > mn:
            mn = val
        self.stack.append([val, mn])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None
