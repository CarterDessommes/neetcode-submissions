class MinStack:

    def __init__(self):
        # intialize a stack and a min tracker
        self.stack = []
        self.minVal = 0

        
    def push(self, val: int) -> None:
        # if the stacks empty 
        if not self.stack:
            self.stack.append(0)
            self.minVal = val
        else:
            self.stack.append(val - self.minVal)
            self.minVal = min(self.minVal, val)

    def pop(self) -> None:
        if not self.stack:
            return 
        
        encoded = self.stack.pop()
        if encoded < 0:
            self.minVal = self.minVal - encoded
        
        
    def top(self) -> int:
        encoded = self.stack[-1]
        if encoded > 0:
            return encoded + self.minVal
        else:
            return self.minVal

    def getMin(self) -> int:
        return self.minVal
        
        
