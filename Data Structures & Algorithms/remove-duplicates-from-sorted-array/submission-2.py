class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [1,2,3,4,2,3,3,4]
        #.       ^         ^
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l
                
                
   