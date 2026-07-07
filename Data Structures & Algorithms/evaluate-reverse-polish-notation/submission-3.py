class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        # this problem lends itself to a stack
        # as the operation is always applied to
        # two most recent nums
        for token in tokens:
            if token == "-":
                first = stack.pop()
                second = stack.pop()
                stack.append(second - first)
            elif token == "+":
                first = stack.pop()
                second = stack.pop()
                stack.append(second + first)
            elif token == "*":
                first = stack.pop()
                second = stack.pop()
                stack.append(second * first)
            elif token == "/":
                first = stack.pop()
                second = stack.pop()
                # we do second/first then convert to int to get the 
                # rounding to 0 behavior. // rounds down always, 
                # so -3//2 gives -2 when we want it to give -1. the conversion 
                # from float to int just chops the decimal point which is hte 
                # same as rounding to 0.
                stack.append(int(second / first))
            else: 
                # make sure we are appending integers not chars
                stack.append(int(token))
        
        return stack.pop()



        