
def solve(board: list[list[str]]) -> None:
    directions = [[1,0], [-1,0], [0,-1], [0,1]]
    ROWS = len(board)
    COLS = len(board)

    def capture():
        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS-1 or c == 0 or c == COLS-1 and board[r][c] == "O"):
                    queue.append((r,c))
        
        while queue:
            r, c = queue.popleft()
            if board[r][c] == "O":
                board[r][c] = "T"
                for dr, dc in directions:
                    nr, nc = r + dr, c + nc 
                    if (0 <= nr < ROWS and 0 <= nc < COLS):
                        queue.append((nr, nc))
    
    capture()
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "T":
                board[r][c] = "O"


                