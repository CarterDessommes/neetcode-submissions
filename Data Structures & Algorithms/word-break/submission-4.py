class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wether s[:i] can be broken down
        memo = [False] * (len(s) + 1)
        memo[0] = True


        for i in range(len(s)):
            if not memo[i]:
                continue

            for w in wordDict:
                if s[i:i + len(w)] == w:
                    memo[i + len(w)] = True

                    
            
        return memo[len(s)]




        