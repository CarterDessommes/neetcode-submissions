class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        target = len(nums) // 3

        counts = Counter(nums)

        sol = []
        for val in counts:
            if counts[val] > target:
                sol.append(val)
        
        return sol
        