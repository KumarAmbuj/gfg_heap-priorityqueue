class Node:
    def __init__(self,data):
        self.key=data
        self.left=None
        self.right=None

def inorder(root,):
    if root:
        inorder(root.left)
        print(root.key,end=' ')
        inorder(root.right)
def inordertraversal(root,arr):
    if root:
        inordertraversal(root.left,arr)
        arr.append(root.key)
        inordertraversal(root.right,arr)

def bsttominheap(root,arr,i):
    if root:
        root.key = arr[i[0]]
        i[0] += 1
        bsttominheap(root.left, arr, i)
        bsttominheap(root.right, arr, i)

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)
inorder(root)
print()
arr=[]
inordertraversal(root,arr)
print(arr)
i=[0]

bsttominheap(root,arr,i)
inorder(root)