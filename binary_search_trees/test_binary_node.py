from binary_node import BinaryNode


def generate_binary_tree(items):
    if len(items) == 0:
        return None
    mid_idx = len(items) // 2
    root = BinaryNode(items[mid_idx])

    root.left = generate_binary_tree(items[:mid_idx])
    root.right = generate_binary_tree(items[mid_idx + 1:])

    if root.left:
        root.left.parent = root

    if root.right:
        root.right.parent = root

    return root


def test_get_first_node_in_subtree():
    for i in range(1, 9):
        items = [j for j in range(1, i+1)]
        root = generate_binary_tree(items)
        assert root.get_first_node_in_subtree().item == items[0]


def test_get_last_node_in_subtree():
    for i in range(1, 9):
        items = [j for j in range(1, i+1)]
        root = generate_binary_tree(items)
        assert root.get_last_node_in_subtree().item == items[-1]


def test_get_successor():
    items = [j for j in range(1, 9)]
    root = generate_binary_tree(items)
    assert root.get_successor().item == root.item + 1


def test_get_predecessor():
    items = [j for j in range(1, 9)]
    root = generate_binary_tree(items)
    assert root.get_predecessor().item == root.item - 1


def test_insert_before():
    items = [1, 2, 3, 4, 5, 6, 7]
    root = generate_binary_tree(items)
    assert root.item == 4
    new_node = BinaryNode(10)
    root.insert_before(new_node)

    assert root.get_predecessor() is new_node


def test_insert_after():
    items = [1, 2, 3, 4, 5, 6, 7]
    root = generate_binary_tree(items)
    assert root.item == 4
    new_node = BinaryNode(10)
    root.insert_after(new_node)

    assert root.get_successor() is new_node


def test_delete():
    items = [1, 2, 3, 4, 5, 6, 7]
    root = generate_binary_tree(items)
    item_to_delete = root.item
    root.delete()
    
    for node in root.subtree_iter():
        assert node.item != item_to_delete
