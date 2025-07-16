def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    COL = len(matrix[0])
    ROW = len(matrix)

    top, bot = 0, ROW - 1

    # Vertical Binary Search
    while top <= bot:
        row = (top + bot) // 2

        if target > matrix[row][-1]:
            top = row + 1
        elif target < matrix[row][0]:
            bot = row - 1
        else:
            break
    
    left, right = 0, COL - 1

    # Horizontal Binary Search
    while left <= right:
        m = (left + right) // 2

        if target > matrix[row][m]:
            left = m + 1
        elif target < matrix[row][m]:
            right = m - 1
        else:
            return True
    
    return False