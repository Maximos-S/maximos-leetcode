# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) < 1:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        middle = math.floor(len(nums)/2)
        root = TreeNode(nums[middle])
        print(nums)
        print(nums[0:middle])
        print(nums[middle+1:len(nums)])
        root.left = self.sortedArrayToBST(nums[0:middle])
        root.right = self.sortedArrayToBST(nums[middle+1:len(nums)])
        return root