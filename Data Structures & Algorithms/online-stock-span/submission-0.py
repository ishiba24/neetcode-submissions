class StockSpanner:
#feel like theres a way to also append to the stack the count so far so you dont have to iterate through completely each time
    def __init__(self):
        self.stockStack = []
        self.popped = []
    def next(self, price: int) -> int:
        count = 1
        while self.stockStack and self.stockStack[-1] <= price:
            self.popped.append(self.stockStack.pop())
            count += 1
        for num in self.popped:
            self.stockStack.append(num)
            self.popped = []
        self.stockStack.append(price)
        return count



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)