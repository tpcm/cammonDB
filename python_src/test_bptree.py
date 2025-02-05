from bptree import BPTree

# def test_bptree_insert_order_3():
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
#     assert bptree.root.keys == [4, 5]
#     assert bptree.root.children[0].keys == [2]
#     assert bptree.root.children[1].keys == [4]
#     assert bptree.root.children[2].keys == [5, 6]

#     bptree.insert(7, bptree.root)
#     assert bptree.root.keys == [5]
#     assert bptree.root.children[0].keys == [4]
#     assert bptree.root.children[1].keys == [6]
#     assert bptree.root.children[0].children[0].keys == [2]
#     assert bptree.root.children[0].children[1].keys == [4]
#     assert bptree.root.children[1].children[0].keys == [5]
#     assert bptree.root.children[1].children[1].keys == [6, 7]

#     bptree.insert(8, bptree.root)
#     assert bptree.root.keys == [5]
#     assert bptree.root.children[0].keys == [4]
#     assert bptree.root.children[1].keys == [6, 7]
#     assert bptree.root.children[0].children[0].keys == [2]
#     assert bptree.root.children[0].children[1].keys == [4]
#     assert bptree.root.children[1].children[0].keys == [5]
#     assert bptree.root.children[1].children[1].keys == [6]
#     assert bptree.root.children[1].children[2].keys == [7, 8]

#     bptree.insert(9, bptree.root)
#     assert bptree.root.keys == [5, 7]
#     assert bptree.root.children[0].keys == [4]
#     assert bptree.root.children[1].keys == [6]
#     assert bptree.root.children[2].keys == [8]
#     assert bptree.root.children[0].children[0].keys == [2]
#     assert bptree.root.children[0].children[1].keys == [4]
#     assert bptree.root.children[1].children[0].keys == [5]
#     assert bptree.root.children[1].children[1].keys == [6]
#     assert bptree.root.children[2].children[0].keys == [7]
#     assert bptree.root.children[2].children[1].keys == [8, 9]

def test_bptree_delete_order_3_depth_3_case_1():
    bptree = BPTree(order=3)

    bptree.insert(2, bptree.root)
    bptree.insert(6, bptree.root)
    bptree.insert(4, bptree.root)
    bptree.insert(5, bptree.root)
    bptree.insert(7, bptree.root)
    bptree.insert(8, bptree.root)
    bptree.insert(9, bptree.root)
    print("\n")

    bptree.delete(2, bptree.root)
    print("\n")
    # bptree.print_tree()

    assert bptree.root.keys == [7]
    assert bptree.root.children[0].keys == [5, 6]
    assert bptree.root.children[1].keys == [8]
    assert bptree.root.children[0].children[0].keys == [4]
    assert bptree.root.children[0].children[1].keys == [5]
    assert bptree.root.children[0].children[2].keys == [6]
    assert bptree.root.children[1].children[0].keys == [7]
    assert bptree.root.children[1].children[1].keys == [8, 9]

def test_bptree_delete_order_3_depth_3_case_2():
    bptree = BPTree(order=3)

    bptree.insert(2, bptree.root)
    bptree.insert(6, bptree.root)
    bptree.insert(4, bptree.root)
    bptree.insert(5, bptree.root)
    bptree.insert(7, bptree.root)
    bptree.insert(8, bptree.root)
    bptree.insert(9, bptree.root)

    bptree.delete(4, bptree.root)

    assert bptree.root.keys == [7]
    assert bptree.root.children[0].keys == [5, 6]
    assert bptree.root.children[1].keys == [8]
    assert bptree.root.children[0].children[0].keys == [2]
    assert bptree.root.children[0].children[1].keys == [5]
    assert bptree.root.children[0].children[2].keys == [6]
    assert bptree.root.children[1].children[0].keys == [7]
    assert bptree.root.children[1].children[1].keys == [8, 9]

def test_bptree_delete_order_3_depth_3_case_3():
    bptree = BPTree(order=3)

    bptree.insert(2, bptree.root)
    bptree.insert(6, bptree.root)
    bptree.insert(4, bptree.root)
    bptree.insert(5, bptree.root)
    bptree.insert(7, bptree.root)
    bptree.insert(8, bptree.root)
    bptree.insert(9, bptree.root)

    bptree.delete(6, bptree.root)

    assert bptree.root.keys == [7]
    assert bptree.root.children[0].keys == [4, 5]
    assert bptree.root.children[1].keys == [8]
    assert bptree.root.children[0].children[0].keys == [2]
    assert bptree.root.children[0].children[1].keys == [4]
    assert bptree.root.children[0].children[2].keys == [5]
    assert bptree.root.children[1].children[0].keys == [7]
    assert bptree.root.children[1].children[1].keys == [8, 9]

