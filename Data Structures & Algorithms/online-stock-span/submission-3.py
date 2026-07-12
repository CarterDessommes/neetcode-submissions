class StockSpanner:

    def __init__(self):
        self.stack = []
        # stack contains prices that have not been coalesced into another sum or 
        # havent found anything that is higher
        

    def next(self, price: int) -> int:
        count = 1
        # while we have lesser values to clear off the stack
        while self.stack and price >= self.stack[-1][0]:
            stackIdx, stackCount = self.stack.pop()
            # we know that the count of this number contains strictly numbers smaller 
            # than our current number so we can just steal this precomputed number
            count += stackCount
        
        self.stack.append((price, count))
        return count
        

# monotonic decreasing stack problem, clear the stack and compute some value relevant to your solution
# while clearing the stack. take advantage of what you know about how it is decreasing

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)