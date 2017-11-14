#!/usr/bin/env python

# Write a Markov text generator, [markov.py](python/markov.py). Your program should be called from the command line with two arguments: the name of a file containing text to read, and the number of words to generate. For example, if `chains.txt` contains the short story by Frigyes Karinthy, we could run:

# ```bash
# ./markov.py chains.txt 40
# ```

# A possible output would be:

# > show himself once more than the universe and what I often catch myself playing our well-connected game went on. Our friend was absolutely correct: nobody from the group needed this way. We never been as the Earth has the network of eternity.

# There are design choices to make; feel free to experiment and shape the program as you see fit. Jeff Atwood's [Markov and You](http://blog.codinghorror.com/markov-and-you/) is a fun place to get started learning about what you're trying to make.

import random as r
import numpy as np

#function to generate word frequency dictionary looking back only 1 word

def gen_word_freq_1back(filename):
    with open(filename, 'r') as f:
        paragraphs = [p for p in f.readlines() if p != '\n']

    word_freq = {}

    raw_txt = [p.split(' ') for p in paragraphs]
    raw_txt = [w for p in raw_txt for w in p]

    #read input text and get create word frequency dictionary

    for i in range(len(raw_txt)-1):
        word_0 = raw_txt[i].lower()
        word_1 = raw_txt[i+1].lower()
        if word_0 not in word_freq.keys():
            word_freq[word_0] = {word_1:1}
        else: 
            if word_1 not in word_freq[word_0].keys():
                word_freq[word_0][word_1] = 1
            else:
                word_freq[word_0][word_1] = word_freq[word_0][word_1] + 1
   
    
    return word_freq

#function to generate word frequency dictionary looking back 2 words

def gen_word_freq_2back(filename):
    with open(filename, 'r') as f:
        paragraphs = [p for p in f.readlines() if p != '\n']

    word_freq = {}

    raw_txt = [p.split(' ') for p in paragraphs]
    raw_txt = [w for p in raw_txt for w in p]

    #read input text and get create word frequency dictionary

    for i in range(len(raw_txt)-2):
        word_0 = raw_txt[i].lower()
        word_1 = raw_txt[i+1].lower()
        word_2 = raw_txt[i+2].lower()
        prev_words_tup = word_0,word_1
        if prev_words_tup not in word_freq.keys():
            word_freq[prev_words_tup] = {word_2:1}
        else: 
            if word_2 not in word_freq[prev_words_tup].keys():
                word_freq[prev_words_tup][word_2] = 1
            else:
                word_freq[prev_words_tup][word_2] = word_freq[prev_words_tup][word_2] + 1
   
    
    return word_freq


#function to generate the next word given the current word
#Based on probability distribution indicated above

def gen_next_word_1back(word, word_freq):
    if word in word_freq.keys():
        d = word_freq[word]
        t = sum(d.values())
        word_list = list(map(list,d.items()))
        next_word = [w[0] for w in word_list]
        prob = [w[1]/t for w in word_list]
        return str(np.random.choice(next_word,1,prob)[0])
    
    #chose from a uniform distribution of all the unique words seen in the raw text
    #in the case that the previous word is missing from word_freq
    #this should only happen for the last word in a paragraph
    
    else: return str(np.random.choice(list(word_freq.keys()),1))

#word_freq = {w:paragraph_1.count(w) for w in paragraph_1}

def gen_next_word_2back(word_0,word_1, word_freq):
    word_tup = word_0,word_1
    if word_tup in word_freq.keys():
        d = word_freq[word_tup]
        t = sum(d.values())
        word_list = list(map(list,d.items()))
        next_word = [w[0] for w in word_list]
        prob = [w[1]/t for w in word_list]
        return str(np.random.choice(next_word,1,prob)[0])
    
    #chose from a uniform distribution of all the unique words seen in the raw text
    #in the case that the previous word is missing from word_freq
    #this should only happen for the last word in a paragraph
    
    else: return str(np.random.choice(list(word_freq.keys()[0]),1))
    
def gen_paragraph_1back(word_freq):
    
    rand_txt = [np.random.choice(list(word_freq.keys()),1)[0]]
    sentence_cnt = 0
    #for i in range(100):
    while True:
        #next_word = gen_next_word(rand_txt[i], word_freq)
        rand_txt = rand_txt + [gen_next_word_1back(rand_txt[-1],word_freq)]
        if rand_txt[-1][-1] == '.':
            sentence_cnt += 1
        if sentence_cnt > 5:
            break
    return ' '.join(rand_txt)

def gen_paragraph_2back(word_freq):
    
    tup_list = list(word_freq.keys())
    str_list = list(map(' '.join, tup_list))
    rand_txt = np.random.choice(str_list,1)[0].split(' ')
    sentence_cnt = 0
    
    while True:
        rand_txt = rand_txt + [gen_next_word_2back(rand_txt[-2],rand_txt[-1],word_freq)]
        if rand_txt[-1][-1] == '.':
            sentence_cnt += 1
        if sentence_cnt > 5:
            break
    return ' '.join(rand_txt)
    
