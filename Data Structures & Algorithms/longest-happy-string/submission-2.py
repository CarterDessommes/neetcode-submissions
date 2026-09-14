class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        prev = -1
        count = [a, b, c]

        def getMax(prev):
            idx = -1
            maxCnt = -1
            for i in range(3):
                if i == prev or count[i] == 0:
                    continue
                
                if count[i] > maxCnt:
                    idx = i
                    maxCnt = count[i]
            return idx


        while True:
            maxVar = getMax(prev)

            if maxVar == -1:
                break

            res.append(chr(maxVar + ord("a")))
            count[maxVar] -= 1

            if len(res) > 1 and res[-1] == res[-2]:
                prev = maxVar
            else:
                prev = -1
            
            
        
        return "".join(res)