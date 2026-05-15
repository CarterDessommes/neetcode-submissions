class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        best = 0
        for num in nums:
            if num - 1 in nums:
                continue
            
            cur = 0
            while num + cur in nums:
                cur += 1
            
            best = max(best, cur)
        
        return best



            


        