class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int: 
        
        m = len(grid)
        n = len(grid[0])

        # memo = [[0] * n for _ in range(m)]
        # above is the more intuitive non space optimized memo. 
        # when using above, you would just do memo[y][x].
        # But we can optimize the space complexity to just be O(n)
        # instead of O(mn) by 
        memo = [0] * n


        for y in reversed(range(m)):
            for x in reversed(range(n)):

                if y == m - 1 and x == n - 1:
                    memo[x] = grid[y][x]
                    continue
                
                val = grid[y][x]
                val_x = float('inf')
                val_y = float('inf')
                if y + 1 < m:
                    val_y = memo[x]
                if x + 1 < n:
                    val_x = memo[x + 1]
                
                val += min(val_x, val_y)

                memo[x] = val
        

        return memo[0]
        