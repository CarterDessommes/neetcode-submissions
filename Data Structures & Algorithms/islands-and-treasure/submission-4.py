class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            cur_r, cur_c = q.popleft()

            for dr, dc in directions: 
                if (cur_r + dr >= 0 and cur_r + dr < len(grid) and 
                    cur_c + dc >= 0 and cur_c + dc < len(grid[0]) and 
                        grid[cur_r + dr][cur_c + dc] != -1):

                    grid[cur_r][cur_c] = min(grid[cur_r][cur_c], grid[cur_r + dr][cur_c + dc] + 1)
                    
                    if grid[cur_r + dr][cur_c + dc] == INF:
                        # no min because redundant, as whoever gets here
                        # first will be smallest
                        # set value of unknown based off value of known
                        grid[cur_r + dr][cur_c + dc] =  grid[cur_r][cur_c] + 1
                        q.append((cur_r + dr, cur_c + dc))





        