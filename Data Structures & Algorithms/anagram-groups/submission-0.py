class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)

        # hash each string by making it a tuple of its letters
        for s in strs:
            freq = [0] * 26

            # faster than sorting, only O(n)
            for char in s:
                freq[ord(char) - ord("a")] += 1
            
            table[tuple(freq)].append(s)
        
        return list(table.values())

        