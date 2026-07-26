class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        # set to one as we will immediately set it
        curMin, curMax = 1, 1

        for num in nums:
            # save because we are going to change it
            tmp = num * curMax 
            # must compare to all three possibilities
            # for min and max because of negatives
            curMax = max(num * curMax, num * curMin, num)
            curMin = min(tmp, num * curMin, num)
            res = max(curMax, res)
        
        return res