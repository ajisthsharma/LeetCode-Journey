# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans=[]

        def solve(root,res):
            if root.left is None and root.right is None:
                res+=str(root.val)
                ans.append(int(res))
                return

            res+=str(root.val)

            if root.left:
                solve(root.left,res)
            if root.right:
                solve(root.right,res)

        solve(root,"")

        return sum(ans)
