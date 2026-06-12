class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # memo represents the max amount of money we can have at
        # each hosue

        n = len(nums)

        if n == 1:
            return nums[0]

        memo = [0] * n

        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])

        
        for i in range(2, len(nums)):
            val = max(memo[i - 1], memo[i - 2] + nums[i])
            memo[i] = val

        


        return memo[n - 1]

            

        