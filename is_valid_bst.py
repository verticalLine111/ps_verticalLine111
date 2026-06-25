def is_valid_bst(root):
    def check(node, lower, upper):
        if node is None:
            return True

        if not (lower < node.val < upper):
            return False

        return check(node.left, lower, node.val) and check(node.right, node.val, upper)
        4 , -inf , 7. and 9 , 7 , inf
        1, -inf , 4 and none, 9 , 7
        
    return check(root, float("-inf"), float("inf"))
#      7
#     / \
#    4   9
#   / \
#  1   8