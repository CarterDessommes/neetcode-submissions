class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in pairs:
                return [pairs[pair], i]
            else:
                pairs[nums[i]] = i
        return []
        

