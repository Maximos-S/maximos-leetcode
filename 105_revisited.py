# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not len(inorder):
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        left_len = len(inorder[0:root_index])
        if root_index > 0:
            root.left = self.buildTree(
                preorder[0:left_len], inorder[0:root_index])
            root.right = self.buildTree(
                preorder[left_len:], inorder[root_index + 1:])
        else:
            root.left = None
            root.right = self.buildTree(preorder, inorder[1:])

        return root
