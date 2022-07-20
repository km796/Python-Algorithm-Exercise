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
            if i+k < len(path):
                if path[i+k][j] == 1:
                    return False
            if i-k >=0:
                if path[i-k][j] == 1:
                    return False
            if j+k < len(path[0]):
                if path[i][j+k] == 1:
                    return False
            if j-k >= 0:
                if path[i][j-k] == 1:
                    return False
            if i+k < len(path) and j+k < len(path[0]):
                if path[i+k][j+k] == 1: return False






