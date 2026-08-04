# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, left, right):
            if not root:
                return True
            
            if left < root.val < right:
                valid_left = validate(root.left, left, root.val)
                valid_right = validate(root.right, root.val, right)
            else:
                return False
            
            return valid_left and valid_right
        
        return validate(root, float('-inf'), float('inf'))