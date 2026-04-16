# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def __init__(self):
        # self.count = 0
        # self.result = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        #Approach 1: Using instance variable count O(1)
        # def dfs(node):
        #     if not node or self.result is not None:
        #         return

        #     dfs(node.left)
        #     self.count += 1
        #     if self.count == k:
        #         self.result = node.val
        #         return
        #     # result.append(node.val)
        #     dfs(node.right)

        # dfs(root)

        # return self.result

        # Approach 2: Using generators
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        gen_obj = inorder(root)
        for _ in range(k):
            result  = next(gen_obj)

        return result


        