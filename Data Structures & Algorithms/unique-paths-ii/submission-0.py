class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        memo = [[0] * n for _ in range(m)]


        for y in reversed(range(m)):
            for x in reversed(range(n)):

                if obstacleGrid[y][x] == 1:
                    memo[y][x] = 0
                    continue

                if y == m - 1 and x == n - 1:
                    memo[y][x] = 1
                    continue
                
                val = 0 
                if y + 1 < m:
                    val += memo[y + 1][x]
                
                if x + 1 < n:
                    val += memo[y][x + 1]

                memo[y][x] = val
        

        return memo[0][0]



                

                





        