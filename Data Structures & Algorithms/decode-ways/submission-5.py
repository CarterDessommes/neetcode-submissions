class Solution:
    def numDecodings(self, s: str) -> int:
        
        # memo is # of ways to decode i onwards
        memo = {len(s): 1}
        

        for i in reversed(range(len(s))):
            if s[i] == "0":
                memo[i] = 0
            else:
                memo[i] = memo[i + 1]
            
            if i + 1 < len(s) and 10 <= int(s[i:i + 2]) <= 26:
                memo[i] += memo[i + 2]
        
        return memo[0]


        