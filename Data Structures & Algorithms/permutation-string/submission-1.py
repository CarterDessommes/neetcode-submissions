class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        # create freq arrays for initial window
        f1 = [0] * 26
        f2 = [0] * 26
        for i in range(len(s1)):
            f1[ord(s1[i]) - ord('a')] += 1
            f2[ord(s2[i]) - ord('a')] += 1
        
        # count up initial matches in window
        matches = 0
        for i in range(26):
            matches += (1 if f1[i] == f2[i] else 0)


        # now, slide the window over 
        l = 0
        for r in range(len(s1), len(s2)):
            # if all freqs are same retur ntrue
            if matches == 26:
                return True
            
            # add new letter on the right
            idx = ord(s2[r]) - ord('a')
            # increase freq count
            f2[idx] += 1
            # if they now match, add one
            if f1[idx] == f2[idx]:
                matches += 1
            # if they matched before, decrement
            # matches
            elif f1[idx] + 1 == f2[idx]:
                matches -= 1
            
            # take letter on the left out
            idx = ord(s2[l]) - ord('a')
            # decresase freq count
            f2[idx] -= 1
            # if it matches add one
            if f1[idx] == f2[idx]:
                matches += 1
            # if it matched before remove one
            elif f1[idx] - 1 == f2[idx]:
                matches -= 1
            
            # move left poniter over
            l += 1
        
        return matches == 26
            

        