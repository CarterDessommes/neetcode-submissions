class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)

        l = [x[0] for x in count.most_common(k)]

        return l  