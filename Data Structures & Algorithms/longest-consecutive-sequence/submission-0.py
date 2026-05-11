class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0 

        for num in nums:
            if (num - 1) not in s:
                i = num
                print(f"{i} is start,")
                while i in s:
                    print(f"{i} in set")
                    i += 1
            
                print(f"{i - num} compared to {best}")
                best = max(i - num, best)

        return best


            


        