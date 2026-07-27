def height(root):
    if root is None:
        return 0
    left=height(root.left)
    right=height(root.right)
    return 1+max(left, right)

class TreeNode:
    def __init__(root, value):
        root.value=value
        root.left=None
        root.right=None

root=TreeNode(1)
root.left=TreeNode(2)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
root.right=TreeNode(3)
root.right.left=TreeNode(6)
root.right.right.right=TreeNode(7)
print(height(root))

