class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = {}

        def dfs(i, j):
            if (i == n):
                return (m - j)
            if (j == m):
                return (n - i)

            if (i, j) in dp:
                return dp[(i, j)]

            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            else:
                insertAns = 1 + dfs(i, j + 1)
                deleteAns = 1 + dfs(i + 1, j)
                replaceAns = 1 + dfs(i + 1, j + 1)

            dp[(i, j)] = min(insertAns, deleteAns, replaceAns)
            return dp[(i, j)]
             


        return dfs(0, 0)
        