class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        memo = {}

        def dfs(r, c, prevVal):
            if r not in range(ROWS) or c not in range(COLS) or matrix[r][c] <= prevVal:
                return 0
            if (r, c) in memo:
                return memo[(r, c)]
            
            res = 1 + max(dfs(r + 1, c, matrix[r][c]), 
                         dfs(r - 1, c, matrix[r][c]), 
                         dfs(r, c + 1, matrix[r][c]), 
                         dfs(r, c - 1, matrix[r][c]))
            memo[(r, c)] = res
            return res

            
        result = 0

        for r in range(ROWS):
            for c in range(COLS):
                result = max(result, dfs(r, c, float('-inf')))

        return result