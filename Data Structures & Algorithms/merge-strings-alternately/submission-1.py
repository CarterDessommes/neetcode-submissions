class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []

        idx = 0
        l1, l2 = len(word1), len(word2)

        while idx < min(l1, l2):
            ans.append(word1[idx])
            ans.append(word2[idx])
            idx += 1

        
        while idx < l1:
            ans.append(word1[idx])
            idx += 1 

        while idx < l2:
            ans.append(word2[idx])
            idx += 1 

        return "".join(ans)
        