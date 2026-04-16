# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = 1
        stack = [[root, 1]]
        while stack:
            current, depth = stack.pop()
            if current:
                result = max(result, depth)
                stack.append([current.right, depth + 1])
                stack.append([current.left, depth + 1])

        return result

        
        