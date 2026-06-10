class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        # a, b, c, d are distinct
        # 0 <= a, b, c, d, < n
        # nums[a] + nums[b] + nums[c] + nums[d] == target

        sorted_nums = sorted(nums)
        end = len(sorted_nums) - 1

        result = []

        for i in range(len(sorted_nums)):
            first_fixed = sorted_nums[i]

            if i > 0 and first_fixed == sorted_nums[i - 1]:
                continue

            for j in range(i + 1, len(sorted_nums)):

                l = j + 1
                r = end

                second_fixed = sorted_nums[j]

                if j > i + 1 and sorted_nums[j] == sorted_nums[j - 1]:
                    continue

                while l < r:
                    left_val = sorted_nums[l]
                    right_val = sorted_nums[r]

                    cur_sum = left_val + right_val + first_fixed + second_fixed

                    if cur_sum < target:
                        l += 1
                    elif cur_sum > target:
                        r -= 1
                    else:
                        result.append((left_val, right_val, first_fixed, second_fixed))
                      
                        while l <= end and sorted_nums[l] == left_val:
                            l += 1
                        while r >= 0 and sorted_nums[r] == right_val:
                            r -= 1
            
        return result

                    


                

        