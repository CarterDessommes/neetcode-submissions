class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for str in strs:
            freq = [0] * 26
            for ch in str:
                freq[ord(ch) - ord('a')] += 1
            
            anagrams[tuple(freq)].append(str)
        
        return list(anagrams.values())
            




        