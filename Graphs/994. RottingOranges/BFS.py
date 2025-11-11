from collections import deque
def orangesRotting(grid: list[list[int]]) -> int:
    rotten_q = deque()
    fresh_q = deque()
    ROWS = len(grid)
    COLS = len(grid[0])
    fresh = 0
    time = -1

    directions = [[1,0], [-1,0], [0,1], [0,-1]]

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 2:
                rotten_q.append([r,c])
            elif grid[r][c] == 1:
                fresh += 1

    # handling the edge case where there are no fresh oranges to rot
    if fresh == 0:
        return 0 
    
    while rotten_q or fresh_q:
        while rotten_q:
            r, c = rotten_q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1):
                    fresh_q.append([nr,nc])
                
        if not rotten_q:
            time += 1
        
        while fresh_q:
            r, c = fresh_q.popleft()
            grid[r][c] = 2
            rotten_q.append([r,c])

    # Checking if there are any fresh oranges left
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                return -1
    return time 
