tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [None, None],
    'D': [None, None],
    'E': [None, None]
}

def preorder(node):
    if node != None:
        print(node, end=' ')
        preorder(tree[node][0])
        preorder(tree[node][1])

preorder('A')