class FreqStack:

    def __init__(self):
        self.freqMap = defaultdict(int)
        self.stacks = {}
        self.maxCnt = 0

    def push(self, val: int) -> None:
        self.freqMap[val] += 1
        if self.freqMap[val] > self.maxCnt:
            self.maxCnt = self.freqMap[val]
            self.stacks[self.freqMap[val]] = []
        self.stacks[self.freqMap[val]].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxCnt].pop()
        self.freqMap[res] -= 1
        if not self.stacks[self.maxCnt]:
            self.maxCnt -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()