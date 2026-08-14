class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        # key insight is prefixSum[j] - prefixSum[i] = k
        # then subarray from index i+1 to j has sum k

        # in other words we can represent every subarray
        # as the difference of two other subarrays

        # we will go through the whole array
        # maintaing a running sum and at each num asking
        # have we seen a sum that we can subtract off our 
        # running sum to get k?

        res = 0
        curSum = 0
        for num in nums:
            curSum += num

            # we are looking for a prefix of this sum
            diff = curSum - k
            # add any we have
            res += prefix_sum[diff]
            prefix_sum[curSum] += 1

        
        return res


        