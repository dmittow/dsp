# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


#     Given a list of strings, return the count of the number of strings
#     where the string length is 2 or more and the first and last chars
#     of the string are the same.

def match_ends(words):
    match_words = [w for w in words if len(w) >= 2 and w[0] == w[-1]]
    return len(match_words)
   

    raise NotImplementedError

#     Given a list of strings, return a list with the strings in sorted
#     order, except group all the strings that begin with 'x' first.
#     e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
#          ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

def front_x(words):
    print(sorted([w for w in words if w[0] == 'x']) + sorted([w for w in words if w[0] != 'x']))


#     Given a list of non-empty tuples, return a list sorted in
#     increasing order by the last element in each tuple.
#     e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
#          [(2, 2), (1, 3), (3, 4, 5), (1, 7)].
def sort_last(tuples):
    return sorted(tuples, key = lambda t: t[-1])


#     Given a list of numbers, return a list where all adjacent equal
#     elements have been reduced to a single element, so [1, 2, 2, 3]
#     returns [1, 2, 3]. You may create a new list or modify the passed
#     in list.

def remove_adjacent(nums):
    if len(nums) > 1:
        dedup_nums = [nums[0]]
        for i,j in zip(range(0,len(nums)-1), range(1,len(nums))):
            if nums[i] != nums[j]:
                dedup_nums.append(nums[j])
        return dedup_nums
    else: return nums

#  Given two lists sorted in increasing order, create and return 
#  merged list of all the elements in sorted order. You may modify
#  the passed in lists. Ideally, the solution should work in "linear"
#  time, making a single pass of both lists.

def linear_merge(list1, list2):
    return sorted(list1 + list2)
