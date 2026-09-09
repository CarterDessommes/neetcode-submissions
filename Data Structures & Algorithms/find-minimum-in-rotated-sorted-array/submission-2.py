class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            mid = nums[m]
            right = nums[r]
            left = nums[l]

            if mid > right:
                l = m + 1
            else: 
                r = m 


        
        return nums[l]



