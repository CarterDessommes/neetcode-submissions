class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1

        # key insight is prefixSum[j] - prefixSum[i] = k
        # then subarray from index i+1 to j has sum k
        res = 0
        curSum = 0
        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefix_sum[diff]
            
            prefix_sum[curSum] += 1

        
        return res


        