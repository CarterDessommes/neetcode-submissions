class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        

        memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]


        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if r == m - 1 and c == n - 1:
                    memo[r][c] = 1
                    continue
                
                memo[r][c] = memo[r + 1][c] + memo[r][c + 1]
        
        return memo[0][0]



        