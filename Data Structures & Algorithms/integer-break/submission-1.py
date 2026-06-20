class Solution:
    def integerBreak(self, n: int) -> int:
        memo = [0] * (n + 1)

        memo[0] = 0
        memo[1] = 0

        # this one is a tiny bit tricky, we loop over 
        # all the possible pairs of values that could make up 
        # our current target, we then check whether the
        # current value in the memo is higher, or if we can make a higher
        # one by either keeping our pair of values as is, or 
        # breaking them down further into smaller pieces.
        for i in range(2, n + 1):
            for j in range(1, i):
                compliment = i - j

                # check if value alr there is better or if 
                # we can make a better one
                memo[i] = max(memo[i], 
                max(j, memo[j]) * # check if we can get a better value leaving as is or breaking down further
                max(compliment, memo[compliment])
                )

        return memo[n]