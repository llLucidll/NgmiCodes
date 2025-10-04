def numIslands(grid:list[list[str]]):
    islands = 0

    ROWS = len(grid)
    COLS = len(grid[0])
    DIR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    

    def dfs(i: int, j: int):
        # Assume our dfs is triggered only when the node is "1"
        grid[i][j] = "0"
        for di, dj in DIR:
            ni, nj = i + di, j + dj
            if 0 <= ni < ROWS and 0 <= nj < COLS and grid[ni][nj] == "1":
                dfs(i, j)

    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == "1":
                dfs(i, j)
                islands += 1
    
    return islands 