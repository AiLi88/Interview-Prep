from contextlib import contextmanager
from StringIO import StringIO
from tree import *
import unittest
import sys

class TestTreeAlgorithms(unittest.TestCase):
    def setUp(self):
        self.root = Node(20)
        self.root.left = Node(15)
        self.root.right = Node(25)
        self.root.left.left = Node(10)
        self.root.left.right = Node(14)
        self.root.right.left = Node(24)
        self.root.right.right = Node(34)
    @contextmanager
    def capture(self):
        new_out = StringIO()
        old_out = sys.stdout
        try:
            sys.stdout = new_out
            yield sys.stdout
        finally:
            sys.stdout = old_out
    def test_count_size_of_tree(self):
        root = None
        self.assertEqual(0, size(root))
        root = Node(10)
        self.assertEqual(1, size(root))
        root.left = Node(10)
        root.left.left = Node(10)
        self.assertEqual(3, size(root))
        root.right = Node(4)
        self.assertEqual(4, size(root))
        self.assertEqual(7, size(self.root))
    def test_max_depth_of_tree(self):
        root = None
        self.assertEqual(0, max_depth(root))
        root = Node(2)
        self.assertEqual(1, max_depth(root))
        root.left = Node(5)
        root.right = Node(10)
        self.assertEqual(2, max_depth(root))
        root.left.left = Node(6)
        self.assertEqual(3, max_depth(root))
        root.right.right = Node(20)
        root.right.right.right = Node(20)
        root.right.right.right.right = Node(20)
        root.right.right.right.right.right = Node(20)
        root.right.right.right.right.right.right = Node(20)
        self.assertEqual(7, max_depth(root))
        self.assertEqual(3, max_depth(self.root))
    def test_min_value(self):
        self.assertEqual(10, min_value(self.root))
    def test_print_tree_in_order(self):
        output = None
        with self.capture() as out:
            in_order(self.root)
            output = out
        self.assertEqual('10 15 14 20 24 25 34',output.getvalue().rstrip().replace('\n', ' '))
    def test_print_tree_in_preorder(self):
        output = None
        with self.capture() as out:
            pre_order(self.root)
            output = out
        self.assertEqual('20 15 10 14 25 24 34', output.getvalue().rstrip().replace('\n', ' '))
    def test_print_tree_in_postorder(self):
        output = None
        with self.capture() as out:
            post_order(self.root)
            output = out
        self.assertEqual('10 14 15 24 34 25 20', output.getvalue().rstrip().replace('\n', ' '))
    def test_get_all_paths_from_root_to_leafs(self):
        paths = [[20, 15, 10], [20, 15, 14],
                 [20, 25, 24], [20, 25, 34]]
        self.assertEqual(paths, get_paths(self.root))
    def test_make_a_mirror_of_tree(self):
        root = Node(4)
        root.left = Node(2)
        root.right = Node(5)
        root.left.left = Node(1)
        root.left.right = Node(3)
        with self.capture() as out:
            m_root = mirror_tree(root)
            in_order(root)
            m_root_res = out.getvalue().rstrip().replace('\n', ' ')
            self.assertEqual("5 4 3 2 1", m_root_res)
            self.assertEqual("5 4 3 2 1", m_root_res)
    def test_get_height_of_tree(self):
        root = Node(2)
        self.assertEqual(1, get_height(root))
        root.left = Node(3)
        self.assertEqual(2, get_height(root))
        self.assertEqual(3, get_height(self.root))
    def test_tree_is_balanced(self):
        self.assertEqual(True, balance(self.root))
    def test_sorted_array_to_tree(self):
        array = [0, 4, 6, 9, 12, 16, 20]
        root = array_into_tree(array)
        with self.capture() as out:
            in_order(root)
            result = out.getvalue().rstrip().replace('\n', ' ')
            self.assertEqual('0 4 6 9 12 16 20', result)
    def test_breadth_first_traversal(self):
        with self.capture() as f:
            breadth_traversal(self.root)
            result = f.getvalue().rstrip().replace('\n', ' ')
            self.assertEqual("20 15 25 10 14 24 34", result) 
    def test_linked_lists_at_each_level(self):
        print linked_list_depth(self.root)
class TestPython(unittest.TestCase):
    def test_how_queues_work_in_python(self):
        import Queue
        q1 = Queue.Queue()
        q2 = Queue.Queue()
        q1.put(1)
        q2.put(2)
        self.assertFalse(q1 == q2)
        q1 = q2
        self.assertTrue(q1 == q2)
        q2.empty()
        self.assertTrue(q1 == q2)



if __name__=='__main__':
    unittest.main()
