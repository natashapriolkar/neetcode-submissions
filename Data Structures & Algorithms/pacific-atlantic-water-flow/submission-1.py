class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = []
        atlantic = []

        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(source, ocean):
            q = deque(source)
            while q:
                r, c = q.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(ROWS) and nc in range(COLS) and heights[nr][nc] >= heights[r][c] and not ocean[nr][nc]:
                        q.append((nr, nc))


        for r in range(ROWS):
            pacific.append((r, 0))
            atlantic.append((r, COLS - 1))

        for c in range(COLS):
            pacific.append((0, c))
            atlantic.append((ROWS - 1, c))

        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])

        return res


        