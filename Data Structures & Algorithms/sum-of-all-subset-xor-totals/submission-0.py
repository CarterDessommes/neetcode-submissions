class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # XOR makes a bit 1 when an odd number of selected elements have that bit.
        res = 0
        for num in nums:
            res |= num
        return res << (len(nums) - 1)

        