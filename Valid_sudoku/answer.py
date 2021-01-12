class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n, m = 3, 3
        ## row and column check
        for i in range(n * m):
            row_set = set()
            col_set = set()
            for j in range(n * m):
                if board[i][j] != ".":
                    if board[i][j] in row_set:
                        return False
                    row_set.add(board[i][j])
                if board[j][i] != ".":
                    if board[j][i] in col_set:
                        return False
                    col_set.add(board[j][i])
            # print(row_set, col_set)
        # sub-boxes check
        for sub_row in range(n):
            for sub_col in range(m):
                box_set = set()
                for r in range(n):
                    for c in range(m):
                        if board[sub_row*n + r][sub_col*m + c] != ".":
                            if board[sub_row*n + r][sub_col*m + c] in box_set:
                                return False
                            box_set.add(board[sub_row*n + r][sub_col*m + c])
                # print(box_set)
        return True
