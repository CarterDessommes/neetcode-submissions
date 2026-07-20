class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefixs = [1] * len(nums)
        suffixs = [1] * len(nums)
        
        # prefixs is product of everything to the 
        # left of i
        for i in range(1, len(nums)):
            # so everything to the left of i - 1, times the thing
            # to the left of i - 1, gives prefixs[i]
            prefixs[i] = nums[i - 1] * prefixs[i - 1]
        
        # suffixs is the product of everything to the
        # right of i
        for i in reversed(range(len(nums) - 1)):
            # so everything to the right of i + 1,
            # times i + 1 gives suffixs[i]
            suffixs[i] = nums[i + 1] * suffixs[i + 1]
        
        output = [0] * len(nums)
        for i in range(len(nums)):
            output[i] = prefixs[i] * suffixs[i]
        
        return output
        

            