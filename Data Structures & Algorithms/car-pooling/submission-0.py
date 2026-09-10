class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:


        points = []

        # break into simply just up and down amounts at points
        for p, s, e in trips:
            points.append([s, p])
            points.append([e, -p])
        
        # order them in time
        points.sort()

        # process them
        cur = 0
        for point, passengers in points:
            cur += passengers
            # if we ever cant fit everyone return false
            if cur > capacity:
                return False
        
        return True
        