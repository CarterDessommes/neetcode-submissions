class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int: 
        
        m = len(grid)
        n = len(grid[0])

        memo = [[0] * n for _ in range(m)]


        for x in reversed(range(n)):
            for y in reversed(range(m)):
                
                if y == m - 1 and x == n - 1:
                    memo[y][x] = grid[y][x]
                    continue
                
                val = grid[y][x]
                val_x = float('inf')
                val_y = float('inf')
                if y + 1 < m:
                    val_y = memo[y + 1][x]
                if x + 1 < n:
                    val_x = memo[y][x + 1]
                
                val += min(val_x, val_y)

                memo[y][x] = val
        

        return memo[0][0]
        