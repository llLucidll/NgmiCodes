class Solution:
    def exist(self, board, word)-> bool:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(x, y, curr):
            if board[x][y] != word[curr]:
                return 
            
            path.add((x, y))
            if curr + 1 == len(word):
                return True 

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < ROWS and 0 <= ny < COLS and (nx, ny) not in path:
                    if dfs(nx, ny, curr + 1):
                        return True 
            path.remove((x, y))

        for x in range(ROWS):
            for y in range(COLS):
                path = set()
                if dfs(x, y, 0):
                    return True 
        return False
