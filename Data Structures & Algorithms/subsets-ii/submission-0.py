class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sol = []
        self.recurse(sol, [], 0, nums)
        return sol


    def recurse(self, sol, cur, i, nums):
        if i == len(nums):
            copy = sorted(cur.copy())
            if copy not in sol:
                sol.append(copy)
            return
        
        cur.append(nums[i])
        self.recurse(sol, cur, i+1, nums)
        cur.pop()
        self.recurse(sol, cur, i+1, nums)
        