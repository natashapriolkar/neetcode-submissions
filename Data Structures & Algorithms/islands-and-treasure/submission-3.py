class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        visit = set()

        def bfs(r, c):
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == -1 or (r, c) in visit:
                return

            visit.add((r, c))
            q.append((r, c))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                bfs(r + 1, c)
                bfs(r - 1, c)
                bfs(r, c + 1)
                bfs(r, c - 1)

            dist += 1

        

        
        