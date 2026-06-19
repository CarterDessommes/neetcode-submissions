class Solution:
    def numSquares(self, n: int) -> int:
        memo = [n] * (n + 1)

        memo[0] = 0
        # the idea here is that we look over every square 
        # that is less than our current value we are solving for.
        for i in range(1, n + 1):
            for s in range(1, i):
                
                square = s * s 

                if i - square < 0:
                    break
                
                memo[i] = min(memo[i], 1 + memo[i - square])
        
        return memo[n]

