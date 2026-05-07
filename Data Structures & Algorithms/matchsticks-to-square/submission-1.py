class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sides = [0, 0, 0, 0]
        target = sum(matchsticks) // 4
        cur = 0
        if sum(matchsticks) % 4 != 0:
            return False

        matchsticks.sort(reverse=True)
        return self.recurse(matchsticks, sides, cur, target)


    def recurse(self, matchsticks, sides, cur, target): 
        if cur == len(matchsticks):
            for side in sides:
                if side != target:
                    return False
            return True
        

        matchstick = matchsticks[cur]

        # try placing in the 4 sides
        for j in range(4):
            # choose
            sides[j] += matchstick
            
            # explore
            if sides[j] <= target:
                if self.recurse(matchsticks, sides, cur + 1, target):
                    return True

            # un choose
            sides[j] -= matchstick
         
        return False
        