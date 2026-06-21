class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        # two cases, either it wraps or it doesn't

        # the case where it doesnt wrap, just regular kadanes
        cur_max = 0
        sol_max = max(nums)

        for num in nums:
            cur_max += num

            if cur_max < 0:
                cur_max = 0
                continue
            
            sol_max = max(sol_max, cur_max)
        
        # the case where it does wrap, we want to take out the smallest subarray!
        # like if we have the overall value, we want to take out the smallest possible subarray
        # in order to increase this.
        cur_min = 0
        sol_min = min(nums)

        for num in nums:
            cur_min += num

            if cur_min > 0:
                cur_min = 0
                continue
            
            sol_min = min(sol_min, cur_min)
        
        # this is for the edge case where all the inputted values are 0, 
        # because in this case total - min = 0 which would represent
        # an empty subarray which is not allowed. aka the case where the 
        # min subarray is the entire array.
        if sol_max < 0:
            return sol_max
        
        return max(sol_max, sum(nums) - sol_min)

            
