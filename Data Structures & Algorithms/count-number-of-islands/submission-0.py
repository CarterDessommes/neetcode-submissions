class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == '1':
                    count += 1
                    self.clearIsland(m, n, grid)
        return count

    def clearIsland(self, x, y, grid):
        if x >= len(grid) or x < 0:
            return
        if y >= len(grid[0]) or y < 0:
            return
        
        if grid[x][y] == '0':
            return

        if grid[x][y] == '1':
            grid[x][y] = '0'
            self.clearIsland(x + 1, y, grid)
            self.clearIsland(x, y + 1, grid)
            self.clearIsland(x , y - 1, grid)
            self.clearIsland(x - 1 , y, grid)


        