class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        cur = 0

        for num in nums:
            if count == 0:
                cur = num
            if num == cur:
                count += 1
            else:
                count -= 1
        return cur