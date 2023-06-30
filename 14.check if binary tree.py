class Node:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None
def checkbinarytree(root):
    if root.left==None and root.right==None:
        return True

    if root.right==None:
        if root.key> root.left.key:
            return True

    else:
        if root.key>root.left.key and root.key>root.right.key :
            return checkbinarytree(root.left) and checkbinarytree(root.right)
        else:
            False
def inorder(root):
    if root:
        inorder(root.left)
        print(root.key,end=' ')
        inorder(root.right)

root=Node(50)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(15)
root.left.right=Node(17)
root.right.left=Node(12)
root.right.right=Node(10)
inorder(root)
print()

print(checkbinarytree(root))