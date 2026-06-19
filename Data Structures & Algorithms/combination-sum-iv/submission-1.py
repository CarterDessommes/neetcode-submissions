class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:


        memo = [0] * (target + 1)

        memo[0] = 1

        # pretty simple, add to it all 
        for i in range(1, target + 1):
            for num in nums:
                if i - num < 0:
                    continue

                memo[i] += memo[i - num]    


        return memo[target]
        
