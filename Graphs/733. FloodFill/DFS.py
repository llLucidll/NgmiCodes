class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):
        ROWS = len(image)
        COLS = len(image[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        seen = set()


        prev = image[sr][sc]

        def dfs(x, y):
            if image[x][y] == prev:
                image[x][y] = color
                seen.add((x, y))
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < ROWS and 0 <= ny < COLS and (nx, ny) not in seen:
                        dfs(nx, ny)
            else:
                return 


        dfs(sr, sc)
        return image


