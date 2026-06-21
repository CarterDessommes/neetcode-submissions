class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        
        sol = max(nums)
        cur = 0

        for num in nums:
            cur += num

            if cur < 0:
                cur = 0
                continue
            
            sol = max(cur, sol)
        
        return sol