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
print groupAnagramsHash(a)


