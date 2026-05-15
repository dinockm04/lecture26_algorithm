class STreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = STreeNode(35)
root.left = STreeNode(18)
root.right = STreeNode(68)
root.left.left = STreeNode(7)
root.left.right = STreeNode(26)

def search_bst(node, key):
    if node == None:
        return None

    if key == node.data:
        return node

    elif key < node.data:
        return search_bst(node.left, key)

    else:
        return search_bst(node.right, key)

result = search_bst(root, 26)

if result:
    print('탐색 성공 :', result.data)
else:
    print('탐색 실패')