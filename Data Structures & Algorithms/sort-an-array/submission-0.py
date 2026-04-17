class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[mid:])
        right = self.sortArray(nums[:mid])
        return self.merge(left, right)
    
    def merge(self, left, right):
        i = j = 0
        sol = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sol.append(left[i])
                i += 1
            else:
                sol.append(right[j])
                j += 1
        
        sol.extend(left[i:])
        sol.extend(right[j:])
        return sol





        

        


        