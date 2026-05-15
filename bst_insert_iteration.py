class STreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert_bst(root, node):
    p = None
    current = root

    while current != None:
        p = current

        if node.data < current.data:
            current = current.left
        else:
            current = current.right

    if node.data < p.data:
        p.left = node
    else:
        p.right = node

numbers = [35, 18, 68, 7, 26, 99]

root = STreeNode(numbers[0])

for num in numbers[1:]:
    insert_bst(root, STreeNode(num))

def inorder(node):
    if node != None:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

inorder(root)