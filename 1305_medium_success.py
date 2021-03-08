# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr1 = self.iot(root1)
        arr2 = self.iot(root2)
        return self.merge(arr1, arr2)
    
    def iot(self,root):
        if not root:
            return []
        if root.left == None and root.right == None:
            return [root.val]
        
        array = self.iot(root.left)
        array.append(root.val)
        array += self.iot(root.right)
        
        return array
    
    def merge(self, arr1, arr2):
        resArr = []
        while arr1 and arr2:
            if arr1[0] <= arr2[0]:
                resArr.append(arr1.pop(0))
            else:
                resArr.append(arr2.pop(0))
                
        if arr1:
            resArr += arr1
        else:
            resArr += arr2
            
        return resArr