class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            # while our idx is in range and the thing 
            # we will swap it with isnt the same value
            while 0 <= nums[i] - 1 < n and nums[i] != nums[nums[i] - 1]:
                # swap it into the idx that matches its value
                idx = nums[i] - 1
                nums[i], nums[idx] = nums[idx], nums[i]
        
        # loop over and find first incorrect indeex
        for i in range(n):
            if i + 1 != nums[i]:
                return i + 1

        # if none are wrong its the first thing not in the array
        return n + 1

        