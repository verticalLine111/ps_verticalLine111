# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # 1. 종료 조건: 노드가 비어있으면 None 반환
        if not root:
            return None
        
        # 2. 현재 노드의 왼쪽 자식과 오른쪽 자식을 스왑(Swap)
        root.left, root.right = root.right, root.left
        
        # 3. 바뀐 왼쪽, 오른쪽 자식을 타고 내려가며 동일한 작업 반복 (재귀)
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # 4. 트리의 루트 노드 반환
        return root