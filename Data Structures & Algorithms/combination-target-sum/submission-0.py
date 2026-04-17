class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        self.recurse(sol, [], target, nums)
        return sol
        
    def exists(self, sol, candidate):
        for num in sol:
            if sorted(num) == sorted(candidate):
                return True
        return False

    def recurse(self, sol, cur, target, nums):
        if sum(cur) == target:
            clone = sorted(cur.copy())
            if not self.exists(sol, cur):
                sol.append(clone)
            return

        
        if sum(cur) > target:
            return
        
        for num in nums:
            cur.append(num)
            self.recurse(sol, cur, target, nums)
            cur.pop()
        


        