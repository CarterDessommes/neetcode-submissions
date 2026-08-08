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
            val = grid[cur_r][cur_c]

            for dr, dc in directions: 
                if (cur_r + dr >= 0 and cur_r + dr < len(grid) and 
                    cur_c + dc >= 0 and cur_c + dc < len(grid[0]) and 
                        grid[cur_r + dr][cur_c + dc] == INF):
                        grid[cur_r + dr][cur_c + dc] = grid[cur_r][cur_c] + 1
                        q.append((cur_r + dr, cur_c + dc))





        