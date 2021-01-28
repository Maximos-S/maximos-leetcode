# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        paths = []
        level = 0
        self.dfs_recursion(root, level, paths)
        print(paths)
        return min(paths)

    def dfs_recursion(self, root, level, paths):
        if root.left == None and root.right == None:
            level += 1
            paths.append(level)
        level += 1
        if root.left:
            self.dfs_recursion(root.left, level, paths)
        if root.right:
            self.dfs_recursion(root.right, level, paths)
