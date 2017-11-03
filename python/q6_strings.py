# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0

# Given an int count of a number of donuts, return a string of the
# form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word
# 'many' instead of the actual count.
    
def donuts(count):
    if count >= 10: 
        cnt_str = 'many' 
    else: 
        cnt_str = str(count)
    return 'Number of donuts: ' + cnt_str


#Given a string s, return a string made of the first 2 and the last
#2 chars of the original string, so 'spring' yields 'spng'.
#However, if the string length is less than 2, return instead the
#empty string.

def both_ends(s):
    if len(s) >= 2:
        b_ends = s[:2] + s[-2:]
    else:
        b_ends = ''
    return b_ends

#Given a string s, return a string where all occurences of its
#first char have been changed to '*', except do not change the
#first char itself. e.g. 'babble' yields 'ba**le' Assume that the
#string is length 1 or more.


def fix_start(s):
    temp = ['*' if c == s[0] else c for c in s]
    return s[0] + ''.join(temp[1:])


   
#Given strings a and b, return a single string with a and b
#separated by a space '<a> <b>', except swap the first 2 chars of
#each string. Assume a and b are length 2 or more.


def mix_up(a, b):
    return b[:2] + a[2:] + ' ' + a[:2] + b[2:]

#     Given a string, if its length is at least 3, add 'ing' to its end.
#     Unless it already ends in 'ing', in which case add 'ly' instead.
#     If the string length is less than 3, leave it unchanged. Return
#     the resulting string.

def verbing(s):
    if len(s) < 3:
        return s
    else: 
        if s[-3:] == 'ing':
            return s + 'ly'
        else: return s + 'ing'

#Given a string, find the first appearance of the substring 'not'
#and 'bad'. If the 'bad' follows the 'not', replace the whole
#'not'...'bad' substring with 'good'. Return the resulting string.
#So 'This dinner is not that bad!' yields: 'This dinner is
#good!'

import re

def not_bad(s):
    return re.sub(r"not.*bad", "good", s)


#     Consider dividing a string into two halves. If the length is even,
#     the front and back halves are the same length. If the length is
#     odd, we'll say that the extra char goes in the front half. e.g.
#     'abcde', the front half is 'abc', the back half 'de'. Given 2
#     strings, a and b, return a string of the form a-front + b-front +
#     a-back + b-back

import math

def front_back(a, b):
    half = lambda a: math.ceil(len(a)/2)
    return a[:half(a)] + b[:half(b)] + a[half(a):] + b[half(b):]

