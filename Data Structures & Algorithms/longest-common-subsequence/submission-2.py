class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # memo[i][j] is lcs of text1[:i] and text2[:j]
        memo = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):

                # LCS("abc", "adc") = 1 + LCS("ab", "ad")
                if text1[i - 1] == text2[j - 1]:
                    memo[i][j] = 1 + memo[i - 1][j - 1]
                # if they differ, we cannot include both in the lcs
                # so chose whichever gives a longer subsequence
                else:
                    memo[i][j] = max(memo[i - 1][j], memo[i][j - 1])

        
        return memo[i][j]
