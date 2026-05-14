class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count += 1
                    self.clearIsland(grid, r, c)
        
        return count

    

    def clearIsland(self, grid, r, c):
        if r < 0 or r >= len(grid):
            return
        
        if c < 0 or c >= len(grid[0]):
            return

        if grid[r][c] == "0":
            return

        grid[r][c] = "0"

        self.clearIsland(grid, r + 1, c)
        self.clearIsland(grid, r - 1, c)
        self.clearIsland(grid, r, c - 1)
        self.clearIsland(grid, r, c + 1)






        