class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()

        def dfs(r, c):
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == "0" or (r, c) in visit:
                return

            visit.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        numOfIslands = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visit:
                    dfs(r, c)
                    numOfIslands += 1

        return numOfIslands