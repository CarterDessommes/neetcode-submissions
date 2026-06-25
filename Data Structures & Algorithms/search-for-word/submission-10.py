class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for y in range(len(board)):
            for x in range(len(board[0])):
                if self.recurse(board, word, x, y, 0):
                    return True

        return False    

    def recurse(self, board, word, x, y, i):

        if (x >= len(board[0]) or y >= len(board) or 
            x < 0 or y < 0 or board[y][x] == '#' or board[y][x] != word[i]):
            return False

        # need this to make sure we don't infiinite loop
        board[y][x] = '#'

        if i == len(word) - 1:
            return True
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for dx, dy in directions:
            if self.recurse(board, word, x + dx, y + dy, i + 1):
                return True

        board[y][x] = word[i]
        return False
        
        