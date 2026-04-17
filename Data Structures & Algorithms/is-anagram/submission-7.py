class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = defaultdict(int)
        for char in s:
            s_dic[char] += 1
        
        t_dic = defaultdict(int)
        for char in t:
            t_dic[char] += 1
        
        return s_dic == t_dic