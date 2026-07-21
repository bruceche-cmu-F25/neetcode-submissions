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
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # count = 1
        # while root.left is not None or root.right is not None:
        #     count += 1
        #     if root.left is None and root.right is not None:
        #         root = root.right
        #     elif root.right is None and root.left is not None:
        #         root = root.left
        # return count

        