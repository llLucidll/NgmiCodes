from collections import deque

class Solution:
    def floodFill(self, image, sr: int, sc: int, color: int):

        ROWS = len(image)
        COLS = len(image[0])

        seen = set()

        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        queue = deque([(sr, sc)])
        seen.add((sr, sc))
        prev = image[sr][sc]
        while queue:
            x, y = queue.popleft()
            seen.add((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < ROWS and 0 <= ny < COLS and image[nx][ny] == prev and (nx, ny) not in seen:
                    queue.append((nx, ny))

            image[x][y] = color

        return image 

