class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for r in range(len(board)):
            seen = set()
            for c in range(len(board[0])):
                if board[r][c] in seen:
                    return False
                
                if board[r][c] != ".":
                    seen.add(board[r][c])
            
        for c in range(len(board[0])):
            seen = set()
            for r in range(len(board)):
                if board[r][c] in seen:
                    return False
                
                if board[r][c] != ".":
                    seen.add(board[r][c])
        
        idxs = [0, 3, 6]
        for i in idxs:
            for j in idxs:
                seen = set()
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if board[r][c] in seen:
                            return False
                        if board[r][c] != ".":
                            seen.add(board[r][c])
        
        return True





        