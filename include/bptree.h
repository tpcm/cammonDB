typedef struct Node t_node;

typedef struct Node {
    int order;
    int *keys;
    t_node *children;
    bool is_leaf;
} t_node;

t_node *insert_key(t_node *node, int *key) {
    if (!node) {
        return NULL;
    }
    if (len(node->keys) == 0) {
        node->keys = key;
    }
}