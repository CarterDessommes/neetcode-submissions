class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []
        
        for point in points:
            heapq.heappush(heap, (math.sqrt(point[0]**2 + point[1]**2), point))
        
        smallest = heapq.nsmallest(k, heap)

        return [x[1] for x in smallest]


        