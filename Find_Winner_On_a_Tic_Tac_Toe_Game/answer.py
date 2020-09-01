class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        # A=> 0, B=> 1
        boards = [[-1 for _ in range(3)] for _ in range(3)]
        
        ## progressing game
        for i in range(len(moves)):
            move = moves[i]
            if i % 2 == 0:
                boards[move[0]][move[1]] = 0
            else:
                boards[move[0]][move[1]] = 1
        
        ## checking winner
        for i in range(3):
            row = boards[i]
            if row[0] == row[1] == row[2]:
                if row[0] == 0:
                    return 'A'
                if row[0] == 1:
                    return 'B'
        for j in range(3):
            if boards[0][j] == boards[1][j] == boards[2][j]:
                if boards[0][j] == 0:
                    return 'A'
                if boards[0][j] == 1:
                    return 'B'
            
        if boards[0][0] == boards[1][1] == boards[2][2]:
            if boards[0][0] == 0:
                return 'A'
            if boards[0][0] == 1:
                return 'B'
        if boards[0][2] == boards[1][1] == boards[2][0]:
            if boards[0][2] == 0:
                return 'A'
            if boards[0][2] == 1:
                return 'B'
        
        ## checking if pending
        if len(moves) < 9:
            return 'Pending'
        return "Draw"
        
