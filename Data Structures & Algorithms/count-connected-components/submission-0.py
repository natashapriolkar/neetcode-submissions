class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        visit = [False] * n

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node):
            q = deque([node])
            visit[node] = True
            while q:
                node = q.popleft()
                for neighbor in adj[node]:
                    if not visit[neighbor]:
                        visit[neighbor] = True
                        q.append(neighbor)

        res = 0
        for node in range(n):
            if not visit[node]:
                bfs(node)
                res +=1

        return res
        