from collections import deque
def levelorder(root):
    if root is None:
        return []
    queue=deque([root])
    ans=[]
    while queue:
        node=queue.popleft()
        ans.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return ans

def Preorder(root):
    if root is None:
        return
    print(root.value)
    Preorder(root.left)
    Preorder(root.right)

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
print(levelorder(root))
Preorder(root)

