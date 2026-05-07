class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        q = deque()
        fresh = 0
        time = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    fresh += 1
                if grid[x][y] == 2:
                    q.append((x, y))


        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while fresh > 0 and q:
            length = len(q)
            for i in range(length): 

                x, y = q.popleft()

                for dx, dy in directions:
                    x2 = x + dx
                    y2 = y + dy
                    if x2 in range(len(grid)) and y2 in range(len(grid[0])):
                        if grid[x2][y2] == 1:
                            grid[x2][y2] = 2
                            q.append((x2, y2))
                            fresh -= 1
            
            time += 1

        return time if fresh == 0 else -1

            
          


    


  
        