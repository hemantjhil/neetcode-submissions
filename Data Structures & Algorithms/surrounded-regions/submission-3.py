class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS,COLS=len(board),len(board[0])

        def capture(i,j):
            if i<0 or j<0 or i>=ROWS or j>=COLS or board[i][j]!='O':
                return
            board[i][j]='T'
            capture(i+1,j)
            capture(i-1,j)
            capture(i,j+1)
            capture(i,j-1)
        
        # Step 1: make all boundary 0 to T
        for r in range(ROWS):
            if board[r][0]=='O':
                capture(r,0)
            if board[r][COLS-1]=='O':
                capture(r,COLS-1)
        
        for c in range(COLS):
            if board[0][c]=='O':
                capture(0,c)
            if board[ROWS-1][c]=='O':
                capture(ROWS-1,c)
        
        # step 2 : make all 0 to X
        # step 3: make all T to O
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=='O':
                    board[r][c]='X'
                if board[r][c]=='T':
                    board[r][c]='O'
        






        
        

        