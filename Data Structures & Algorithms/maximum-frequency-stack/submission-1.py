class FreqStack:

    def __init__(self):
        self.counts = defaultdict(int)
        self.maxCnt = 0
        self.stacks = defaultdict(list)
        

    def push(self, val: int) -> None:
        valCnt = self.counts[val] + 1
        self.counts[val] = valCnt
        self.maxCnt = max(valCnt, self.maxCnt)
        self.stacks[valCnt].append(val)
        

    def pop(self) -> int:
        val = self.stacks[self.maxCnt].pop()
        self.counts[val] -= 1

        if not self.stacks[self.maxCnt]:
            self.maxCnt -= 1
        
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()