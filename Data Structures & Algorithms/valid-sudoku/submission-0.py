class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valcols = collections.defaultdict(set)
        valrows = collections.defaultdict(set)
        valsquares = collections.defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j]!=".":

                    if board[i][j] in valcols[j] or board[i][j] in valrows[i]or board[i][j] in valsquares[(i//3,j//3)]:
                        return False



                    valcols[j].add(board[i][j])
                    valrows[i].add(board[i][j])
                    valsquares[(i//3,j//3)].add(board[i][j])
        
        print(valcols)
        print(valrows)
        print(valsquares)
        return True