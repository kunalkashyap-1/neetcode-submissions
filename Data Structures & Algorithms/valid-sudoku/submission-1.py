class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = {i:set() for i in range(len(board))}
        col = {i:set() for i in range(len(board))}
        gridMap = {i:set() for i in range(len(board))}

        for i in range(len(board)):
            for j in range(len(board)):
                el = board[i][j]
                if el == ".":
                    continue
                if el in row[i] or el in col[j]:
                    return False
                else:
                    row[i].add(el)
                    col[j].add(el)

                gid = (i // 3 ) * 3 + j // 3
                if el in gridMap[gid]:
                    return False
                else:
                    gridMap[gid].add(el)
        
        return True