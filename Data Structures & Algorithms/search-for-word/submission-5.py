class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for y in range(len(board)):
            for x in range(len(board[0])):
                if self.recurse(board, word, x, y, [], set()):
                    return True

        return False    

    
    def recurse(self, board, word, x, y, cur, visited):

        if x >= len(board[0]) or y >= len(board) or x < 0 or y < 0:
            return False

        if (x, y) in visited:
            return False

        cur.append(board[y][x])

        visited.add((x, y))

        if "".join(cur) == word:
            return True
        
        if self.recurse(board, word, x + 1, y, cur, visited):
            return True 

        if self.recurse(board, word, x, y + 1, cur, visited):
            return True

        if self.recurse(board, word, x - 1, y, cur, visited):
            return True

        if self.recurse(board, word, x, y - 1, cur, visited):
            return True

        visited.remove((x, y))
        cur.pop()
        return False
        
        