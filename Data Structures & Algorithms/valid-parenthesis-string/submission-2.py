class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = 0
        leftMax = 0
        for i in range(len(s)):
            if s[i] == "(":
                leftMin += 1
                leftMax += 1
            elif s[i] == ")":
                leftMin -= 1
                leftMax -= 1
            else:
                leftMin -= 1
                leftMax += 1

            if leftMax < 0:
                return False
            
            if leftMin < 0:
                leftMin = 0
                # if we have extra closings, which we must from *
                # as otherwise the left max above would have returned false
                # we can just make them "" to make our min 0.
            
        return leftMin == 0

                

        