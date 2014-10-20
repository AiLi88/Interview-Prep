# -*- coding: utf-8 -*-
""" Classic Question 1
    You have 8 coins which are all the same weight, except for one which is slightly heavier
    than the others (you don't know which coin is heavier). You also have an old‐style balance,
    which allows you to weigh two piles of coins to see which one is heavier 
    (or if they are of equal weight).  What is the fewest number of weighings 
    that you can make which will tell you which coin is the heavier one?
     
    Solution
    Weigh the 2 sets of three. At this point, you will know which sets of three to pick from.
    Pick 2 of the three, and at this point you will know what the heavy coin is
"""

""" Classic Question #3: A to I
    Write a function to convert a string into an integer.  (This function is called A to I (or 
    atoi()) because we are converting an ASCII string into an integer.)

    C Solution
    int custom_atoi(char *str) {
        char *c = str;
        int sum = 0;
        int sign = 1;
        if (!*c)
            return 0;
        if (*c == '-') {
            sign = -1;
            ++c;
        }
        while (*c) { 
            if (is_num(*c) == 0) return 0;
            sum = sum * 10  + *c++ - '0';
        }
        return sign*sum;
    }
"""

""" Classic Question #4: Reversing the words in a string
    Write a function to reverse the order of words in a string in place.
"""
def reverse_string(string):
    left = 0
    right = len(string) - 1
    string = list(string) 
    while left < right:
        string[left], string[right] = string[right], string[left]
        left += 1
        right -= 1
    return ''.join(string)
def reverse_string_pythonic(string):
    return string[::-1]

""" Classic Sorts: Merge Sort """
def merge_aux(array, left, right):
    pass
def merge_sort_aux(array, left, right):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort_aux(array, left, mid)
        merge_sort_aux(array, mid+1, right)
        merge_aux(array, left, right)
def merge_sort(array):
    print array
    merge_sort_aux(array, 0, len(array) - 1)
    print array

""" Classic Sorts: Quick Sort """
def quick_sort_aux(array, left, right):
    if left < right:
        pivot = partition(array, left, right)
        quick_sort_aux(array, left, pivot-1)
        quick_sort_aux(array, pivot+1, right)
def quick_sort(array):
    quick_sort_aux(array, 0, len(array)-1)

""" Order Statistics
    Describe an algorithm to identify the kth smallest element in an array of n elements.
"""
def partition(array, left, right):
    pass
def kth_smallest_element(array, left, right, k):
    pass

""" Question: Nearest Neighbor
    Say you have an array containing information regarding n people.  Each person is 
    described using a string (their name) and a number (their position along a number 
    line).  Each person has three friends, which are the three people whose number is 
    nearest their own.  Describe an algorithm to identify each person's three friends.

    Solution
    Good answer: Sort the array in ascending order of the people's number.  For each 
    person, check the three people immediately before and after them.  Their three 
    friends will be among these six people.  This algorithm takes O(n log n) time, since 
    sorting the people takes that much time.
"""

""" Classic Question #5: Cycle in a Linked List
    
    Floyd-Cycle Detetection Algorithm
"""

""" Question: Compute 2^x """
def two_power(x):
    return 1 << x

""" Question: How can you quickly determine whether a number is a power of 2? """
def power_of_two(num):
    print num & (num - 1)

