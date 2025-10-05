class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        self.area = 0
        result = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(i, j):
            self.area += 1
            grid[i][j] = 0

            for di, dj in directions:
                ci, cj = i + di, j + dj
                if 0 <= ci < ROWS and 0 <= cj < COLS and grid[ci][cj] == 1:
                    dfs(ci, cj)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    self.area = 0
                    dfs(i, j)
                    result = max(result, self.area)
        
        return result 