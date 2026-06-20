class Solution:
    def integerBreak(self, n: int) -> int:


        memo = [0] * (n + 1)

        memo[0] = 0
        memo[1] = 0
        # memo[2] = 1
        # memo[3] = 2
        # memo[4] = 4
        # memo[5] = 6


        for i in range(2, n + 1):
            for j in range(1, i):
                compliment = i - j

                memo[i] = max(memo[i], 
                max(j, memo[j]) * 
                max(compliment, memo[compliment])
                )


        return memo[n]
        