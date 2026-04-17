class MyStack:

    def __init__(self):
        self.q = deque()
       
    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        l = len(self.q)

        # [2, 0, 0 ,1]
        #
        while l > 1:
            val = self.q.popleft()
            self.q.append(val)
            l -= 1
        
        return self.q.popleft()



        

    def top(self) -> int:
        return self.q[-1]

        

    def empty(self) -> bool:
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()