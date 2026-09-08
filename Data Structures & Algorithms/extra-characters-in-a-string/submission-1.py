class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # min number of extra chars in a 
        # string starting at index i
        dp = [0] * (len(s) + 1)
    
        for i in reversed(range(len(s))):
            # at worst, we just add one to the previous answer
            dp[i] = 1 + dp[i + 1]

            # at best we find a matching word in the dictionary
            # that matches some prefix of the current string,
            # in which case we can see if taking this will give us 
            # a lower count of extra chars
            for word in dictionary:
                w = len(word)
                if i + w <= len(s):
                    if s[i:i+w] == word:
                        dp[i] = min(dp[i + w], dp[i])
            
        return dp[0]






        

        