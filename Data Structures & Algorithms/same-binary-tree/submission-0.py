# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. 둘 다 None이면 같은 것
        if not p and not q:
            return True
        # 2. 하나만 None이거나, 값이 다르면 다른 것
        if not p or not q or p.val != q.val:
            return False
        # 3. 현재 노드가 같으면 좌/우 서브트리를 재귀적으로 비교
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)