class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1

        sol = 0
        curSum = 0
        for num in nums:
            curSum += num

            diff = curSum - k

            sol += prefix_sums[diff]

            prefix_sums[curSum] += 1
        
        return sol



        