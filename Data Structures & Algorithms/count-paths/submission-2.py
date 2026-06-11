class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = [[0] * n for _ in range(m)]

        memo[m - 1][n - 1] = 1


        for y in reversed(range(m)):
            for x in reversed(range(n)):

                if y == m - 1 and x == n - 1:
                    continue

                val = 0
                if y + 1 < m:
                    val += memo[y + 1][x]
                
                if x + 1 < n:
                    val += memo[y][x + 1]

                memo[y][x] = val
        
        return memo[0][0]




    

        