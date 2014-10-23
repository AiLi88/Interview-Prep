from test_linked_list import Node

""" 2.1
    Write code to remove duplicates from an unsorted linked list
    FOLLOW UP
    How would you solve this problem if a temporary buffer is not
    allowed?
"""
def remove_duplicates(head):
    """ O(n^2 solution) 
        O(n) can be achieved by using hash table
    """
    if head == None: return
    while head != None and head.next != None:
        cursor = head
        while cursor.next != None:
            if cursor.next.data == head.data:
                cursor.next = cursor.next.next
            else:
                cursor = cursor.next
        head = head.next
def remove_duplicates_hash(head):
    if head == None:
        return
    cache = {}
    prev = None
    while head != None:
        if head.data in cache:
            prev.next = head.next
        else:
            cache[head.data] = True
            prev = head
        head = head.next

""" 2.2
    Implement an algorithm to find the kth to last element of a
    singly linked list
"""
def kth_last_element(head, k):
    # No error checking done, but should if not given guarantee that
    # the list has at least k elements
    cursor = head
    for i in xrange(0, k):
        cursor = cursor.next
    while cursor.next != None:
        cursor = cursor.next
        head = head.next
    return head.data

""" 2.3
    Implement an algorithm to delete a node in the middle of a singly
    linked list, given only access to that node.
"""
def delete_middle_node(node):
    # Assuming node is NOT at the end
    node.data = node.next.data
    node.next = node.next.next

""" 2.4
    Write code to partition a linked list around a value x, such that
    all nodes less than x come before all nodes greater than or equal
    to x
"""
def partition_list(head, x):
    # the two lists that represents < , >  pivot value(x)
    lesser = None
    lesserTail = None

    greater = None
    greaterTail = None

    while head != None:
        next = head.next
        head.next = None
        if head.data < x:
            if lesser == None:
                lesser = head
                lesserTail = lesser
            else:
                lesserTail.next = head
                lesserTail = head
        else:
            if greater == None:
                greater = head
                greaterTail = greater
            else:
                greaterTail.next = head
                greaterTail = head
        head = next
    if lesser == None:
        return greater
    lesserTail.next = greater
    return lesser

""" 2.5
    You have two numbers represented by a linked list, where each node
    contains a single digit. The digts are stored in reverse order, such that
    the 1's digit is at the head of the list. Write a function that adds the
    two numbers and returns the sum as a linked list.

    FOLLOW UP
    Suppose the digits are stored in forward order. Repeat the above problem
"""
def sum_linked_lists(x, y, carry=0):
    if x == None and y == None and carry == 0:
        return None
    if x != None:
        carry += x.data
    if y != None:
        carry += y.data
    return Node(carry % 10, sum_linked_lists(None if x == None else x.next,
                                             None if y == None else y.next,
                                             carry/10))

""" 2.6
    Given a circular linked list, implement an algorithm which returns
    the node at the beginning of the loop
"""
def beginning_of_loop(head):
    hare = head
    tortoise = head

    while hare != None and hare.next != None:
        tortoise = tortoise.next
        hare = hare.next.next
        if tortoise == hare:
            break
    if tortoise == None or hare == None:
        return None
    tortoise = head
    while tortoise != hare:
        tortoise = tortoise.next
        hare = hare.next
    # Should be at the beginning of the loop
    return tortoise

""" 2.7
    Implement a function to check if a linked list is a palindrome

    Solution
    Reverse linked list, check for equality

    Also you can use stack to keep track of half the list
    You can get to the middle by tortoise and hare approach
"""
def reverse_list(head, prev=None):
    if head == None:
        return prev
    next = head.next
    head.next = prev
    return reverse_list(next, head)

def is_palindrome(head):
    """ You could reverse the linked list and compare """
    reversed = reverse_list(head)
    while head != None:
        if reversed == None or head.data != reversed.data:
            return False
        head = head.next
        reversed = reversed.next
    return True








