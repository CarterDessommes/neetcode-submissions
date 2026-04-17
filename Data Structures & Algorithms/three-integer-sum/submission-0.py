class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i, j, k = 0, 1, 2
        sol = []

        while i < len(nums) - 2:
            while j < len(nums) - 1:
                while k < len(nums):
                    ni, nj, nk = nums[i], nums[j], nums[k]
                    if ni + nj + nk == 0:
                        sort = sorted([ni, nj ,nk])
                        if sort not in sol:
                            sol.append(sort)
                    k += 1
                j += 1
                k = j + 1
            i += 1
            j = i + 1
            k = i + 2
            
        return sol


        

        # [-1,0,1,2,-1,-4]
        #   i         j         k