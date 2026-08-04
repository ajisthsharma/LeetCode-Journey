# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, minn, maxx):
            if not node:
                return True
            
            if not (minn < node.val < maxx):
                return False
            
            left = valid(node.left, minn, node.val)
            right = valid(node.right,node.val, maxx)

            return left and right
        if not root:
            return True
        return valid(root, float("-inf"), float("inf"))