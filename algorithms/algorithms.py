# -*- coding: utf-8 -*-
"""Collection of Classic Algorithms
"""

from auxilary import swap

def bubblesort(list_):
    """Bubble Sort Algorithm
    Complexity: O(n^2)
    Space: O(1)
    """
    size = len(list_) - 1
    swap_ = True
    while swap_ and size > 0:
        swap_ = False
        for i in xrange(0, size):
            if list_[i] > list_[i+1]:
                swap_ = True
                swap(list_, i, i + 1)
        size -= 1

def selection_sort(list_):
    """Selection Sort Algorithm
    Complexity: O(n^2)
    Space: O(1)
    """
    size = len(list_) - 1
    for i in range(size, 0, -1):
        index = 0
        for j in xrange(1, i + 1):
            if list_[j] > list_[index]:
                index = j
        swap(list_, i, index)

def insertion_sort(list_):
    """Insertion Sort Algorithm
    Complexity: O(n^2)
    Space: O(1)
    """
    for i in xrange(1, len(list_)):
        current_value = list_[i]
        position = i
        while position > 0 and list_[position-1] > current_value:
            list_[position] = list_[position-1]
            position -= 1
        list_[position] = current_value

def shell_sort(list_):
    """Shell Sort Algorithm
    Complexity: O(n^2)
    Space: O(1)
    """
    k = len(list_) // 3
    while k > 0:
        for i in range(k):
            insertion_sort_gap(list_, i, k)
        k //= 3
def insertion_sort_gap(list_, start, gap):
    """Auxilary function for Shell Sort Algorithm"""
    for i in range(start+gap, len(list_), gap):
        current_value = list_[i]
        position = i
        while position >= gap and list_[position-gap] > current_value:
            list_[position] = list_[position - gap]
            position = position - gap
        list_[position] = current_value
def merge_sort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
def quick_sort(list_):
    quick_sort_aux(list_, 0, len(list_))
def quick_sort_aux(list_, left, right):
    if left < right:
        pivot = partition(list_, left, right)
        quick_sort_aux(list_, left, pivot - 1)
        quick_sort_aux(list_, pivot + 1, right)
def partition(list_, left, right):
    pivot = list_[left]
    lbound = left
    print list_
    for i in xrange(left + 1, right):
        if list_[i] < pivot:
            lbound += 1
            swap(list_, i, lbound)
    swap(list_, left, lbound)
    return lbound
