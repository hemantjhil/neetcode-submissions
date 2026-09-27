class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS =len(board),len(board[0])
        def capture(i,j):
            if i<0 or j<0 or i==ROWS or j==COLS or board[i][j]!='O':
                return
            board[i][j]='T'
            capture(i+1,j)
            capture(i-1,j)
            capture(i,j+1)
            capture(i,j-1)

        for i in range(ROWS):
            if board[i][0]=='O':
                capture(i,0)
            if board[i][COLS-1]=='O':
                capture(i,COLS-1)
        for j in range(COLS):
            if board[0][j]=='O':
                capture(0,j)
            if board[ROWS-1][j]=='O':
                capture(ROWS-1,j)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='T':
                    board[i][j]='O'
        
        