class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        # stack to hold days that have not found a warmer day
        # holds temp and index. By nature, it is monotonic and decreasing
        # as otherwise we would have found a warmer day and it wouldnt be on the stack
        result = [0] * len(temperatures)

        # o(n) time and space
        for i, t in enumerate(temperatures):
            # clear the stack of temperatures that 
            # have now found a warmer day
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                # their result is current index minus their index
                result[stackInd] = i - stackInd
            # add the current index to the stack for processing.
            stack.append((t, i))
        return result

        # o(n^2) solution   
        # result = [0] * (len(temperatures))

        # for i in range(len(temperatures)):
        #     count = 0 
        #     for j in range(i, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             result[i] = count
        #             break
        #         count += 1

        # return result


        