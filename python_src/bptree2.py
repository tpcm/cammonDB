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

    def __str__(self):
        return f"Keys: {self.keys},  Children: {self.children},  IS_LEAF: {self.is_leaf}"

                
class BPTree:
    def __init__(self, order=3):
        self.order = order
        self.root = Node(is_leaf=True)
        self.traversed_nodes: list[Node] = []
    
    def find_leaf_node(self, value: int, current_node: Node, tree_traversed: bool = False):
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

        # Check if need to split the nodes and push up
        if len(current_node.keys) >= self.order:
            median_ind = math.floor(len(current_node.keys) / 2)
            # print(f"median ind: {median_ind}, median key: {current_node.keys[median_ind]}")
            median_key = current_node.keys[median_ind]
            split_nodes = current_node.split(median_ind)

            # If no parent node create one
            if len(self.traversed_nodes) == 0:
                parent_node = Node(False)
            else:
                parent_node = self.traversed_nodes.pop()

            if self.root == current_node:
                self.root = parent_node
            
            # Migrate children to new parent node
            if parent_node.children:
                child_ind_to_remove = parent_node.children.index(current_node)
                new_children = parent_node.children[:child_ind_to_remove] + split_nodes + parent_node.children[child_ind_to_remove+1:]
                parent_node.children = new_children
            else:
                parent_node.children = split_nodes

            if len(current_node.children) != 0:
                for ind in range(len(current_node.children)):
                    if current_node.children[ind].keys[0] == median_key:
                        child_to_split_on = ind
                        break

                split_children = [current_node.children[:child_to_split_on], current_node.children[child_to_split_on:]]
                split_nodes[0].children = split_children[0]
                split_nodes[1].children = split_children[1]
                
            return self.insert(current_node=parent_node, value=median_key, tree_traversed=True)
        return


    def delete(self: "BPTree", value: int, current_node: Node, tree_traversed: bool = False):
        if not tree_traversed:
            current_node, tree_traversed = self.find_leaf_node(value, current_node, tree_traversed)
        
        current_node.delete(value)
        print(f"current_node_keys: {len(current_node.keys)}")


        # Check if node is less than half empty
        if len(current_node.keys) >= math.ceil(self.order/2) - 1:
            print("CHECK")
            return
        
        else:
            self.redistribute(current_node, value)
        
    def redistribute(self: "BPTree", current_node: Node, value: int):
        parent_node = self.traversed_nodes[-1]
        current_node_index = parent_node.children.index(current_node)
        if len(parent_node.children) <= 1:
            return False
        if current_node_index != 0:
            sibling_node = parent_node.children[current_node_index - 1]
            is_left_sibling = True
        else:
            sibling_node = parent_node.children[current_node_index + 1]
            is_left_sibling = False
        
        if ( len(sibling_node.keys) < math.ceil(self.order/2) - 1 ) | len(current_node.keys) == 0:
            # merge
            print("MERGE")
            if is_left_sibling:
                new_node = Node(is_leaf=current_node.is_leaf)
                new_node.keys = sibling_node.keys + current_node.keys
            else:
                new_node = current_node + sibling_node
        # update parent node to account for change in keys
        ##########
        # check sibling len
        elif len(sibling_node.keys) >= math.ceil(self.order/2) - 1:
            # redistribute
            print(f"len_sibling_node: {len(sibling_node.keys)}")
            if is_left_sibling:
                print(f"current_node_keys: {current_node.keys}")
                print(f"sibling_node_keys: {sibling_node.keys}")
                current_node.keys.insert(0, sibling_node.keys[-1])
                print(f"current_node_keys: {current_node.keys}")
                if value in parent_node.keys:
                    parent_node.keys[parent_node.keys.index(value)] = sibling_node.keys.pop(-1)
            else:
                current_node.keys.append(sibling_node.keys[0])
                if value in parent_node.keys:
                    parent_node.keys[parent_node.keys.index(sibling_node.keys.pop(0))] = parent_node.children[1].keys[1]
        
        



