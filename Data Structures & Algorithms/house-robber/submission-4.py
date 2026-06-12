class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # memo represents the max amount of money we can have at
        # each hosue

        n = len(nums)

        if n == 1:
            return nums[0]

        # only need to track two values so 
        # this is a space optmized version
        # time is O(n), space is O(1)
        memo = [0, 0]

        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])

        
        for i in range(2, n):
            val = max(memo[1], memo[0] + nums[i])
            memo[0] = memo[1]
            memo[1] = val


        return memo[1]

            

        