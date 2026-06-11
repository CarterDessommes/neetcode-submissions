class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:


        l = 0 
        r = len(numbers) - 1

        while l < r:
            
            left_val = numbers[l]
            right_val = numbers[r]

            if left_val + right_val < target:
                l += 1
            elif left_val + right_val > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        