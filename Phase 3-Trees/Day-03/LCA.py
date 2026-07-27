def LCA(root,p,q):
    if root is None:
        return None
    if root==p or root==q:
        return root
    left=LCA(root.left,p,q)
    right=LCA(root.right,p,q)
    if left and right :
        return root
    if left:
        return left
    return right

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
print(LCA(root,root.left.left,root.left.right).value)
