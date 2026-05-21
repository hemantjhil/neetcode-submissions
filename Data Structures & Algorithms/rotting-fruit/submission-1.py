class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        freshOranges=0
        q=deque()
        ROWS,COLS=len(grid),len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    freshOranges+=1
                if grid[i][j]==2:
                    q.append((i,j))
        if freshOranges==0:
            return 0
        
        
        minutes=0
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while q and freshOranges>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for i,j in directions:
                    r1,c1=r+i,c+j
                    if 0<=r1<ROWS and 0<=c1<COLS and grid[r1][c1]==1:
                        grid[r1][c1]=2
                        q.append((r1,c1))
                        freshOranges-=1
            minutes+=1
        return minutes if freshOranges==0 else -1


        