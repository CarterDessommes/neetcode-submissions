class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # precompute palindromic substrings to save time.
        n = len(s)
        dp = [[False] * n for _ in range(n)]        
        for center in range(n):
            # test even and odd centers
            for left, right in [(center, center), (center, center+1)]:
                while left >= 0 and right < n and s[left] == s[right]:
                    dp[left][right] = True
                    left -= 1
                    right += 1
        
        
        res = []
        cur = []
        
        def dfs(i, j):
            if j >= len(s):
                if i == j:
                    res.append(cur.copy())
                return 

            if dp[i][j]:
                # choose explore unchoose
                cur.append(s[i : j + 1])
                dfs(j + 1, j + 1)
                cur.pop()
            
            dfs(i, j + 1)
        
        dfs(0, 0)
        return res
        ###
        
        
