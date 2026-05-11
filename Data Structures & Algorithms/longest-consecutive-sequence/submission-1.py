class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0 

        for num in nums:
            if (num - 1) not in s:
                i = num
                while i in s:
                    i += 1
            
                best = max(i - num, best)

        return best


            


        