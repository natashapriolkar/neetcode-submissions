# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0

    def dfs(self, node, maxSoFar):
        if node:
            if node.val >= maxSoFar:
                maxSoFar = node.val
                self.count += 1
            self.dfs(node.left, maxSoFar)
            self.dfs(node.right, maxSoFar)

    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, maxSoFar = float('-inf'))
        return self.count

    
    