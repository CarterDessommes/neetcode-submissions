class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        i = 0
        while i < len(arr) and arr[i] < x:
            i += 1
        


        res = []
        l = i - 1
        r = i
        while len(res) < k and l >= 0 and r < len(arr):
            a = arr[l]
            b = arr[r]

            if abs(a - x) < abs(b - x) or ((abs(a - x) == abs(b - x)) and a < b):
                res.append(a)
                l -= 1
            else:
                res.append(b)
                r += 1
        
        while len(res) < k and l >= 0:
            res.append(arr[l])
            l -= 1
        
        while len(res) < k and r < len(arr):
            res.append(arr[r])
            r += 1
        
        return sorted(res)




        