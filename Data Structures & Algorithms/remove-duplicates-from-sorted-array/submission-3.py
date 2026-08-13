class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        # maintain a left writer pointer
        l = 1
        # move through the array, writing to the writer
        # if we see a unique value
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        # the inex of our writer will be the same value we 
        # would want an array up to
        return l
                
                
   