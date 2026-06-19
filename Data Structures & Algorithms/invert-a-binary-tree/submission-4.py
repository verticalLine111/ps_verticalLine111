# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        self.recurseSwitch(root)
        return curr
    
    def recurseSwitch(self, root: TreeNode):
        if root is None:
            return
        left = root.left
        right = root.right
        root.left = right
        root.right = left
        if left is not None:
            self.recurseSwitch(left)
        if right is not None:
            self.recurseSwitch(right)
        return
