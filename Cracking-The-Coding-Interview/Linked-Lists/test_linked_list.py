from contextlib import contextmanager
from StringIO import StringIO
import linkedlist as ll
import unittest
import sys


""" Linked List Node object used to implement/test with"""
class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    def __str__(self):
        temp = self
        data = ''
        while temp != None:
            data += str(temp.data) + '->'
            temp = temp.next
        return data[:-2]

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.head = self.generate_list()
    @contextmanager
    def capture(self):
        """ Function used to capture stdout to StringIO 
            so that testing is possible
        """
        new_out = StringIO()
        old_out = sys.stdout
        try:
            sys.stdout = new_out
            yield sys.stdout
        finally:
            sys.stdout = old_out
    def parse_node(self, node):
        if node == None: return None
        with self.capture() as f:
            print node
            return [int(_) for _ in f.getvalue().rstrip().split('->')]
    def generate_list(self):
        head = Node(10)
        head.next = Node(5)
        head.next.next = Node(10)
        head.next.next.next = Node(20)
        head.next.next.next.next = Node(40)
        head.next.next.next.next.next = Node(20)
        head.next.next.next.next.next.next = Node(20)
        return head

    def test_remove_deplicates_from_linked_list(self):
        head = self.generate_list()
        ll.remove_duplicates(self.head)
        self.assertEqual([10,5,20,40], self.parse_node(self.head))
        ll.remove_duplicates_hash(head)
        self.assertEqual([10,5,20,40], self.parse_node(head))
    def test_kth_last_element_of_singly_linked_list(self):
        self.assertEqual(20, ll.kth_last_element(self.head, 0))
        self.assertEqual(20, ll.kth_last_element(self.head, 1))
        self.assertEqual(40, ll.kth_last_element(self.head, 2))
    def test_delete_middle_node(self):
        ll.delete_middle_node(self.head.next)
        result = self.parse_node(self.head)
        self.assertEqual([10,10,20,40,20,20], result)
    def test_partition_linked_list_around_value(self):
        head = ll.partition_list(self.head, 40)
        result = self.parse_node(head)
        self.assertEqual([10,5,10,20,20,20,40], result)
    def test_sum_up_linked_lists(self):
        x = Node(6)
        x.next = Node(1)
        x.next.next = Node(7)
        y = Node(2)
        y.next = Node(9)
        y.next.next = Node(5)
        result = ll.sum_linked_lists(x, y)
        self.assertEqual([8,0,3,1], self.parse_node(result))
    def test_detect_beginning_of_loop(self):
        head = self.head
        while head.next != None: head = head.next
        head.next = Node(60, self.head.next.next)
        beginning = ll.beginning_of_loop(self.head)
        self.assertEqual(head.next.next, beginning)
    def test_linked_list_is_palindrome(self):
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(3)
        head.next.next.next.next = Node(2)
        head.next.next.next.next.next = Node(1)
        self.assertTrue(ll.is_palindrome(head))
    

if __name__ == '__main__':
    unittest.main()
