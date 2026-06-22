# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.recurseSwitch(root)
        return root
        
    def recurseSwitch(self, root: TreeNode):
        if root is None:
            return
        left = root.left
        right = root.right
        root.left = right
        root.right = left
        if root.left is not None:
            self.recurseSwitch(root.left)
        if root.right is not None:
            self.recurseSwitch(root.right)
        return

