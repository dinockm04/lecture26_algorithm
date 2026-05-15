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

def search_bst_iter(node, key):
    while node != None:
        if key == node.data:
            return node

        elif key < node.data:
            node = node.left

        else:
            node = node.right

    return None

result = search_bst_iter(root, 68)

if result:
    print('탐색 성공 :', result.data)
else:
    print('탐색 실패')