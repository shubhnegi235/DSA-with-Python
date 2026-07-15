#Creating a recursive function of Preorder, Inorder and Postorder.
def Preorder(root):
    if root is None:
        return
    print(root.val)
    Preorder(root.left)
    Preorder(root.right)

def Inorder(root):
    if root is None:
        return
    Inorder(root.left)
    print(root.val)
    Inorder(root.right)

def Postorder(root):
    if root is None:
        return
    Postorder(root.left)
    Postorder(root.right)
    print(root.val)
