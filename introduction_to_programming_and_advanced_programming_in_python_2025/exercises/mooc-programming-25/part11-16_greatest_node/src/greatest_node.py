# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def print_nodes(root: Node):
    print(root.value)

    if root.left_child is not None:
        print_nodes(root.left_child)

    if root.right_child is not None:
        print_nodes(root.right_child)

def greatest_node(root: Node):
    value       = root.value
    left_value  = value
    right_value = value

    if root.left_child is not None:
        left_value = greatest_node(root.left_child)
    if root.right_child is not None:
        right_value = greatest_node(root.right_child)

    greatest = max(value, left_value, right_value)
    return greatest

if __name__ == "__main__":
    # first, let's define a tree so we can test our function; I'll use the example from the course
    tree = Node(2)
    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)
    
    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)
    
    # another way of declaring the same tree:
    tree2 = Node(2, Node(3, Node(5), Node(8)), Node(4, None, Node(11)))
    
    # we can be sure both trees are the same by using print_node, which must print the same nodes in the same order:
    print("=" * 50)
    print("First Tree:")
    print_nodes(tree)
    print("=" * 50)
    print("Second Tree:")
    print_nodes(tree2)
    print("=" * 50)
    # Now let's do what the exercise asked us to do:
    print("Find the greatest node in a tree:")
    print(greatest_node(tree))
