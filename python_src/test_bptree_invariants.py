from bptree import BPTree
import random

def validate_child_key_order(current_node):
    for ind, key in enumerate(current_node.keys):
        if current_node.is_leaf:
            return
        if len(current_node.children) == 1:
            assert current_node.keys[0] <= current_node.children[0].keys[0]
        else:
            assert current_node.keys[ind] > current_node.children[ind].keys[-1]
            assert current_node.keys[ind] <= current_node.children[ind+1].keys[0]
        validate_child_key_order(current_node=current_node.children[ind])
    validate_child_key_order(current_node=current_node.children[-1])


# def test_parent_child_key_ordering():
#     bptree = BPTree(order=3)

#     bptree.insert(2, bptree.root)
#     bptree.insert(6, bptree.root)
#     bptree.insert(4, bptree.root)
#     bptree.insert(5, bptree.root)
#     bptree.insert(7, bptree.root)
#     bptree.insert(8, bptree.root)
#     bptree.insert(9, bptree.root)

#     print("")
#     bptree.print_tree()

#     print("DELETE 7")
#     bptree.delete(7, bptree.root)
#     current_node = bptree.root
#     bptree.print_tree()
#     validate_child_key_order(current_node=current_node)

#     print("DELETE 8")
#     bptree.delete(8, bptree.root)
#     bptree.print_tree()
#     current_node = bptree.root
#     validate_child_key_order(current_node=current_node)

#     print("DELETE 4")
#     bptree.delete(4, bptree.root)
#     bptree.print_tree()
#     current_node = bptree.root
#     validate_child_key_order(current_node=current_node)


# def test_random_inserts_and_delete_order_3():
#     bptree = BPTree(order=3)
#     sampled_numbers = [num for num in random.sample(range(100), 10)]
#     print(sampled_numbers)
#     for i in sampled_numbers:
#         print(i)
#         bptree.print_tree()
#         bptree.insert(i, bptree.root)
#         bptree.print_tree()

#     for i in random.sample(sampled_numbers, 5):
#         bptree.delete(i, bptree.root)
#         current_node = bptree.root
#         validate_child_key_order(current_node=current_node)

def test_random_inserts_and_delete_order_3():
    bptree = BPTree(order=3)
    sampled_numbers = [5, 49, 90, 54, 76, 81, 84, 3, 31, 32]
    print(sampled_numbers)
    for i in sampled_numbers:
        if i == 32:
            print(i)
            bptree.print_tree()
        bptree.insert(i, bptree.root)
        if i == 32:
            bptree.print_tree()

    for i in random.sample(sampled_numbers, 5):
        bptree.delete(i, bptree.root)
        current_node = bptree.root
        validate_child_key_order(current_node=current_node)
# [5, 49, 90, 54, 76, 81, 84, 3, 31, 32]
# def test_random_inserts_and_delete_order_4():
#     bptree = BPTree(order=4)
#     sampled_numbers = [num for num in random.sample(range(100), 10)]
#     print(sampled_numbers)
#     for i in sampled_numbers:
#         bptree.insert(i, bptree.root)

#     for i in random.sample(sampled_numbers, 5):
#         bptree.delete(i, bptree.root)
#         current_node = bptree.root
#         validate_child_key_order(current_node=current_node)

