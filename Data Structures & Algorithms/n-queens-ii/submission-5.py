class Solution:
    def totalNQueens(self, n: int) -> int:
        def solveNQueens(row: int, cols: set, diag1: set, diag2: set) -> int:
            if row == n:
                return 1
            solutions = 0
            for col in range(n):
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)
                solutions += solveNQueens(row + 1, cols, diag1, diag2)
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)
            return solutions
        
        return solveNQueens(0, set(), set(), set())
