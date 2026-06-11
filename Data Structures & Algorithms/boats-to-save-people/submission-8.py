class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # idea is to sort them, then we can pair them off lightest with heaviest
        people_sorted = self.countingSort(people)

        left = 0
        right = len(people) - 1
        count = 0
        
        while left <= right:
         
            count += 1
         
            weight_right = people_sorted[right]
            weight_left = people_sorted[left] 

            # pair off the lightest person with the heaviest if possible.
            if limit - weight_right >= weight_left:
                left += 1
            
            right -= 1
        
        return count
            

    def countingSort(self, arr):
        # we can use counting sort here because the upper bound of 
        # the things we are sorting is relatively low. People weights < 1000.
        # so the cost of scanning the array is O(n)
        max_value = max(arr)

        counts = [0] * (max_value + 1)

        for value in arr:
            counts[value] += 1
        
        result = []
        for number in range(len(counts)):
            current_number_count = counts[number]
            for j in range(current_number_count):
                result.append(number)
        
        return result


        