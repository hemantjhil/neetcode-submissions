class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS,COLS=len(board),len(board[0])

        def capture(i,j):
            if i<0 or j<0 or i==ROWS or j==COLS or board[i][j]!="O" :
                return
            board[i][j]="T"
            capture(i+1,j)
            capture(i-1,j)
            capture(i,j+1)
            capture(i,j-1)

        # step 1 make unsurround O to T (unsurrounded are border ones)
        for r in range(ROWS):
            if board[r][0]=="O":
                capture(r,0)
            if board[r][COLS-1]=="O":
                capture(r,COLS-1)
        
        for c in range(COLS):
            if board[0][c]=="O":
                capture(0,c)
            if board[ROWS-1][c]=="O":
                capture(ROWS-1,c)


        # step 2 make all O to X
        # step 3 make all T back to O
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="T":
                    board[i][j]="O"


        
        

        