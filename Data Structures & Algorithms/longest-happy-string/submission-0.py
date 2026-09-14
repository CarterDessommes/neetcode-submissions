class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        prev = -1
        count = [a, b, c]

        # gotta get the max char in a special day 
        def getMax(prev):
            idx = -1
            maxCnt = 0
            # loop over each char
            for i in range(3):
                # if we already used it or there are none
                # left to use
                if i == prev or count[i] == 0:
                    continue
                # set the max count and track
                # which letter it is
                if maxCnt < count[i]:
                    maxCnt = count[i]
                    idx = i

            return idx

        while True:
            # returns idx of letter with highest ocunt
            maxChar = getMax(prev)
            # if none are left we are done
            if maxChar == -1:
                break
            
            # otherwise append the correct char
            res.append(chr(maxChar + ord('a')))
            # decd its count
            count[maxChar] -= 1
            # if the last two chars are the same set the 
            # prev var
            if len(res) > 1 and res[-1] == res[-2]:
                prev = maxChar
            # otherwise it must not be set
            else:
                prev = -1
        
        return "".join(res)
        