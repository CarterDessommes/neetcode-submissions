class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float("inf")

        # sliding window, shrink left if over
        # otherwise just keep movign right
        # tracking smallest size we see the whole time
        # that satisfies constraints
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        
        return 0 if res == float("inf") else res


        