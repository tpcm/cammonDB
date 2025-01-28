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

# def test_bptree_insert_wo_children():
    # bptree = BPTree(order=3)
    # bptree.insert(2, bptree.root)
#     assert bptree.root.keys == [2]

#     bptree.insert(6, bptree.root)
#     assert bptree.root.keys == [2, 6]

#     bptree.insert(4, bptree.root)
    # assert bptree.root.keys == [4]
    # assert bptree.root.children[0].keys == [2]
    # assert bptree.root.children[1].keys == [4, 6]

#     bptree.insert(5, bptree.root)
#     # print(bptree.root)
#     # for i in bptree.root.children:
#     #     print(i)
#     assert bptree.root.keys == [4, 5]
#     assert bptree.root.children[0].keys == [2]
#     assert bptree.root.children[1].keys == [4]
#     assert bptree.root.children[2].keys == [5, 6]

#     bptree.insert(7, bptree.root)
#     # print(bptree.root)
#     # for i in bptree.root.children:
#     #     print(i)
#     assert bptree.root.keys == [5]
#     assert bptree.root.children[0].keys == [4]
#     assert bptree.root.children[1].keys == [6]
#     assert bptree.root.children[0].children[0].keys == [2]
#     assert bptree.root.children[0].children[1].keys == [4]
#     assert bptree.root.children[1].children[0].keys == [5]
#     assert bptree.root.children[1].children[1].keys == [6, 7]

#     bptree.insert(8, bptree.root)
#     print(bptree.root)
#     for i in bptree.root.children:
#         print(i)
#     assert bptree.root.keys == [5]
#     assert bptree.root.children[0].keys == [4]
#     assert bptree.root.children[1].keys == [6, 7]
#     assert bptree.root.children[0].children[0].keys == [2]
#     assert bptree.root.children[0].children[1].keys == [4]
#     assert bptree.root.children[1].children[0].keys == [5]
#     assert bptree.root.children[1].children[1].keys == [6]
#     assert bptree.root.children[1].children[2].keys == [7, 8]

def test_node_delete():
    node = Node(order=3, is_leaf=True)
    node.insert(2)
    assert node.keys == [2]

    node.delete(2)
    assert node.keys == []

def test_tree_delete():
    bptree = BPTree(order=3)
    bptree.insert(2, bptree.root)
    bptree.insert(6, bptree.root)
    bptree.insert(4, bptree.root)

    assert bptree.root.keys == [4]
    assert bptree.root.children[0].keys == [2]
    assert bptree.root.children[1].keys == [4, 6]

    bptree.delete(2, bptree.root)
    
    assert bptree.root.keys == [6]
    assert bptree.root.children[0].keys == [4]
    assert bptree.root.children[1].keys == [6]
