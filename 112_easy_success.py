# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        return self.recursiveSum(root, 0, sum) == sum

    def recursiveSum(self, root, total, sum):
        if root.left == None and root.right == None:
            return total + root.val
        total += root.val
        print(total)
        if root.left:
            if self.recursiveSum(root.left, total, sum) == sum:
                return sum
        if root.right:
            if self.recursiveSum(root.right, total, sum) == sum:
                return sum
        return

tree_root = TreeNode(5)
tree_root.left = TreeNode(4)
tree_root.right = TreeNode(8)
tree_root.left.left = TreeNode(11)
tree_root.left.left.left = TreeNode(7)
tree_root.left.left.right = TreeNode(2)
tree_root.right.left = TreeNode(13)
tree_root.right.right = TreeNode(4)
tree_root.right.right.right = TreeNode(1)

test =Solution()
print(test.hasPathSum(tree_root, 22))