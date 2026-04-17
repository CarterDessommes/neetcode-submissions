class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    area = self.removeIsland(x, y, grid)
                    maxArea = max(maxArea, area)
        return maxArea

    
    def removeIsland(self, x, y, grid, ):
        if x < 0 or x >= len(grid):
            return 0
        if y < 0 or y >= len(grid[0]):
            return 0
        
        if grid[x][y] == 0:
            return 0

        grid[x][y] = 0

        return (
            1
            + self.removeIsland(x + 1, y, grid)
            + self.removeIsland(x - 1, y, grid)
            + self.removeIsland(x, y + 1, grid)
            + self.removeIsland(x, y - 1, grid)
        )
        

        
        