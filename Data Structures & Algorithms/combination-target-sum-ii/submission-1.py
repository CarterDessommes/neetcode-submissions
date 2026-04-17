class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        self.recurse(sol, [], target, candidates, 0)
        return sol
            
    def recurse(self, sol, cur, target, candidates, i):
        if sum(cur) == target:
            clone = sorted(cur.copy())
            if clone not in sol:
                sol.append(clone)
            return
        
        if sum(cur) > target or i >= len(candidates):
            return
        
        cur.append(candidates[i])
        self.recurse(sol, cur, target, candidates, i+1)
        cur.pop()
    
        self.recurse(sol, cur, target, candidates, i+1)
        