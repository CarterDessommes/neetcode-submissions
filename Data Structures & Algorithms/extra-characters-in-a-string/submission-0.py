class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # min number of extra chars in a 
        # string starting at index i
        dp = [0] * (len(s) + 1)
    
        for i in reversed(range(len(s))):
            
            dp[i] = 1 + dp[i + 1]

            for word in dictionary:
                w = len(word)
                if i + w <= len(s):
                    if s[i:i+w] == word:
                        dp[i] = min(dp[i + w], dp[i])
            
        return dp[0]






        

        