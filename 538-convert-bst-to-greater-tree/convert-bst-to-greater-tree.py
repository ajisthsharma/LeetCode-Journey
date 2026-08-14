# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.summ=0

        def preorder(root):
            if not root:
                return None

            preorder(root.right)
            self.summ+=root.val
            root.val=self.summ
            preorder(root.left)

        preorder(root)
        return root