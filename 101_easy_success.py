
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode):
        if not root:
            return True
        if root.val == None:
            return True
        
        if root.left and root.right:
            left_tree_q = [root.left]
            right_tree_q = [root.right]
            right_res = [root.right.val]
            left_res = [root.left.val]
        elif not root.left and not root.right:
            return True
        else:
            return False

        while left_tree_q:
            if left_tree_q[0] == None:
                left_res.append(None)
                left_tree_q.pop(0)
                continue
            left_tree_q.append(left_tree_q[0].left)
            left_tree_q.append(left_tree_q[0].right)
            if left_tree_q[0].left:
                left_res.append(left_tree_q[0].left.val)
            else:
                left_res.append(None)
            if left_tree_q[0].right:
                left_res.append(left_tree_q[0].right.val)
            else:
                left_res.append(None)

            left_tree_q.pop(0)

        while right_tree_q:
            if right_tree_q[0] == None:
                right_res.append(None)
                right_tree_q.pop(0)
                continue
            right_tree_q.append(right_tree_q[0].right)
            right_tree_q.append(right_tree_q[0].left)
            if right_tree_q[0].right:
                right_res.append(right_tree_q[0].right.val)
            else:
                right_res.append(None)
            if right_tree_q[0].left:
                right_res.append(right_tree_q[0].left.val)
            else:
                right_res.append(None)
            right_tree_q.pop(0)

        print(right_res)
        print(left_res)
        if right_res == left_res:
            return True

        return False

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.right = TreeNode(3)


test = Solution()
print(test.isSymmetric(root))
