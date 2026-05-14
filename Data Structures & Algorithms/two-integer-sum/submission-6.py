class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in pairs:
                return [pairs[pair], i]
            pairs[nums[i]] = i
        
        return []
        

