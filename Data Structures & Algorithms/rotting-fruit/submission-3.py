class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS,COLS=len(grid),len(grid[0])
        visit=set()
        q=deque()
        minute=0
        freshOrange=0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]==1:
                    freshOrange+=1
                if grid[i][j]==2:
                    q.append((i,j))
        if freshOrange==0:
            return 0
        
        direction=[[-1,0],[1,0],[0,1],[0,-1]]
        while q and freshOrange>0:
            for i in range(len(q)):
                r,c=q.popleft()
                for j,k in direction:
                    j1,k1=r+j,c+k
                    if  0<=j1<ROWS and 0<=k1<COLS and grid[j1][k1]==1:
                        grid[j1][k1]=2
                        q.append((j1,k1))
                        freshOrange-=1
            minute+=1
        return minute if freshOrange==0 else -1
        