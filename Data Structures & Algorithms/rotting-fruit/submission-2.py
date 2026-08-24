class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q=deque()
        ROWS,COLS=len(grid),len(grid[0])
        freshOrange=0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    freshOrange+=1
                if grid[r][c]==2:
                    q.append((r,c))
        
        if freshOrange==0:
            return 0

        minutes=0
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while q and freshOrange>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for i,j in directions:
                    r1,c1=r+i,c+j
                    if 0<=r1<ROWS and 0<=c1<COLS and grid[r1][c1]==1:
                        grid[r1][c1]=2
                        q.append((r1,c1))
                        freshOrange-=1
            minutes+=1
        
        return minutes if freshOrange==0 else -1
