class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        def backtrack(i,j,k):
            if i<0 or j<0 or i>=rows or j>=cols:
                return False
            if board[i][j]!=word[k]:
                return False
            if k==len(word)-1:
                return True
            original=board[i][j]
            board[i][j]="#"
            found=(
                backtrack(i+1,j,k+1) or
                backtrack(i,j+1,k+1) or
                backtrack(i-1,j,k+1) or
                backtrack(i,j-1,k+1)
            )
            board[i][j]=original
            return found

        for i in range(rows):
            for j in range(cols):
                if(backtrack(i,j,0)):
                    return True
        return False