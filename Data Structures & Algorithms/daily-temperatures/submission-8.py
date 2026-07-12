class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0] * len(temperatures)
        # monotonic decreasing stack
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                result[stackInd] = i - stackInd
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


        