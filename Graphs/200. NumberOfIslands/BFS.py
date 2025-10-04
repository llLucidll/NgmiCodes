from collections import deque
def numIslands(grid): 
    ROWS = len(grid)
    COLS = len(grid[0])
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    islands = 0

    def bfs(i, j):
        queue = deque()
        queue.append([i,j])

        while queue:
            xi, xj = queue.popleft()
            for di, dj in directions:
                ci, cj = xi + di, xj + dj

                if (0 > ci or 0 > cj) or (ci >= ROWS or cj >= COLS) or (grid[ci][cj] != "1"):
                    continue 
                
                queue.append([ci, cj])
                grid[ci][cj] = "0"
            grid[xi][xj] = "0" 

    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == "1":
                bfs(i, j) 
                islands += 1
    
    return islands 