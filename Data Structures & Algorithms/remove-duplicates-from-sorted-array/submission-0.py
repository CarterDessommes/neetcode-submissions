class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # [1,2,2,2,3,3,4]
        
        prev = None
        w = 0
        i = 0
       
        while i < len(nums):
            num = nums[i]
            if num != prev: 
                nums[w] = num
                prev = num
                w += 1
            i += 1
        return w
                
                
   