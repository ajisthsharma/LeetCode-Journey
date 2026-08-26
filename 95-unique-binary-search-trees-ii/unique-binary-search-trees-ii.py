# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def build(start,end):
            if start>end:
                return [None]

            tree=[]
            for root in range(start,end+1):
                left_subtree=build(start,root-1)
                right_subtree=build(root+1,end)

                for left in left_subtree:
                    for right in right_subtree:
                        node=TreeNode(root)
                        node.left=left
                        node.right=right
                        tree.append(node)

            return tree

        return build(1,n)