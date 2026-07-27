def height(root):
    if root is None:
        return 0
    left=height(root.left)
    if left==-1:
        return -1
    right=height(root.left)
    if right==-1:
        return -1
    if abs(left-right)>1:
        return -1
    return 1+max(left, right)

def isBalance(root):
    return height(root)!=-1

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
print(height(root))
print(isBalance(root))
