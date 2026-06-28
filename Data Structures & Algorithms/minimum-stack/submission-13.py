class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []
    def push(self, val: int) -> None:
        if not self.mins:
            self.mins.append(val)
        elif self.mins[-1] >= val:
            self.mins.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.mins[-1]:
            self.mins.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1] if self.mins else 0
