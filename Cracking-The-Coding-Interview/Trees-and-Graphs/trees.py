class Node(object):
    def __init__(self, data, lptr=None, rptr=None):
        self.data = data
        self.left = lptr
        self.right = rptr
    def __str__(self, depth=0):
        ret = ""
        # Print right branch
        if self.right != None:
            ret += self.right.__str__(depth + 1)
        # Print own value
        ret += "\n" + ("    "*depth) + str(self.data)
        # Print left branch
        if self.left != None:
            ret += self.left.__str__(depth + 1)
        return ret

node = Node(10)
node.left = Node(20)
node.right = Node(30)
node.left.left = Node(120)

class GraphNode(object):
    def __init__(self, value, state='Unvisited', neighbors=[]):
        self.value = value
        self.state = state
        self.neighbors = neighbors
    def __str__(self):
        data = ''
        for neighbor in self.neighbors:
            data += neighbor.value + ' '
        return '%s(%s): %s' % (self.value, self.state, data)
graph = [ GraphNode('A', neighbors=[GraphNode('B'), GraphNode('C')] ),
          GraphNode('B', neighbors=[GraphNode('C'), GraphNode('D')]),
          GraphNode('C', neighbors=[GraphNode('D')]),
          GraphNode('D', neighbors=[GraphNode('C')]),
          GraphNode('E', neighbors=[GraphNode('F')]),
          GraphNode('F', neighbors=[GraphNode('C')]),
        ]

"""graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
"""

""" 4.1
    Implement a function to check if a binary tree is balanced.
    For the purposes of this question, a balanced tree is defined
    to be a tree such that the heights of the two subtrees of any
    node never differ by more than one
"""
def get_height(root):
    if root == None: return 0
    return 1 + max(get_height(root.left), get_height(root.right))
def is_balanaced(root):
    """ O(n^2) time """
    if root == None:
        return True
    left_tree = get_height(root.left)
    right_tree = get_height(root.right)
    if abs(left_tree - right_tree) > 1:
        return False
    else:
        return (is_balanaced(root.left) and
                is_balanaced(root.right))
def get_height_optimal(root):
    if root == None:
        return 0
    left_tree = get_height_optimal(root.left)
    if left_tree == -1:
        return -1
    right_tree = get_height_optimal(root.right)
    if right_tree == -1:
        return -1
    height_diff = abs(left_tree - right_tree)
    if height_diff > 1:
        return -1
    else:
        return 1 + max(get_height_optimal(root.left), get_height_optimal(root.right))
def is_balanced_optimal(root):
    """ O(n) time; O(H) space; H = height of tree """
    return get_height_optimal(root) != -1

""" 4.2
    Given a directed graph, design an algorithm to find out whether there is
    a route between two nodes
"""
def is_route(graph, start, end):
    """ Discuss wehether pros/cons of breadth first search vs depth first search 
        DFS = May go into sub graph deep before finding out it doesn't exist
    """
    from collections import deque
    q = deque()
    for node in graph:
        node.state = 'Unvisited'
    start.state = 'Visiting'
    q.appendleft(start)
    while len(q) != 0:
        u = q.popleft()
        for v in u.neighbors:
            if v.state == 'Unvisited':
                if end == v:
                    return true
                else:
                    v.state = 'Visiting'
                    q.appendleft(v)
        u.state = 'Visited'
    return False

""" 4.3
    Given a sorted (increasing order) array with uniquje integer elements,
    write an algorithm to create a binary search tree with minimal height
"""
def array_to_tree_aux(array, left, right):
    if left > right: return None
    mid = left + (right - left) // 2
    return Node(mid, 
                array_to_tree_aux(array, left, mid-1),
                array_to_tree_aux(array, mid+1, right))
def array_to_tree(array):
    return array_to_tree_aux(array, 0, len(array)-1)
# print array_to_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

""" 4.4
    Given a binary tree, desig an algorithm which creates a linked list
    of all the nodes at each depth (e.g, if you have a tree with depth D,
    you'll have D linked lists)
"""
def tree_to_list_aux(root, lists, level):
    if root == None: return
    lists[level].append(root.data)
    tree_to_list_aux(root.left, lists, 1+level)
    tree_to_list_aux(root.right, lists, 1+level)
def tree_to_lists(root):
    height = get_height(root)
    l = [[] for _ in range(height)]
    tree_to_list_aux(root, l, 0)
    return l
#print tree_to_lists(node)

""" 4.5
    Implement a function to check if a binary tree is a binary search tree
"""
def modified_inorder_traversal(root, array):
    if root == None:
        return None
    modified_inorder_traversal(root.left, array)
    array.append(root.data)
    modified_inorder_traversal(root.right, array)
def is_binary_search_tree(root):
    """ Naive Solution
        Keep in mind this doesn't work with duplicates in the array
    """
    a = []
    modified_inorder_traversal(root, a)
    for i in xrange(0, len(a) - 1):
        if a[i] > a[i+1]: return False
    return True
def is_binary_search_tree_optimal_aux(root, min_value, max_value):
    if root == None:
        return True
    if root.data < min_value or root.data > max_value: return False
    return (is_binary_search_tree_optimal_aux(root.left, min_value, root.data) and
            is_binary_search_tree_optimal_aux(root.right, root.data, max_value))
def is_binary_search_tree_optimal(root):
    from sys import maxint
    return is_binary_search_tree_optimal_aux(root, -maxint-1, maxint)

# print is_binary_search_tree(node)
# print is_binary_search_tree_optimal(node)

# root = Node(100)
# root.left = Node(99)
# root.right = Node(101)
# print is_binary_search_tree_optimal(root)

""" 4.6
    Write an algorithm to find the 'next' node (i.e, in-order successor)
    of a given node in a binary search tree. You may assume that each node
    has a link to its parent
"""
def in_order_successor(root):
    if root == None: return None

    # Found right children, return left most node of right subtree
    if root.right != None:
        return left_most_child(root.right)
    else:
        # Since there is no right child, print the parent node
        q = root
        x = q.parent
        while x != None and x.left != q:
            q = x
            x = x.parent
        return x
def left_most_child(root):
    if root == None: return None
    while root.left != None:
        root = root.left
    return root

""" 4.7
    Design an algorithm and write code to find the first common ancestor
    of two nodes in a binary tree. Avoid storing additional nodes in a
    data structure. NOTE: This is not necessarily a binary search tree
"""
