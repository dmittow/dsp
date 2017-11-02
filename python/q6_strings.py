# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    if count >= 10: 
        cnt_str = 'many' 
    else: 
        cnt_str = str(count)
    return 'Number of donuts: ' + cnt_str

    #>>> donuts(4)
    #'Number of donuts: 4'
    #>>> donuts(9)
    #'Number of donuts: 9'
    #>>> donuts(10)
    #'Number of donuts: many'
    #>>> donuts(99)
    #'Number of donuts: many'



def both_ends(s):
    if len(s) >= 2:
        b_ends = s[:2] + s[-2:]
    else:
        b_ends = ''
    return b_ends

    #>>> both_ends('spring')
    #'spng'
    #>>> both_ends('Hello')
    #'Helo'
    #>>> both_ends('a')
    #''
    #>>> both_ends('xyz')
    #'xyyz'


def fix_start(s):
    temp = ['*' if c == s[0] else c for c in s]
    return s[0] + ''.join(temp[1:])
    raise NotImplementedError

    #>>> fix_start('babble')
    #'ba**le'
    #>>> fix_start('aardvark')
    #'a*rdv*rk'
    #>>> fix_start('google')
    #'goo*le'
    #>>> fix_start('donut')
    #'donut'
   



def mix_up(a, b):
    return b[:2] + a[2:] + ' ' + a[:2] + b[2:]


#     >>> mix_up('mix', 'pod')
#     'pox mid'
#     >>> mix_up('dog', 'dinner')
#     'dig donner'
#     >>> mix_up('gnash', 'sport')
#     'spash gnort'
#     >>> mix_up('pezzy', 'firm')
#     'fizzy perm'



def verbing(s):
    if len(s) < 3:
        return s
    else: 
        if s[-3:] == 'ing':
            return s + 'ly'
        else: return s + 'ing'
#     """
#     Given a string, if its length is at least 3, add 'ing' to its end.
#     Unless it already ends in 'ing', in which case add 'ly' instead.
#     If the string length is less than 3, leave it unchanged. Return
#     the resulting string.

#     >>> verbing('hail')
#     'hailing'
#     >>> verbing('swiming')
#     'swimingly'
#     >>> verbing('do')
#     'do'
#     """
    raise NotImplementedError


import re

def not_bad(s):
    return re.sub(r"not.*bad", "good", s)

#     >>> not_bad('This movie is not so bad')
#     'This movie is good'
#     >>> not_bad('This dinner is not that bad!')
#     'This dinner is good!'
#     >>> not_bad('This tea is not hot')
#     'This tea is not hot'
#     >>> not_bad("It's bad yet not")
#     "It's bad yet not"
#     """
    raise NotImplementedError


import math

def front_back(a, b):
    half = lambda a: math.ceil(len(a)/2)
    return a[:half(a)] + b[:half(b)] + a[half(a):] + b[half(b):]
#     """
#     Consider dividing a string into two halves. If the length is even,
#     the front and back halves are the same length. If the length is
#     odd, we'll say that the extra char goes in the front half. e.g.
#     'abcde', the front half is 'abc', the back half 'de'. Given 2
#     strings, a and b, return a string of the form a-front + b-front +
#     a-back + b-back

#     >>> front_back('abcd', 'xy')
#     'abxcdy'
#     >>> front_back('abcde', 'xyz')
#     'abcxydez'
#     >>> front_back('Kitten', 'Donut')
#     'KitDontenut'
#     """
