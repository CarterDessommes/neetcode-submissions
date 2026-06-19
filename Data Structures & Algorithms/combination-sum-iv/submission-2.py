class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = [0] * (target + 1)
        memo[0] = 1

        # pretty simple, build up sol for a current number by 
        # adding all the ways you could get to it.
        for i in range(1, target + 1):
            for num in nums:
                if i - num < 0:
                    continue

                memo[i] += memo[i - num]    


        return memo[target]
        
