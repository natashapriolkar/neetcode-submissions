class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [[1,0], [-1,0], [0, 1], [0, -1]]

        def bfs(r, c):
            visit = [[False] * COLS for _ in range(ROWS)]
            q = deque([(r, c)])
            visit[r][c] = True
            steps = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    if grid[row][col] == 0:
                        return steps
                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc
                        if nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] != -1 and visit[nr][nc] == False:
                            q.append((nr, nc))
                            visit[nr][nc] = True

                steps += 1
            return INF

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
        