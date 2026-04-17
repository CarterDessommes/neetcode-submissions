class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        sol = []
        self.recurse(sol, [], 0, nums)
        return sol

    



    def recurse(self, sol, cur, i, nums):
        if i == len(nums):
            sol.append(cur.copy())
            return
        

        # dont add this number
        self.recurse(sol, cur, i+1, nums)

        # do add this number
        cur.append(nums[i])
        self.recurse(sol, cur, i+1, nums)
        cur.pop()

        





        