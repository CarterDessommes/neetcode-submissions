class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sol = []
        self.recurse(sol, [], target, nums, 0)
        return sol
        
    def exists(self, sol, candidate):
        for num in sol:
            if sorted(num) == sorted(candidate):
                return True
        return False

    def recurse(self, sol, cur, target, nums, i):
        if sum(cur) == target:
            sol.append(cur.copy())
            return

        if sum(cur) > target or i >= len(nums):
            return
        
        cur.append(nums[i])
        self.recurse(sol, cur, target, nums, i)
        cur.pop()
        self.recurse(sol, cur, target, nums, i + 1)


        