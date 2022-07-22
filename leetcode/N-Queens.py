from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        ans = set()
        board = [[0]*n for _ in range(n)]
        visited = set()

        def backtrack(path, i, j, qs):
            tPath = tuple(map(tuple, path))
            if (tPath, i, j) in visited:
                return
            visited.add((tPath, i, j))
            if qs == n:
                ans.add(tPath)
                return
            if i>=len(path) or j>=len(path[0]):
                return
            if self.check(path, i, j):
                path[i][j] = 1
                if j==len(path[0])-1:
                    backtrack(path, i+1, 0, qs+1)
                else:
                    backtrack(path, i, j+1, qs+1)
                path[i][j] = 0

            if j==len(path[0])-1:
                backtrack(path, i+1, 0, qs)
            else:
                backtrack(path, i, j+1, qs)
        backtrack(board, 0, 0, 0)

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
print(sol.solveNQueens(8))








