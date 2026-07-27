class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # wether s[i:] can be broken
        memo = [False] * (len(s) + 1)
        memo[len(s)] = True

        for i in reversed(range(len(s))):
            for w in wordDict:
                if s[i:i + len(w)] == w:
                    memo[i] = memo[i + len(w)]

                    if memo[i] == True:
                        break
            
        return memo[0]




        