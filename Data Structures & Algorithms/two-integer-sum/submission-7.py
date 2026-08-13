class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        pairs = {}
        for i in range(len(nums)):
            cur = nums[i]
            pair = target - cur
            if pair in pairs:
                return [pairs[pair], i]
            
            pairs[cur] = i
        

        

