class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        freq = [[] for i in range(len(nums) + 1)]

        for key, value in count.items():
            freq[value].append(key)
        
        res = []
        for i in reversed(range(len(freq))):
            
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        return res
        

          