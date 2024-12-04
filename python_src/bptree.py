import math

class Node:
    def __init__(self, order, is_leaf):
        self.order = order
        self.max_num_keys = order - 1
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
    
    def split(self: "Node", median_ind: int) -> list:
        if self.is_leaf:
            split_nodes_keys = [self.keys[:median_ind], self.keys[median_ind:]]
        else:
            split_nodes_keys = [self.keys[:median_ind], self.keys[median_ind+1:]]
        first_node = Node(self.order, is_leaf=self.is_leaf)
        second_node = Node(self.order, is_leaf=self.is_leaf)
        first_node.keys = split_nodes_keys[0]
        second_node.keys = split_nodes_keys[-1]
        return [first_node, second_node]

    def __str__(self):
        return f"Keys: {self.keys},  Children: {self.children},  IS_LEAF: {self.is_leaf}"

                
class BPTree:
    def __init__(self, order=3):
        self.order = order
        self.root = Node(order, is_leaf=True)
        self.traversed_nodes: list[Node] = []

    
    def insert(self, value: int, current_node: Node, tree_traversed: bool = False):
        """"""
        if not tree_traversed:
            while not current_node.is_leaf:
                if len(current_node.children) > 0:
                    child_index = None
                    for ind in range(len(current_node.keys)):
                        if value < current_node.keys[ind]:
                            child_index = ind
                            break

                    if not current_node.is_leaf:
                        self.traversed_nodes.append(current_node)
                    
                    if child_index:
                        current_node = current_node.children[child_index]
                    else:
                        current_node = current_node.children[-1]

                if current_node.is_leaf:
                    tree_traversed = True

        current_node.insert(value)

        # Check if need to split the nodes and push up
        if len(current_node.keys) >= self.order:
            median_ind = math.ceil(len(current_node.keys) / 2)
            median_key = current_node.keys[median_ind-1]
            split_nodes = current_node.split(median_ind-1)

            # If no parent node create one
            if len(self.traversed_nodes) == 0:
                parent_node = Node(self.order, False)
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
            


                
                

                
                







# class BPTree:
#     def __init__(self, order=3):
#         self.order = order
#         self.root = Node(order, is_leaf=True)
    
#     def insert(self, value, current_node: Node):

#         if not current_node.is_leaf:
#             for ind in range(len(current_node.keys)):
#                 if value < current_node.keys[ind]:
#                     child_index = ind
#                     break
            
#             if child_index:
#                 self.insert(value, current_node.children[child_index])
#             else:
#                 self.insert(value, current_node.children[-1])


#         elif current_node.is_leaf:
#             current_node.insert(value)
        
#             if len(current_node.keys) > current_node.max_num_keys:
#                 median_index = math.ceil(len(current_node.keys) / 2)
#                 split_node_keys = [current_node.keys[:median_index-1], current_node.keys[median_index-1:]]

#                 new_leaf_nodes = []
#                 for keys in split_node_keys:
#                     new_leaf_node = Node(self.order, is_leaf=True)
#                     new_leaf_node.keys = keys
#                     new_leaf_nodes.append(new_leaf_node)

#                 # Check if node has parent and push key to parent
#                 if current_node.parent:
#                     print("HAS PARENT")
#                     # TODO: How to handle replacin new children??? !!!!!!
#                     current_node.parent.children = new_leaf_nodes
                    
#                     self.insert(current_node.keys[median_index-1], current_node.parent)
#                 else:
#                     print("DOES NOT HAVE PARENT")
#                     new_parent = Node(self.order, is_leaf=False)
#                     new_parent.children = new_leaf_nodes
#                     self.insert(current_node.keys[median_index-1], new_parent)

#             return
        
        


