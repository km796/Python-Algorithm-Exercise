from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        ans = set()
        board = [[0]*n for _ in range(n)]

        def backtrack(path, row):
            if row == n:
                tPath = tuple(map(tuple, path))
                ans.add(tPath)
                return
            for i in range(n):
                if self.check(path, row, i):
                    path[row][i] = 1
                    backtrack(path, row+1)
                    path[row][i] = 0
        backtrack(board, 0)
        return list(map(self.convert, ans))

    def check(self, path, i, j):
        for k in range(len(path)):
            dirs = [[i+k,j],[i-k,j],[i,j+k],[i,j-k],[i+k,j+k],[i-k,j-k],[i+k,j-k],[i-k,j+k]]
            for dir in dirs:
                if 0 <= dir[0] < len(path) and 0 <= dir[1] < len(path) and path[dir[0]][dir[1]] == 1:
                    return False
        return True
    def convert(self, path):
        res = []
        for row in path:
            builder = ""
            for r in row:
                el = "." if r == 0 else "Q"
                builder += el
            res.append(builder)
        return res

sol = Solution()
print(sol.solveNQueens(4))








