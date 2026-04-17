class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char_map = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }

        result = []
        cur = []
        parsed = [int(x) for x in digits]
        self.recurse(parsed, char_map, result, cur)
        return result
    
    def recurse(self, digits, char_map, result, cur):
        if not digits:
            print(f"appending: {''.join(cur)}")
            if cur:
                result.append(''.join(cur))
            return

        digit = digits.pop(0)


        for char in char_map[digit]:
            cur.append(char) 
            self.recurse(digits, char_map, result, cur)
            cur.pop()

        digits.insert(0, digit)
           
        
        return


            



        