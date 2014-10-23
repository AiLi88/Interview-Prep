""" 1.1
    Implement an algorithm to determine if a string has all unique characters.
    What if you cannot use additional data structures?
"""
def unique_characters(string):
    """ Assuming the string is ascii 
        You could create an boolean array of size 256.
        Convert each character to int, and check if the value exists

        Better solution might be using hash. Check if character exists
        in hash, if not, insert it
    """
    cache = {}
    string = list(string)
    for s in string:
        if s in cache:
            return False
        else:
            cache[s] = True
    return True

""" 1.2
    Implement a function void reverse(char* str) in C or C++ which 
    reverses a null terminated string
"""

""" 1.3
    Given two strings, write a method to decide if one is a permutation
    of the other.
"""
def permutation(string, perm):
    """ Sort both strings and check for equality O(nlogn)
        Another valid answer and (faster time wise) would make a hash 
        map of string and count individual characters
    """
    return sorted(string) == sorted(perm)

""" 1.4
    Write a method to replace all spaces in a string with '%20'. You
    may assume that the string has sufficient space at the end of the 
    string to hold the additional characters, and that you are given
    the "true" length of the string. (Note: if implementing in Java,
    please use a character array so you can perform this operation in
    place.)
"""

""" 1.5
    Implement a method to perform basic string compression using the 
    counts of repeated characters. For example, the string aabcccccaaa
    would become a2b1c5as3. If the "compressed" string would not become
    smaller than the original string, your method should return the
    original string.
"""

""" 1.6
    Given an image represented by an NxN matrix, where each pixel in the
    image is 4 bytes, write a method to rotate the image by 90 degrees.
    Can you do this in place?
"""

""" 1.7
    Write an algorithm such that if an element in an MxN matrix is 0, its
    entire row and column are set to 0
"""

""" 1.8
    Assume you have a method isSubstring which checks if one word is
    a substring of another. Given two strings, s1 and s2, write code
    to check if s2 is a rotation of s1 using only one call to is
    isSubString(e.g., "waterbottle" is a rotation of "erbottlewat")
"""
def isSubstring(string, substring):
    return substring in string
def is_rotation(string, rotated):
    length = len(string)
    if length != len(rotated) or length <= 0:
        return False
    return isSubstring(string+string, rotated)
