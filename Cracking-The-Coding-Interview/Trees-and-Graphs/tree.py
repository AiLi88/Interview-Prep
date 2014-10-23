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
def size(root):
    if root == None:
        return 0
    return 1 + size(root.left) + size(root.right)
def max_depth(root):
    if root == None: 
        return 0
    return max(1+max_depth(root.left), 1+max_depth(root.right))
def min_value(root):
    temp = root
    while temp.left != None:
        temp = temp.left
    return temp.data
def in_order(root):
    if root == None:
        return
    in_order(root.left)
    print root.data
    in_order(root.right)
def pre_order(root):
    if root == None:
        return
    print root.data
    pre_order(root.left)
    pre_order(root.right)
def post_order(root):
    if root == None:
        return
    post_order(root.left)
    post_order(root.right)
    print root.data
def get_paths(root):
    paths = []
    get_paths_aux(root, paths, [])
    return paths
def get_paths_aux(root, paths, path):
    if root.left == None and root.right == None:
        paths.append(path + [root.data])
        return
    else:
        path.append(root.data) 
        get_paths_aux(root.left, paths, path)
        get_paths_aux(root.right, paths, path)
        path.pop()
def mirror_tree(root):
    temp = root
    return mirror_tree_aux(root)
def mirror_tree_aux(root):
    if root == None:
        return
    temp = root.left
    root.left = root.right
    root.right = temp
    mirror_tree_aux(root.left)
    mirror_tree_aux(root.right)
def get_height(root):
    if root == None: return 0
    return max(1+get_height(root.left), 1+get_height(root.right))
def balance(root):
    if root == None:
        return True
    diff = abs(get_height(root.left) - get_height(root.right))
    if diff > 1: return False
    return balance(root.left) and balance(root.right)
def array_into_tree_aux(array, left, right):
    if left > right:
        return None
    mid = left + (right - left) // 2
    return Node(array[mid], array_into_tree_aux(array, left, mid-1), array_into_tree_aux(array, mid+1, right))
    
def array_into_tree(array):
    return array_into_tree_aux(array, 0, len(array)-1)

def breadth_traversal(root):
    import Queue
    q = Queue.Queue()
    q.put(root)
    level = 0
    while q.empty() == False:
        node = q.get()
        print node.data
        if node.left != None:
            q.put(node.left)
        if node.right != None:
            q.put(node.right)
def linked_list_depth_aux(root, lists, level):
    if root == None: return
    lists[level].append(root.data)
    linked_list_depth_aux(root.left, lists, 1+level)
    linked_list_depth_aux(root.right, lists, 1+level)
    return lists
def linked_list_depth(root):
    size = max_depth(root)
    l = [[] for _ in xrange(0, size)]
    return linked_list_depth_aux(root, l, 0)