def test_bptree_delete_order_3_depth_3_case_4():
    bptree = BPTree(order=3)

    bptree.insert(2, bptree.root)
    bptree.insert(6, bptree.root)
    bptree.insert(4, bptree.root)
    bptree.insert(5, bptree.root)
    bptree.insert(7, bptree.root)
    bptree.insert(8, bptree.root)
    bptree.insert(9, bptree.root)

    bptree.delete(5, bptree.root)

    assert bptree.root.keys == [7]
    assert bptree.root.children[0].keys == [4, 6]
    assert bptree.root.children[1].keys == [8]
    assert bptree.root.children[0].children[0].keys == [2]
    assert bptree.root.children[0].children[1].keys == [4]
    assert bptree.root.children[0].children[2].keys == [6]
    assert bptree.root.children[1].children[0].keys == [7]
    assert bptree.root.children[1].children[1].keys == [8, 9]

def test_bptree_delete_order_3_depth_3_case_5():
    bptree = BPTree(order=3)

    bptree.insert(2, bptree.root)
    bptree.insert(6, bptree.root)
    bptree.insert(4, bptree.root)
    bptree.insert(5, bptree.root)
    bptree.insert(7, bptree.root)
    bptree.insert(8, bptree.root)
    bptree.insert(9, bptree.root)

    bptree.delete(7, bptree.root)

    assert bptree.root.keys == [5, 8]
    assert bptree.root.children[0].keys == [4]
    assert bptree.root.children[1].keys == [6]
    assert bptree.root.children[2].keys == [9]
    assert bptree.root.children[0].children[0].keys == [2]
    assert bptree.root.children[0].children[1].keys == [4]
    assert bptree.root.children[1].children[0].keys == [5]
    assert bptree.root.children[1].children[1].keys == [6]
    assert bptree.root.children[2].children[0].keys == [8]
    assert bptree.root.children[2].children[1].keys == [9]

# def test_bptree_delete_order_3_depth_3_case_6():
#     bptree = BPTree(order=3)

#     bptree.insert(2, bptree.root)
#     bptree.insert(6, bptree.root)
#     bptree.insert(4, bptree.root)
#     bptree.insert(5, bptree.root)
#     bptree.insert(7, bptree.root)
#     bptree.insert(8, bptree.root)
#     bptree.insert(9, bptree.root)

#     bptree.delete(8, bptree.root)

#     assert bptree.root.keys == [5, 7]
#     assert bptree.root.children[0].keys == [4]
#     assert bptree.root.children[1].keys == [6]
#     assert bptree.root.children[2].keys == [9]
#     assert bptree.root.children[0].children[0].keys == [2]
#     assert bptree.root.children[0].children[1].keys == [4]
#     assert bptree.root.children[1].children[0].keys == [5]
#     assert bptree.root.children[1].children[1].keys == [6]
#     assert bptree.root.children[2].children[0].keys == [7]
#     assert bptree.root.children[2].children[1].keys == [9]

# def test_bptree_delete_order_3_depth_3_case_6():
#     bptree = BPTree(order=3)

#     bptree.insert(2, bptree.root)
#     bptree.insert(6, bptree.root)
#     bptree.insert(4, bptree.root)
#     bptree.insert(5, bptree.root)
#     bptree.insert(7, bptree.root)
#     bptree.insert(8, bptree.root)
#     bptree.insert(9, bptree.root)

#     bptree.delete(9, bptree.root)

#     assert bptree.root.keys == [5, 7]
#     assert bptree.root.children[0].keys == [4]
#     assert bptree.root.children[1].keys == [6]
#     assert bptree.root.children[2].keys == [8]
#     assert bptree.root.children[0].children[0].keys == [2]
#     assert bptree.root.children[0].children[1].keys == [4]
#     assert bptree.root.children[1].children[0].keys == [5]
#     assert bptree.root.children[1].children[1].keys == [6]
#     assert bptree.root.children[2].children[0].keys == [7]
#     assert bptree.root.children[2].children[1].keys == [8]

