from bptree import Node

def test_node():
    node = Node(is_leaf=False)
    node.insert(2)
    assert node.keys == [2]

    node.insert(6)
    assert node.keys == [2, 6]

    node.insert(4)
    assert node.keys == [2, 4, 6]

    node.insert(8)
    assert node.keys == [2, 4, 6, 8]

def test_node_delete():
    node = Node(is_leaf=True)
    node.insert(2)
    node.insert(4)
    node.insert(6)
    node.insert(8)
    assert node.keys == [2, 4, 6, 8]

    node.delete(2)
    assert node.keys == [4, 6, 8]

    node.delete(4)
    assert node.keys == [6, 8]

    node.delete(6)
    assert node.keys == [8]

    node.delete(8)
    assert node.keys == []