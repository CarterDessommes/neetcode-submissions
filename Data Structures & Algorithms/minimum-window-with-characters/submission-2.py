class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        
        target = Counter(t)
        window = Counter()

        need = len(target)
        have = 0
        

        best_len = float("inf")
        best_l = 0

        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] += 1

            if char in target and window[char] == target[char]:
                have += 1

            while have == need:
                cur_len = r - l + 1
                if best_len > cur_len:
                    best_len = cur_len
                    best_l = l

                left_char = s[l]
                
                if (left_char in target and window[left_char] == target[left_char]):
                    have -= 1
                
                window[left_char] -= 1
                l += 1

                
                
        if best_len == float("inf"):
            return ""
        
        return s[best_l:best_l + best_len]