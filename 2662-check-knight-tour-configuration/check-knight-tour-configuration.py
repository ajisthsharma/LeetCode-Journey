class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        n=len(grid)

        if grid[0][0]!=0 or n<5:
            return False

        pos=[None]*(n*n)

        for i in range(n):
            for j in range(n):
                pos[grid[i][j]]=(i,j)

        for k in range(n*n -1):
            x1,y1=pos[k]
            x2,y2=pos[k+1]
            dx,dy=abs(x1-x2),abs(y1-y2)

            if not ((dx==2 and dy==1) or (dx==1 and dy==2)):
                return False

        return True