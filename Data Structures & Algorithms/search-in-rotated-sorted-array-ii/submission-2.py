class Solution:
    def search(self, nums: List[int], target: int) -> bool:


        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            cur = nums[m]
            right = nums[r]
            left = nums[l]

            # because we exclude m from all paths moving forward
            if cur == target:
                return True

            if left < cur:
                if left <= target < cur:
                    r = m - 1
                else:
                    l = m + 1

            elif left > cur:
                if cur < target <= right:
                    l = m + 1
                else: 
                    r = m - 1
            else:
                l += 1
        
        return nums[l] == target