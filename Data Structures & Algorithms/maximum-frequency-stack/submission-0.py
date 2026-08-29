class FreqStack:
    # we can use a stack of stacks
    def __init__(self):
        self.cnt = defaultdict(int)
        self.maxCnt = 0
        self.stacks = defaultdict(list)
        

    def push(self, val: int) -> None:
        self.cnt[val] += 1
        valCnt = self.cnt[val]

        if valCnt > self.maxCnt:
            self.maxCnt = valCnt

        # append the value to the associated stack
        self.stacks[valCnt].append(val)
        

    def pop(self) -> int:
        res = self.stacks[self.maxCnt].pop()
        self.cnt[res] -= 1
        # if this was the last element in the stack, decrease max 
        # coutn by one
        if not self.stacks[self.maxCnt]:
            self.maxCnt -= 1
        return res
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()