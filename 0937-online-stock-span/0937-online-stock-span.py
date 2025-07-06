class StockSpanner:

    def __init__(self):
        self.stack = []  # Each element is a pair: [price, span]

    def next(self, price: int) -> int:
        span = 1
        # While the current price is greater than or equal to the price at the top of the stack
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]  # Add their span to ours
        self.stack.append([price, span])
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)