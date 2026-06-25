class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # trying every starting point
        for y in range(len(board)):
            for x in range(len(board[0])):
                if self.recurse(board, word, x, y, 0):
                    return True

        return False    

    def recurse(self, board, word, x, y, i):

        # if we are out of range or if we have seen this before, or if its not
        # the right letter
        if (x >= len(board[0]) or y >= len(board) or 
            x < 0 or y < 0 or board[y][x] == '#' or board[y][x] != word[i]):
            return False

        # need this to make sure we don't infinite loop
        # choose
        board[y][x] = '#'

        # if the length mathces and so does every letter we know we 
        # found it
        if i == len(word) - 1:
            return True
        
        # explore
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for dx, dy in directions:
            if self.recurse(board, word, x + dx, y + dy, i + 1):
                return True

        # un choose 
        board[y][x] = word[i]
        return False
        
        