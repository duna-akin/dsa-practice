from binary_tree import Node


def levelOrder(root: Node):
    if root is None:
        return

    queue = [] # stores nodes to be visited
    queue.append(root)
    while queue:
        for _ in range(len(queue)):
            node = queue.pop() # popping is marking that node as visited
            print(node.val)

            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

deep = Node(1)
deep.left = Node(2)
deep.right = Node(3)
deep.left.left = Node(4)
deep.left.right = Node(5)


levelOrder(deep)
