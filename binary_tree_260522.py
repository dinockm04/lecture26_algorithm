tree = [
    ['A', 1, 2],
    ['B', 3, None],
    ['C', 4, 5],
    ['D', None, None],
    ['E', None, None],
    ['F', None, 6],
    ['G', None, None]
]

def preorder(index):
    if index is None:
        return
    print(tree[index][0], end='')
    preorder(tree[index][1])
    preorder(tree[index][2])

def inorder(index):
    if index is None:
        return
    inorder(tree[index][1])
    print(tree[index][0], end='')
    inorder(tree[index][2])

def postorder(index):
    if index is None:
        return
    postorder(tree[index][1])
    postorder(tree[index][2])
    print(tree[index][0], end='')

print('전위 순회 결과 : ', end='')
preorder(0)

print('\n중위 순회 결과 : ', end='')
inorder(0)

print('\n후위 순회 결과 : ', end='')
postorder(0)