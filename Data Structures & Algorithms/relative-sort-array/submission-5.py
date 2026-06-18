class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # counting sort
        max_val = max(arr1)

        count = [0] * (max_val + 1)

        for num in arr1:
            count[num] += 1
        
        res = []
        # modification to process the numbers in arr2 first
        for num in arr2:
            # add count[num] num's to our solution
            res += [num] * count[num]
            # set to 0 so when we process again in the below loop it 
            # doesnt double count
            count[num] = 0
        
        for num in range(len(count)):
            res += [num] * count[num]

        return res