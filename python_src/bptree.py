import math

class Node:
    def __init__(self, is_leaf):
        self.keys: list[int] = []
        # self.values: list[int] = []
        self.is_leaf: bool = is_leaf
        self.children: list[Node] = []
    
    def insert(self: "Node", key: int):
        if not self.keys:
            self.keys.append(key)
            return
        
        self.keys.sort()
        if key > self.keys[-1]:
            self.keys.append(key)
            
        else:
            for ind in range(len(self.keys)):
                if key < self.keys[ind]:
                    self.keys = self.keys[:ind] + [key] + self.keys[ind:]
                    break
    
    def delete(self: "Node", key: int):
        if not self.keys:
            return
        
        for ind in range(len(self.keys)):
            if key == self.keys[ind]:
                break
        self.keys.pop(ind)
        return
            
    def split(self: "Node", median_ind: int) -> list:
        if self.is_leaf:
            split_nodes_keys = [self.keys[:median_ind], self.keys[median_ind:]]
        else:
            split_nodes_keys = [self.keys[:median_ind], self.keys[median_ind+1:]]
        first_node = Node(is_leaf=self.is_leaf)
        second_node = Node(is_leaf=self.is_leaf)
        first_node.keys = split_nodes_keys[0]
        second_node.keys = split_nodes_keys[-1]
        return [first_node, second_node]
    
    def reconfigure_keys(self):
        new_keys = []
        for child in self.children[1:]:
            if not child :
                return []
            new_keys.append(child.keys[0]) 
        self.keys = new_keys

    def __str__(self):
        return f"Keys: {self.keys},  Children: {self.children},  IS_LEAF: {self.is_leaf}"

                
