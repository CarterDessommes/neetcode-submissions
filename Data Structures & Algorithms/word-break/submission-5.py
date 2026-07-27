class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [False] * (len(s) + 1)
        memo[0] = True

        for i in range(len(s)):
            if memo[i]:
                for word in wordDict:
                    if s[i:i+len(word)] == word:
                        memo[i+len(word)] = True
        
        return memo[len(s)]





        