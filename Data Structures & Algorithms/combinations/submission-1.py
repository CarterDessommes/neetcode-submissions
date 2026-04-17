class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol = []
        cur = []
        self.recurse(1, cur, k, n, sol)
        return sol


        
    
    def recurse(self, start, cur, k, n, sol):
        if len(cur) == k:
            sol.append(cur.copy())
            return
        
        for i in range(start, n + 1):
            cur.append(i)
            self.recurse(i + 1, cur, k, n, sol)
            cur.pop()


        



        
