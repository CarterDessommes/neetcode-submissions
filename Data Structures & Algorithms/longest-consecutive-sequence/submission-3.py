class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)

        best = 0
        for num in s:
            if num - 1 in s:
                continue
            
            cur = 0
            while num + cur in s:
                cur += 1
            
            best = max(best, cur)
        
        return best



            


        