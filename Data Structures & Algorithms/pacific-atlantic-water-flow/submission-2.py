class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        res=[]
        ROWS,COLS=len(heights),len(heights[0])

        def dfs(i,j,prev,visit):
            if min(i,j)<0 or i>=ROWS or j>=COLS or heights[i][j]<prev or (i,j) in visit:
                return 
            visit.add((i,j))
            dfs(i+1,j,heights[i][j],visit)
            dfs(i-1,j,heights[i][j],visit)
            dfs(i,j+1,heights[i][j],visit)
            dfs(i,j-1,heights[i][j],visit)
        
        pac,atl=set(),set()
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
        

