typedef struct BPTreeNode {
    int num_keys;
    int *keys;
    struct BPTreeNode *children;
    bool is_leaf;
} t_bptree;