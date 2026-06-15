class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [1] * n

        # the idea is that we build up the longest increasing subsequences
        # by, for each number, looking at all the numbers in the array smaller 
        # than the current number and then just taking the max value we 
        # can get
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    memo[i] = max(memo[i], memo[j] + 1)
        
        return max(memo)


        