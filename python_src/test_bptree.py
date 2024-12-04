from bptree import Node, BPTree

# def test_node():
#     node = Node(order=3, is_leaf=False)
#     node.insert(2)
#     assert node.keys == [2]

#     node.insert(6)
#     assert node.keys == [2, 6]

#     node.insert(4)
#     assert node.keys == [2, 4, 6]

#     node.insert(8)
#     assert node.keys == [2, 4, 6, 8]

def test_bptree_insert_wo_children():
    bptree = BPTree(order=3)
    bptree.insert(2, bptree.root)
    assert bptree.root.keys == [2]

    bptree.insert(6, bptree.root)
    assert bptree.root.keys == [2, 6]

    bptree.insert(4, bptree.root)
    assert bptree.root.keys == [4]
    assert bptree.root.children[0].keys == [2]
    assert bptree.root.children[1].keys == [4, 6]

    bptree.insert(5, bptree.root)
    print(bptree.root)
    for i in bptree.root.children:
        print(i)
    assert bptree.root.keys == [4, 5]
    assert bptree.root.children[0].keys == [2]
    assert bptree.root.children[1].keys == [4]
    assert bptree.root.children[2].keys == [5, 6]


# def test_bptree_insert_w_children():
#     bptree = BPTree(order=3)
#     bptree.insert(2, bptree.root)
#     assert bptree.root.keys == [2]

#     bptree.insert(6, bptree.root)
#     assert bptree.root.keys == [2, 6]

#     bptree.insert(4, bptree.root)
#     assert bptree.root.keys == [4]
#     assert bptree.root.children[0].keys == [2]
#     assert bptree.root.children[1].keys == [4, 6]

#     bptree.insert(5, bptree.root)
#     assert bptree.root.keys == [4]
#     assert bptree.root.children[0].keys == [2]
#     assert bptree.root.children[1].keys == [4, 6]