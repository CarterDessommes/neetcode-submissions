class Solution:
    def reorganizeString(self, s: str) -> str:
        count = [0] * 26
        prev = -1
        res = []

        for char in s:
            count[ord(char) - ord("a")] += 1
        
        def getMax(prev):
            maxCnt = -1
            idx = -1
            for i in range(26):
                if i == prev or count[i] == 0:
                    continue
                
                if count[i] > maxCnt:
                    maxCnt = count[i]
                    idx = i
            
            return idx
        
        while True:
            idx = getMax(prev)

            if idx == -1:
                break
            
            res.append(chr(idx + ord("a")))
            count[idx] -= 1

            if len(res) > 0:
                prev = idx
        
        return "".join(res) if len(res) == len(s) else ""
            



        



        