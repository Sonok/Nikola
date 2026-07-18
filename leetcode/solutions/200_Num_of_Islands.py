from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(1,0), (-1,0), (0, 1), (0, -1)]
        n, m = len(grid), len(grid[0])

        def dfs(i, j): # you visit i,j and the rest of the grid
            q = deque()
            q.append((i,j))
            while(q):
                x,y = q.popleft()
                grid[x][y] = "0"
                for dx, dy in dirs:
                    nx, ny = x+dx,y+dy
                    if(0 <= nx < n and 0 <= ny < m and grid[nx][ny] == "1"):
                        grid[nx][ny] = "0"
                        q.append((nx, ny))
        
        count = 0 
        for i in range(n):
            for j in range(m):
                if(grid[i][j] == "1"):
                    count += 1
                    dfs(i, j)
        return count

