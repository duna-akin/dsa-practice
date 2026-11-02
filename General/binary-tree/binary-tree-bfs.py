from binary_tree import Node


def levelOrder(node: Node):
    if node is None:
        return

    queue = []
    queue.append(node)
    while queue:
        for _ in range(len(queue)):
