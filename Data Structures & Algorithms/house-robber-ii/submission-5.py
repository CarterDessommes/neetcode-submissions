class Solution:


    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # the idea
        return max(self.rob_helper(nums[1:]), self.rob_helper(nums[:-1]))
        
    
    def rob_helper(self, nums):
        n = len(nums)

        if n == 1:
             return nums[0]

        memo = [nums[0], max(nums[0], nums[1])]


        for i in range(2, n):
            
            val = max(memo[1], memo[0] + nums[i])

            memo[0] = memo[1]
            memo[1] = val
        

            
        
        return memo[1]

        


            

        