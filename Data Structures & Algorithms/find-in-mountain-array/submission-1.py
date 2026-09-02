class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l = 1
        r = mountainArr.length() - 2

        while l <= r:
            m = (l + r) // 2

            valL = mountainArr.get(m-1)
            valR = mountainArr.get(m+1)
            valM = mountainArr.get(m)

            # in left side
            if valL < valM < valR:
                l = m + 1
            # in right side    
            elif valL > valM > valR:
                r = m - 1
            else:
                break
        
        peak = m

        l = 0
        r = peak - 1

        # serach left part of array 
        # ascending
        while l <= r:
            m = (l + r) // 2

            val = mountainArr.get(m)

            # in left side
            if val < target:
                l = m + 1
            # in right side    
            elif val > target:
                r = m - 1
            else:
                return m
        
        l = peak
        r = mountainArr.length() - 1

        # right part of the array is ascending
        while l <= r:
            m = (l + r) // 2

            val = mountainArr.get(m)

            # in left side
            if val < target:
                r = m - 1
            # in right side    
            elif val > target:
                l = m + 1
            else:
                return m
        
        return -1



            





        