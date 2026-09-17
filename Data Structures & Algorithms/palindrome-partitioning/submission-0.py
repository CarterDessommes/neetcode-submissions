class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        cur = []
        
        
        def dfs(i, j):
            if j >= len(s):
                if i == j:
                    res.append(cur.copy())
                return 

            if self.isPalindrome(s, i, j):
                # choose explore unchoose
                cur.append(s[i : j + 1])
                dfs(j + 1, j + 1)
                cur.pop()
            
            dfs(i, j + 1)
        
        dfs(0, 0)
        return res

    def isPalindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True
        
