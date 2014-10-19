import random

""" 11.1
You are given two sorted arrays, A and B, where
A has a large enough buffer at the end to hold B.
Write a method to merge B into A in sorted order
"""


""" 11.2
Write a method to sort an array of strings so that
all the anagrams are next to each other
"""
a = ['abc', '123', 'cba', '321', 'ab', '132', 'ba']
def groupAnagrams(list_):
    return sorted(list_, cmp=lambda x, y: 1 if sorted(x) < sorted(y) else -1)
def groupAnagramsHash(list_):
    d = {}
    final = []
    for word in a:
        sorted_ = ''.join(sorted(word))
        if sorted_ in d:
            d[sorted_].append(word)
        else:
            d[sorted_] = list([word])
    # Same thing as
    # result = []
    # for i in d.values():
    #   for j in i:
    #       result.append(j)
    return [m for k in d.values() for m in k]

""" 11.3
Given a sorted array of n integers that has been roated
unknown number of times, write code to find an element in the 
array. You may assume that the array was originally sorted in 
increasing order
"""
# a = [1, 1, 4, 2, 1, 1, 1]
def pivotedBinarySearch(list_, num):
    return findPivot(list_, 0, len(list_) - 1, num)
def findPivot(list_, left, right, num):
    if left > right: return -1
    mid = left + (right - left) // 2 # left + (high - low) / 2 overflow
    if list_[mid] == num: return mid
    if list_[left] < list_[mid]: # might be an 1 off error, <= / <
        # left side is sorted
        # check if value is in between these values
        if num >= list_[left] and num <= list_[mid]: # is num in between left?
            return findPivot(list_, left, mid - 1, num)
        else: # send to the right since it is greater than list_[mid]
            return findPivot(list_, mid + 1, right, num)
    elif list_[mid] < list_[left]: # right side is correctly sorted
        if num >= list_[mid] and num <= list_[right]:
            return findPivot(list_, mid + 1, right, num)
        else:
            return findPivot(list_, left, mid - 1, num)
    elif list_[mid] == list_[left]:
        if list_[mid] != list_[right]:
            return findPivot(list_, mid + 1, right, num)
        else:
            result = findPivot(list_, left, mid - 1, num)
            if result == -1:
                return findPivot(list_, mid + 1, right, num)
            else:
                return result
    return -1

""" 11.4
Given a sorted array of strings which is interpersed with empty strings, 
write a method to find the location of a given string
"""
def find_string(list_, s):
    return find_aux(list_, 0, len(list_), s)
def find_aux(list_, left, right, s):
    mid = left + (right - left) // 2
    lbound = mid - 1
    rbound = mid + 1
    if list_[mid] == '':
        while True:
            if lbound < left and rbound > right: return -1
            if lbound > left and list_[lbound] != '':
                mid = lbound
                break
            elif rbound < right and list_[rbound] != '':
                mid = rbound
                break
            lbound -= 1
            rbound += 1
    if list_[mid] == s: return mid
    elif list_[mid] < s:
        return find_aux(list_, mid + 1, right, s)
    else:
        return find_aux(list_, left, mid-1, s)

""" 11.6
Given a M x N matrix in which each row and each column is sorted in 
ascending order, write a method to find an element
"""
def findNumMatrix(matrix, num):
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == num:
            return (row, col)
        elif matrix[row][col] > num:
            col -= 1
        else:
            row += 1
    return (-1, -1)
""" 11.7
A circus is designing a tower routine consisting of people standing
atop one another's shoulders. For practical and aesthetic reasons,
each person must be both shorter and lighter than the person below 
him or her. Given the heights and weights of each person in the circus,
write a method to compute the largest possible number of people in such
a tower
"""
def towerRoutine():
    pass

# Dyanmic Programming
def find_subsequence(list_):
    print list_


"""Problem 1
Given an array A[0... n - 1] of n numbers containing repetition of some number.
Given an algorithm for checking whether there are reapeated elements or not.
Assume that we are not allowed to use additional space
"""
def find_repetition(list_):
    # This is O(n) complexity but requires O(n) space
    d = {}
    for i in list_:
        if i in d: return True
        else: 
            d[i] = True
    return False
    # This is O(n + nlogn) but requires no space complexity
    # list_ = sorted(list_) # O(nlongn)
    # for i in xrange(0, len(list_) - 1):
    #     if list_[i] == list_[i+1]: return True
    # return False
    # could be done with return len(list_) != len(set(list_))

"""Find the kth smallest element"""
def partition(list_, left, right):
    pivotIndex = left + (right - left) // 2
    pivot = list_[pivotIndex]
    lbound = 0
    rbound = right
    while True:
        while lbound < rbound and list_[lbound] < pivot:
            lbound += 1
        while lbound < rbound and list_[rbound] > pivot:
            rbound -= 1
        if lbound == rbound:
            break
        list_[lbound], list_[rbound] = list_[rbound], list_[lbound]
    return lbound
def kth_element(list_, left, right, k):
    index = partition(list_, left, right)
    ans = k - 1
    if ans == index: 
        return list_[index]
    elif ans < index:
        return kth_element(list_, left, index - 1, k)
    elif ans > index:
        return kth_element(list_, index + 1, right, k)

def swap_num(x, y):
    """ 17.1
        Write a function to swap a number in place 
        (that is, without temporary variables)
    """
    x = x^y
    y = x^y
    x = x^y
    return (x, y)

def won_game(board, n=3):
    """ 17.2
        Design an algorithm to see if someone has won a game 
        of tic tac toe
    """
    for row in xrange(0, n):
        # checking for row
        if board[row][0] != -1 and \
           board[row][0] == board[row][1] and \
           board[row][0] == board[row][2]: 
               return board[row][0]

        # checking for columns
        elif board[0][row] != -1 and \
                board[0][row] == board[1][row] and \
                board[0][row] == board[2][row]:
                    return board[0][row]

        # checking for diagonals
        elif board[0][0] != -1 and \
             board[0][0] == board[1][1] and \
             board[0][0] == board[2][2]:
                 return board[0][0]
        elif board[2][0] != -1 and \
             board[2][0] == board[1][1] and \
             board[2][0] == board[0][2]:
                 return board[2][0]
    return -1

def trailing_zeros(n):
    """ 17.3
        Write an algorithm which computes the number of trailing zeros
        in n factorial 
    """
    count = 0
    if n < 0: return -1
    i = 5
    while n/i > 0:
        count += n / i
        i *= 5
    return count



    



