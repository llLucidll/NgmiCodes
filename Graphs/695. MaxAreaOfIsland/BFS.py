from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        directions  = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        max_area = 0
        self.area = 0

        def bfs(i, j):
            grid[i][j] = 0
            self.area += 1
            queue = deque([[i, j]])

            while queue:
                ci, cj = queue.popleft()
                for di, dj in directions:
                    ni, nj = ci + di, cj + dj 
                    if (ni < 0 or nj < 0) or (ni >= ROWS or nj >= COLS) or (grid[ni][nj] == 0):
                        continue 
                    grid[ni][nj] = 0
                    queue.append([ni, nj])
                    self.area += 1 
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    self.area = 0
                    bfs(i, j)
                    max_area = max(max_area, self.area)
        
        return max_area
