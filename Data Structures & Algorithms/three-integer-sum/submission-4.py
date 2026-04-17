class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and a == nums[i - 1]:
                continue
            
            j = i + 1
            k = len(nums) - 1 

            while j < k:
                b = nums[j]
                c = nums[k]

                if a + b + c == 0:
                    sol.append([a, b, c])
                    pc = c
                    while pc == nums[k] and k > j:
                        k -= 1

                    pb = b
                    while pb == nums[j] and j < k:
                        j += 1
            
                elif a + b + c > 0:
                    k -= 1
                else:
                    j += 1
            
        return sol
                





