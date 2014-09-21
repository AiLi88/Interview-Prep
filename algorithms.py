from auxilary import *

""" Bubble Sort Algorithm
Complexity: O(n^2)
Space: O(1)
"""
def bubblesort(list_):
    n = len(list_) - 1
    swap_ = True 
    while swap_ and n > 0:
        swap_ = False
        for i in xrange(0, n):
            if list_[i] > list_[i+1]:
                swap_ = True
                swap(list_, i, i + 1)
        n -= 1

""" Selection Sort Algorithm
Complexity: O(n^2)
Space: O(1)
"""
def selection_sort(list_):
    n = len(list_) - 1
    for i in range(n, 0, -1):
        index = 0
        for j in xrange(1, i + 1):
            if list_[j] > list_[index]:
                index = j
        swap(list_, i, index)
def insertion_sort(list_):
    for i in xrange(1, len(list_)):
        currentValue = list_[i]
        position = i
        while position > 0 and list_[position-1] > currentValue:
            list_[position] = list_[position-1]
            position -= 1
        list_[position] = currentValue
def shell_sort(list_):
    k = len(list_) // 3
    while k > 0:
        for i in range(k):
            insertion_sort_gap(list_, i, k)
        k //= 3
def insertion_sort_gap(list_, start, gap):
    for i in range(start+gap, len(list_), gap):
        currentValue = list_[i]
        position = i
        while position >= gap and list_[position-gap] > currentValue:
            list_[position] = list_[position - gap]
            position = position - gap
        list_[position] = currentValue
def merge_sort(list_):
    merge_sort_aux(list_, 0, len(list_) - 1)
def merge_sort_aux(list_, left, right):
    print list_


