class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        i, j = self.find_start(grid)
        print("start is", i, j)
        queue = deque()
        queue.append((i, j))
        visited.add((i, j))
        count = 0
        while queue:
            cur = queue.popleft()
            neighbors = self.check_sides(cur, grid)
            count += 4 - len(neighbors)
            for n in neighbors:
                if n not in visited:
                    queue.append(n)
                    visited.add(n)
        return count
            
    def find_start(self, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return i, j
    
    def check_sides(self, coords, grid):
        lst = []
        i = coords[0]
        j = coords[1]
        if i + 1 < len(grid) and grid[i + 1][j] == 1:
            lst.append((i + 1, j))
        if i - 1 >= 0 and grid[i - 1][j] == 1:
            lst.append((i - 1, j))
        if j + 1 < len(grid[0]) and grid[i][j + 1] == 1:
            lst.append((i, j + 1))
        if j - 1 >= 0 and grid[i][j - 1] == 1:
            lst.append((i, j - 1))
        return lst


        