class BPTree:
    def __init__(self, order=3):
        self.order = order
        self.root = Node(is_leaf=True)
        self.traversed_nodes: list[Node] = []
    
    def find_leaf_node(self, value: int, current_node: Node, tree_traversed: bool = False):
        self.traversed_nodes = []
        while not current_node.is_leaf:
            if len(current_node.children) > 0:
                child_index = None
                for ind in range(len(current_node.keys)):
                    if value < current_node.keys[ind]:
                        child_index = ind
                        break
                
                if not current_node.is_leaf:
                    self.traversed_nodes.append(current_node)
                
                if isinstance(child_index, int):
                    current_node = current_node.children[child_index]
                else:
                    current_node = current_node.children[-1]

            if current_node.is_leaf:
                tree_traversed = True
        return current_node, tree_traversed
    
    def insert(self, value: int, current_node: Node, tree_traversed: bool = False):
        if not tree_traversed:
            current_node, tree_traversed = self.find_leaf_node(value, current_node, tree_traversed)

        current_node.insert(value)
        if value in [31, 32, 54]:
            print(current_node.keys)
            print(current_node.children)

        # Check if need to split the nodes and push up
        if len(current_node.keys) >= self.order:
            if value in [31, 32, 54]:
                print("SPLIT")
            median_ind = math.floor(len(current_node.keys) / 2)
            if value in [31]:
                print(f"median ind: {median_ind}, median key: {current_node.keys[median_ind]}")
            median_key = current_node.keys[median_ind]
            split_nodes = current_node.split(median_ind)
            if value in [31, 32, 54]:
                for i in split_nodes:
                    print("SPLIT NODES: ", i.keys)

            # If no parent node create one
            if len(self.traversed_nodes) == 0:
                parent_node = Node(False)
            else:
                parent_node = self.traversed_nodes.pop()
                if value in [31, 32, 54]:
                    print("PARENT NODE: ", parent_node.keys)
                    self.print_tree()

            if self.root == current_node:
                self.print_tree()
                self.root = parent_node
                self.print_tree()
            
            # Migrate children to new parent node
    
            if parent_node.children:
                child_ind_to_remove = parent_node.children.index(current_node)
                if value in [31, 32, 54]:
                    print("CHILD to remove: ", parent_node.children[child_ind_to_remove].keys)
                new_children = parent_node.children[:child_ind_to_remove] + split_nodes + parent_node.children[child_ind_to_remove+1:]
                parent_node.children = new_children
                if value in [31, 32, 54]:
                    self.print_tree()
            else:
                parent_node.children = split_nodes
            try:
                if len(current_node.children) != 0:
                    print("CHILDREN")
                    print(value)
                    for ind in range(len(current_node.children)):

                        if value in [31, 32, 54]:
                            self.print_tree()
                            print(median_key)
                        if current_node.children[ind].keys[0] == median_key:
                            child_to_split_on = ind
                            print("CHILD TO SPLIT ON: ", child_to_split_on)
                            break
                    print("CHILD TO SPLIT ON: ", child_to_split_on)
                    split_children = [current_node.children[:child_to_split_on], current_node.children[child_to_split_on:]]
                    for i in split_children:
                        print("SPLIT CHILDREN: ", i)
                        for j in i:
                            print("SPLIT CHILDREN: ", j.keys)
                    split_nodes[0].children = split_children[0]
                    split_nodes[1].children = split_children[1]
                    self.print_tree()
            except Exception as err:
                raise err

                # print(current_node, ind, median_key)
                # for i in current_node.children:
                #     print("CHILD:", i)
                
            return self.insert(current_node=parent_node, value=median_key, tree_traversed=True)
        return
    
            
    def delete(self: "BPTree", value: int, current_node: Node, tree_traversed: bool=False):
        # print("DELETE: ", value)
        if not tree_traversed:
            current_node, tree_traversed = self.find_leaf_node(value, current_node, tree_traversed)
        
        if value in current_node.keys:
            # self.print_tree()
            current_node.delete(value)
            if value == 4:
                self.print_tree()
        else:
            return False

        min_keys = math.ceil(self.order / 2) - 1
        if len(current_node.keys) >= min_keys:
            return True
        
        # get sibling node, left sibling by default
        parent_node = self.traversed_nodes.pop(-1)
        current_node_index = parent_node.children.index(current_node)

        if current_node_index != 0:
            sibling_node = parent_node.children[current_node_index - 1]
            is_left_sibling = True
        else:
            sibling_node = parent_node.children[current_node_index + 1]
            is_left_sibling = False

        # check we can borrow from sibling to redistribute
        if ( len(sibling_node.keys) - 1 >= min_keys) and len(sibling_node.children) - 2 >= math.ceil(self.order / 2):
            print("BORROW")
            if is_left_sibling:
                # print("Borrow LEft")
                # Borrow sibling's rightmost key
                borrowed_key = sibling_node.keys.pop(-1)
                current_node.keys.insert(0, borrowed_key)
                # Update parent's separator key
                parent_node.keys[current_node_index - 1] = borrowed_key
            else:
                # Borrow sibling's leftmost key
                borrowed_key = sibling_node.keys.pop(0)
                current_node.keys.append(borrowed_key)
                parent_node.keys[current_node_index] = sibling_node.keys[0]
                # Take children
                if not current_node.is_leaf:
                    children_to_take = sibling_node.children[:2]
                    del sibling_node.children[:2]
                    current_node.children.extend(children_to_take)
            if len(current_node.keys) < len(current_node.children) + 1:
                current_node.reconfigure_keys()


            

        # merge
        elif (( len(sibling_node.keys) - 1 < min_keys) or len(current_node.keys) == 0):
            print("MERGE")
            self.print_tree()
            if is_left_sibling:
                print("left sibling")
                sibling_node.keys.extend(current_node.keys)
                sibling_node.children.extend(current_node.children)
                deletion_value_to_cascade = parent_node.keys[current_node_index - 1]
                parent_node.children.pop(current_node_index)
                merged_node = sibling_node

            else:
                print("Right sibling")
                # if len(sibling_node.children) - 2 < math.ceil(self.order / 2):
                #     # Rebalance
                #     current_node.keys.extend(parent_node.keys[current_node_index])
                # else:
                current_node.keys.extend(sibling_node.keys)
                current_node.children.extend(sibling_node.children)
                deletion_value_to_cascade = parent_node.keys[current_node_index]
                parent_node.children.pop(current_node_index + 1)
                merged_node = current_node
        
            current_node = merged_node
            self.print_tree()

            if parent_node == self.root and len(parent_node.children) == 1:
                key_to_bring_down = self.root.keys[0]
                self.root = current_node
                self.insert(value=key_to_bring_down, current_node=current_node, tree_traversed=True)
            else:
                if not current_node.is_leaf:
                    current_node.reconfigure_keys()
                self.delete(value=deletion_value_to_cascade, current_node=parent_node, tree_traversed=True)
        
        return True

    def print_tree(self, node=None, level=0, prefix=""):
        if node is None:
            node = self.root
        
        indent = "    " * level
        connector = "└── " if prefix else ""
        
        # Print current node
        print(f"{indent}{prefix}{connector}[{','.join(map(str, node.keys))}]")
        
        # Print children
        if not node.is_leaf:
            for i, child in enumerate(node.children):
                last_child = i == len(node.children) - 1
                new_prefix = "    " if last_child else "│   "
                self.print_tree(child, level + 1, new_prefix)
