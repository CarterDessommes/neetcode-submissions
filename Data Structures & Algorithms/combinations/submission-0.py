class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol = []
        cur = []
        r = [0] * n
        for i in range(1, n + 1):
            r[i - 1] = i
        self.recurse(k, sol, cur, r)
        return sol


        
    
    def recurse(self, k, sol, cur, r):
        if len(cur) == k:
            sol.append(list(cur))
            return
        
        for i in range(len(r)):
            clone = [x for x in r if x > r[i]]

            cur.append(r[i])
            self.recurse(k, sol, cur, clone)
            cur.pop()


        



        
