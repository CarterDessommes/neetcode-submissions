class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n
        # this solution relies on the fact that
        # x ^ x = x and x ^ 0 = 0
        # we loop through all possible values, 
        # xorring each one together
        # because if we do this the only one that will
        # remain is the one that doesnt have a duplicate
        for i in range(n):
            # this is okay because the order is irrelevant
            # like 2 ^ 3 then ^ 2 = 3
            # this way we are sure we try every 
            # possible value with every value in the 
            # array
            xorr ^= i ^ nums[i]
        
        return xorr

        