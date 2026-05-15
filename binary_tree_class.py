class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('D')
root.left.right = TreeNode('E')

def preorder(node):
    if node != None:
        print(node.data, end=' ')
        preorder(node.left)
        preorder(node.right)

def inorder(node):
    if node != None:
        inorder(node.left)
        print(node.data, end=' ')
        inorder(node.right)

def postorder(node):
    if node != None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=' ')

print('전위순회')
preorder(root)

print('\n중위순회')
inorder(root)

print('\n후위순회')
postorder(root)