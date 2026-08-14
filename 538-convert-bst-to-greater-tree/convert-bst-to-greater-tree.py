# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.summ=0

        def inorder(root):
            if not root:
                return None

            inorder(root.right)
            self.summ+=root.val
            root.val=self.summ
            inorder(root.left)

        inorder(root)
        return root