# def test_tree_delete():
#     bptree = BPTree(order=3)
#     bptree.insert(2, bptree.root)
#     bptree.insert(6, bptree.root)
#     bptree.insert(4, bptree.root)

#     assert bptree.root.keys == [4]
#     assert bptree.root.children[0].keys == [2]
#     assert bptree.root.children[1].keys == [4, 6]

#     bptree.delete(2, bptree.root)
    
#     assert bptree.root.keys == [6]
#     assert bptree.root.children[0].keys == [4]
#     assert bptree.root.children[1].keys == [6]

#     bptree.insert(2, bptree.root)

#     assert bptree.root.keys == [6]
#     assert bptree.root.children[0].keys == [2, 4]
#     assert bptree.root.children[1].keys == [6]

#     bptree.delete(6, bptree.root)

#     assert bptree.root.keys == [4]
#     assert bptree.root.children[0].keys == [2]
#     assert bptree.root.children[1].keys == [4]

# def test_tree_delete_order_3_depth_2():
#     bptree = BPTree(order=3)
#     bptree.insert(2, bptree.root)
#     bptree.insert(3, bptree.root)
#     bptree.insert(4, bptree.root)
#     bptree.insert(5, bptree.root)

#     assert bptree.root.keys == [3,4]
#     assert bptree.root.children[0].keys == [2]
#     assert bptree.root.children[1].keys == [3]
#     assert bptree.root.children[2].keys == [4, 5]

#     bptree.insert(6, bptree.root)

#     assert bptree.root.keys == [4]
#     assert bptree.root.children[0].keys == [3]
#     assert bptree.root.children[1].keys == [5]
#     assert bptree.root.children[0].children[0].keys == [2]
#     assert bptree.root.children[0].children[1].keys == [3]
#     assert bptree.root.children[1].children[0].keys == [4]
#     assert bptree.root.children[1].children[1].keys == [5, 6]

#     bptree.delete(6, bptree.root)

#     assert bptree.root.keys == [4]
#     assert bptree.root.children[0].keys == [3]
#     assert bptree.root.children[1].keys == [5]
#     assert bptree.root.children[0].children[0].keys == [2]
#     assert bptree.root.children[0].children[1].keys == [3]
#     assert bptree.root.children[1].children[0].keys == [4]
#     assert bptree.root.children[1].children[1].keys == [5]

#     bptree.delete(5, bptree.root)

#     assert bptree.root.keys == [3, 4]
#     assert bptree.root.children[0].keys == [2]
#     assert bptree.root.children[1].keys == [3]
#     assert bptree.root.children[0].keys == [4]
    
#     assert bptree.root.keys == [6]
#     assert bptree.root.children[0].keys == [4]
#     assert bptree.root.children[1].keys == [6]

#     bptree.insert(2, bptree.root)

#     assert bptree.root.keys == [6]
#     assert bptree.root.children[0].keys == [2, 4]
#     assert bptree.root.children[1].keys == [6]

#     bptree.delete(6, bptree.root)

#     assert bptree.root.keys == [4]
#     assert bptree.root.children[0].keys == [2]
#     assert bptree.root.children[1].keys == [4]

# def test_tree_order_4():
#     bptree = BPTree(order=4)
#     bptree.insert(2, bptree.root)
#     bptree.insert(4, bptree.root)
#     bptree.insert(6, bptree.root)
#     bptree.insert(8, bptree.root)
#     bptree.insert(5, bptree.root)

#     assert bptree.root.keys == [6]
#     assert bptree.root.children[0].keys == [2, 4, 5]
#     assert bptree.root.children[1].keys == [6, 8]

#     bptree.delete(5, bptree.root)
    
#     assert bptree.root.keys == [6]
#     assert bptree.root.children[0].keys == [2, 4]
#     assert bptree.root.children[1].keys == [6, 8]

    # bptree.insert(2, bptree.root)

    # assert bptree.root.keys == [6]
    # assert bptree.root.children[0].keys == [2, 4]
    # assert bptree.root.children[1].keys == [6]

    # bptree.delete(6, bptree.root)

    # assert bptree.root.keys == [4]
    # assert bptree.root.children[0].keys == [2]
    # assert bptree.root.children[1].keys == [4]