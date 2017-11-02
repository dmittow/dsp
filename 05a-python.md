# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and tuples are both sequential and ordered data structures which contain multiple items of any data type. Lists have variable lenght and support operations such as insert, delete, append, and extend. Tuples are immutable, meaning they have a fixed length and for the most part do not support updates. The only slight exception to this is in the case of a tuple made of lists, in which the component lists can be modified but not the tuple itself.

>>Tuples can be used as keys in a dictionary while lists cannot. This is mostly because of the mutability of lists. Dictionaries are constructed by hashing the key of an item, and then inserting the key:value pair at the address indicated by the hash function. Since lists can be updated, calculating a consistent hash value is almost impossible. Any updates to the values in a list used as keys would change the hash value, and therefore change the place where the (key,value) pair would need to be stored. Since tuples stay constant once initialized, the hash values also stay content and thus they are a good candidate for use as a key in a dictionary.

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists are ordered, and allow duplicates while sets do not. Sets are best for operations like 'IN', 'MINUS', and 'XOR'.
```python
foods_i_like = {'cheese','chocolate','cookies','lobster'}

def do_i_like(s, foods):
    like = 'no'
    if s in foods:
        like = 'yes'
    return like
    
>>>do_i_like('cheese',foods_i_like)
yes
>>>do_i_like('mushrooms', foods_i_like)
no
```    
>>Adding items to sets is fast, and so is checking membership. Finding the index of an element in a SET is meaningless since the values are not ordered. 

>>Finding the index of a value in a list takes linear time, since you have to iterate through the items in a list checking equality until you find the desired value. They are best used when the order of values is important. For example, strings are internally treated like lists of characters
```python
>>>x = 'computer'
>>>x[2]
m
```

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda is a keyword that can help simplify the code for defining a function. Instead of using the keywords *def* and *return*, the same functionality can be accomplished with one line.

```python
mx = lambda x,y: x if x>y else y
>>>mx(3,5)
5
```
>>Here is an example of code to sort a list of drinks by the length of their names:

```python
>>>drinks = ['coffee','lemonade','wine','beer','tea']
>>>print(sorted(drinks, key=lambda s:len(s)))
['tea', 'wine', 'beer', 'coffee', 'lemonade']
```
---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a shorthand way of applying simple operations to all the items in a list, and which returns another list as a result.

```python
>>>menu = ['wine','lemonade','orange juice','water']
>>>prefs = [do_i_like(d,drinks) for d in menu]
>>>print(prefs)
['yes', 'yes', 'no', 'no']
```
>>Here is the same function implemented using *map*

```python
>>>print(list(map(do_i_like, menu, 4*[drinks_i_like])))
['yes', 'yes', 'no', 'no']
```

>>Here is an example of filtering implemented with list comprehension

```python
print([d for d in menu if (d in drinks_i_like)])
```
>>Here is the same thing using the filtering keyword
```python
print(list(filter(lambda d: d in drinks_i_like, menu)))
```
>>Here is an example of a dictionary comprehension
```python
food_menu = ['cheese','chocolate','cookies','lobster']
drink_menu = ['wine','water','milk','lemonade']
drink_recs = {f: d for (f,d) in zip(food_menu,drink_menu)}
print(drink_recs)

{'cheese': 'wine', 'chocolate': 'water', 'cookies': 'milk', 'lobster': 'lemonade'}
```
>>Here is an example of a set comprehension
```python
good_drinks = {d for d in drink_menu if d in drinks_i_like}
print(good_drinks)
```

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

```python
import numpy  
import pandas  
from datetime import datetime as dt  
from dateutil.parser import parse  
  
date_start = '01-02-2013'      
date_stop = '07-28-2015'  

diff = dt.date(dt.strptime(date_stop, '%m-%d-%Y')) - dt.date(dt.strptime(date_start, '%m-%d-%Y'))  
print(diff)  
```

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  (answer will be in number of days)

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)





