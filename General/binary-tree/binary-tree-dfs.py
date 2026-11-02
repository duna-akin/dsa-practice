from binary_tree import Node

# DFS uses a stack. A recursion uses the call stack so DFS can be done via recursion!
def treeSum(node: Node) -> int:
    if node is None:
        return 0

    leftSum = treeSum(node.left)
    rightSum = treeSum(node.right)
    return node.val + leftSum + rightSum


def tests():
    # empty tree
    assert treeSum(None) == 0

    # single node
    assert treeSum(Node(5)) == 5

    # root with two children
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    assert treeSum(root) == 6

    # only a left child
    left_only = Node(10)
    left_only.left = Node(4)
    assert treeSum(left_only) == 14

    # only a right child
    right_only = Node(10)
    right_only.right = Node(4)
    assert treeSum(right_only) == 14

    # deeper tree
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    deep = Node(1)
    deep.left = Node(2)
    deep.right = Node(3)
    deep.left.left = Node(4)
    deep.left.right = Node(5)
    assert treeSum(deep) == 15

    # negative values
    neg = Node(-1)
    neg.left = Node(-2)
    neg.right = Node(3)
    assert treeSum(neg) == 0

    print("All tests passed")

tests()
