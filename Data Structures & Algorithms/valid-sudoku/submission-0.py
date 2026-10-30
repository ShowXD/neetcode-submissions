class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            col = set()
            metrix = set()

            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])

                if board[j][i] != ".":
                    if board[j][i] in col:
                        return False
                    col.add(board[j][i])
                
                box_row = (i //3) * 3 + j //3
                box_col = (i % 3) * 3 + j % 3
                if board[box_row][box_col] != ".":
                    if board[box_row][box_col] in metrix:
                        return False
                    metrix.add(board[box_row][box_col])
        return True
