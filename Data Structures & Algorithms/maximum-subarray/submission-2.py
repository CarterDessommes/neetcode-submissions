class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        
        sol = max(nums)
        cur = 0

        # pretty hyped I sniper optimal solution, though its not that
        # complex, just applied the same prinicpals as best time to
        # buy and sell stock problem
        for num in nums:
            cur += num

            if cur < 0:
                cur = 0
                continue
            
            sol = max(cur, sol)
        
        return sol