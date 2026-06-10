class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)

        end = len(nums) - 1

        result = []
        print(sorted_nums)

        for i in range(len(sorted_nums)):
            fixed = sorted_nums[i]
            l = i + 1
            r = end

            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            while l < r:
                if l < 0 or r < 0 or l > end or r > end:
                    break

                if fixed > 0:
                    break

                r_val = sorted_nums[r]
                l_val = sorted_nums[l]

                cur_sum = fixed + r_val + l_val
                
                if cur_sum > 0:
                    r -= 1
                elif cur_sum < 0:
                    l += 1
                else:
                    result.append((fixed, sorted_nums[r], sorted_nums[l]))

                    while r >= 0 and sorted_nums[r] == r_val:
                        r -= 1
                    while l <= end and sorted_nums[l] == l_val:
                        l += 1
                
        return result
