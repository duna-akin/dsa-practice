from binary_tree import Node


def insert(root: Node, value: int):
    left = root.left
    right = root.right

    if left is None and value < root.val:
        root.left = Node(value)
        return
    if right is None and value >= root.val:
        root.right = Node(value)
        return

    if value < root.val:
        insert(left, value)
    else:
        insert(right, value)


def toList(node):
    if node is None:
        return []
    return toList(node.left) + [node.val] + toList(node.right)


def tests():
    # smaller value goes left
    root = Node(10)
    insert(root, 5)
    assert root.left.val == 5
    assert root.right is None

    # larger value goes right
    root = Node(10)
    insert(root, 15)
    assert root.right.val == 15
    assert root.left is None

    # equal value goes right
    root = Node(10)
    insert(root, 10)
    assert root.right.val == 10
    assert root.left is None

    # two levels down on the left
    root = Node(10)
    insert(root, 5)
    insert(root, 3)
    assert root.left.left.val == 3

    # two levels down on the right
    root = Node(10)
    insert(root, 15)
    insert(root, 20)
    assert root.right.right.val == 20

    # left then right inside the left subtree
    root = Node(10)
    insert(root, 5)
    insert(root, 7)
    assert root.left.right.val == 7

    # duplicates in a chain
    root = Node(10)
    insert(root, 10)
    insert(root, 10)
    assert root.right.right.val == 10

    # duplicate below the root
    root = Node(10)
    insert(root, 15)
    insert(root, 15)
    assert root.right.right.val == 15

    # larger tree stays sorted in order
    root = Node(10)
    for v in [5, 15, 3, 7, 12, 18]:
        insert(root, v)
    assert toList(root) == [3, 5, 7, 10, 12, 15, 18]

    # root value never changes
    root = Node(10)
    for v in [1, 20, 5, 15]:
        insert(root, v)
    assert root.val == 10

    print("All tests passed")

tests()
