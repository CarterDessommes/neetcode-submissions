class Solution:
    def findMin(self, nums: List[int]) -> int:
    
        l = 0
        r = len(nums) - 1
        while l < r:
            m = l + (r - l) // 2

            # then we know split is on the left
            # so we can move our focus left.
            # keep m included as it could be
            # the value 
            if nums[m] < nums[r]:
                r = m
            # otherwise the split is on the right
            # so move focus right. We know, 
            # in this case that m cannot be 
            # the min, as the first condition
            # would be true.
            else:
                l = m + 1
        
        # if we are here, l = r
        return nums[l]
            
            



