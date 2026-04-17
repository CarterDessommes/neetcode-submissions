class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []
        self.recurse(n, sol, [], 0, 0)
        return sol



    def recurse(self, n, sol, cur, l, r):
        if l > r or (l + r) > (n * 2) or l > n or r > n:
            return 

        if (l + r) == (n * 2):
            sol.append("".join(cur.copy()))
            return
        
        

        cur.append("(")
        self.recurse(n, sol, cur, l, r + 1)
        cur.pop()

        cur.append(")")
        self.recurse(n, sol, cur, l + 1, r)
        cur.pop()
    

    