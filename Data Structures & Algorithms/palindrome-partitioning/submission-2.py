class Solution:
    def partition(self, s: str) -> List[List[str]]:

        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for center in range(n):
            for l, r in [(center, center), (center, center + 1)]:
                while l >= 0 and r < n and s[l] == s[r]:
                    dp[l][r] = True
                    l -= 1
                    r += 1
        
        

        res = []
        cur = []

        def dfs(i, j):
            if j >= len(s):
                if i == j:
                    res.append(cur.copy())
                return
            
            if dp[i][j]:
                cur.append(s[i : j + 1])
                dfs(j + 1, j + 1)
                cur.pop()
            
            dfs(i, j + 1)
        
        dfs(0, 0)
        return res

        ###
        
        
