class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []
        n = len(nums)
        self.recurse(sol, [], nums, n)
        return sol

    
    def recurse(self, sol, cur, nums, n):
        if len(cur) == n:
            sol.append(cur.copy())
            return
        
        for i, num in enumerate(nums):
            cur.append(num)
            copy = nums.copy()
            copy.pop(i)
            self.recurse(sol, cur, copy, n)
            cur.pop()
        
            





        