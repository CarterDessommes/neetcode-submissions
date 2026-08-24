class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t == "":
            return ""
        
        # our target freqs
        target = Counter(t)
        # freqs of our window
        window = Counter()

        # number of character requirements
        need = len(target)

        # number of character requiements winow satisfies
        have = 0
        

        best_len = float("inf")
        best_l = 0

        l = 0
        for r in range(len(s)):
            char = s[r]
            window[char] += 1
            
            # adding this char satisfies a req, increase count
            if char in target and window[char] == target[char]:
                have += 1

            # if all reqs are satisfied shrink the window untill its invalid
            while have == need:
                cur_len = r - l + 1
                if best_len > cur_len:
                    best_len = cur_len
                    best_l = l

                left_char = s[l]
                
                # if removing leftmost char makes the window invalid, decrease
                # the requirements count
                if (left_char in target and window[left_char] == target[left_char]):
                    have -= 1
                
                # remove the left char
                window[left_char] -= 1
                l += 1

                
        # if we never saw valid return emptry string
        if best_len == float("inf"):
            return ""
        
        # return best substring found
        return s[best_l:best_l + best_len]