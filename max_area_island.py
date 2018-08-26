class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_area=0
        m=len(grid)
        n=len(grid[0])
        
        def dfs(x,y):
            if 0<=x<m and 0<=y<n and grid[x][y]==1:
                grid[x][y]=0
                return dfs(x-1,y)+dfs(x+1,y)+dfs(x,y-1)+dfs(x,y+1)+1
            return 0
        
        for x in range(0,m):
            for y in range(0,n):
                if  grid[x][y]==1:
                    max_area=max(max_area,dfs(x,y))
        return max_area

        


