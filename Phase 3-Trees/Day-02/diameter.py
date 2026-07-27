def diameter(root):
    ans=0
    def height(node):
        nonlocal ans
        if node is None:
            return 0
        left=height(node.left)
        right=height(node.right)
        ans=max(ans, left+right+1)
        return 1+max(left, right)
    height(root)
    return ans

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
print(diameter(root))
