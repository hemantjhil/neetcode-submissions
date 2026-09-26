class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        pac,atl=set(),set()
        ROWS,COLS=len(heights),len(heights[0])
        visit=set()
        def dfs(i,j,prev,visit):
            if i<0 or j<0 or i==ROWS or j==COLS or (i,j) in visit or heights[i][j]<prev:
                return
            visit.add((i,j))
            dfs(i,j+1,heights[i][j],visit)
            dfs(i,j-1,heights[i][j],visit)
            dfs(i+1,j,heights[i][j],visit)
            dfs(i-1,j,heights[i][j],visit)
        
        res=[]
        for r in range(ROWS):
            dfs(r,0,heights[r][0],pac)
            dfs(r,COLS-1,heights[r][COLS-1],atl)
        
        for c in range(COLS):
            dfs(0,c,heights[0][c],pac)
            dfs(ROWS-1,c,heights[ROWS-1][c],atl)
        
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i,j])
        return res

        