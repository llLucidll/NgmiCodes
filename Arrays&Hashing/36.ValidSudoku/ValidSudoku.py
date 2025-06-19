class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # The grid has 3x3 subgrids.
        cols = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[]}
        subgrids = {0:[], 1:[], 2:[]}
        reset = 0
        ROWS = len(board)

        for i in range(ROWS):
            row = board[i]
            current = {}
            #To reset our subgrid collection when we go down 3 columns
            if i//3 > reset:
                subgrids = {0:[], 1:[], 2:[]}
                reset = i//3
            for j in range(len(row)):
                #First we validate the entry
                if row[j] == ".":
                    continue
    
                value = int(row[j])
                # Add the value to our current
                if current.get(value, 0) == 1:
                    return False
                current[value] = 1
                # Add the value to our column
                if value in cols[j]:
                    return False
                cols[j].append(value)
                # Add the value to our subgrids
                sub = j//3
                if value in subgrids[sub]:
                    return False
                subgrids[sub].append(value)
            
        return True