# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            print("preorder",preorder)
            return None
        root = TreeNode(preorder[0])
        try:
            rootIndex = inorder.index(preorder[0])
        except:
            root = TreeNode(inorder[0])
            return root 
        try:
            secondIndex = inorder.index(preorder[1])
        except:
            secondIndex = -1
        if secondIndex > rootIndex:
            root.left = None
            root.right = self.buildTree(preorder[1:],inorder[rootIndex + 1:])
            return root
        root.left = self.buildTree(preorder[1:],inorder[0:rootIndex])
        root.right = self.buildTree(preorder[2:],inorder[rootIndex + 1:])
        
        return root