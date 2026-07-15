class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        xorr = n
        # this solution relies on the fact that
        # x ^ x = x and x ^ 0 = 0
        for i in range(n):
            
            xorr ^= i ^ nums[i]
        
        return xorr

        