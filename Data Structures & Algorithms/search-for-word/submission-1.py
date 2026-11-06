class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS = len(board)
        COLS = len(board[0])

        path = set()

        def backtrack(row, col, numWords):
            if numWords == len(word):
                return True
            
            if (
                row >= ROWS or
                col >= COLS or 
                row < 0 or
                col < 0 or
                (row, col) in path or
                word[numWords] != board[row][col] 
            ):
                return False
            
            path.add((row,col))
            res = (
                backtrack(row + 1, col, numWords + 1) or
                backtrack(row, col + 1, numWords + 1) or
                backtrack(row - 1, col, numWords + 1) or
                backtrack(row, col - 1, numWords + 1) 
            )

            path.remove((row,col))
            return res

        for row in range(ROWS):
            for col in range(COLS):
                if backtrack(row, col, 0):
                    return True

        return False