class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        m = -1
        for n in sorted(nums):
            if n != m + 1:
                return m + 1
            m = m + 1
        
        return m + 1


        