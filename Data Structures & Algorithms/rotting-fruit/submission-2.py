class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rotten = deque()
        fresh = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotten.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        time = 0
        while rotten and fresh > 0:
            time += 1
            layer = []
            while rotten:
                layer.append(rotten.popleft())

            for r, c in layer:
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for dr, dc in directions:
                    r2 = r + dr
                    c2 = c + dc
                    if r2 < len(grid) and r2 >= 0 and c2 < len(grid[0]) and c2 >= 0:
                        if grid[r2][c2] == 1:
                            fresh -= 1
                            grid[r2][c2] = 2
                            rotten.append((r2, c2))
        
        if fresh == 0:
            return time
        return -1





        
        
        
       

            
          


    


  
        