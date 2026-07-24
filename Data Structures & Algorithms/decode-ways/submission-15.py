class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = [1] * (len(s) + 1)

        for i in reversed(range(len(s))):

            if s[i] == "0":
                memo[i] = 0
            else:
                # if you decode as one number, there are 
                # memo[i + 1] ways left to decode the rest of the string
                memo[i] = memo[i + 1]
            
            # add number of ways if you count it as double digits,
            # memo[i + 2] ways left to decode the rest of the string
            if i + 1 < len(s) and 10 <= int(s[i:i+2]) <= 26:
                memo[i] += memo[i + 2]
            
        return memo[0]



        