from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        ans = set()
        board = [[0]*n for _ in range(n)]

        def backtrack(path, i, j, qs):
            if qs == n:
                ans.add(path)
                return
            self.check(path, i, j)

    def check(self, path, i, j):
        for k in range(len(path)):
            dirs = [[i+k,j],[i-k,j],[i,j+k],[i,j-k],[i+k,j+k],[i-k,j-k],[i+k,j-k],[i-k,j+k]]
            for dir in dirs:
                if 0 <= dir[0] < len(path) and 0 <= dir[1] < len(path) and path[dir[0]][dir[1]] == 1:
                    return False
        return True










