class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit=set()
        def dfs(i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]==0 or (i,j) in visit:
                return 0
            visit.add((i,j))
            return (1+dfs(i+1,j)+ dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1))

        area=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area=max(area,dfs(i,j))
        return area

        