# Daily Learnings:

1)
```
testdata =[ ['9034968', 'ETH'], ['14160113', 'ETH'], ['9034968', 'ETH'], ['11111', 'NOT'], ['9555269', 'NOT'], ['15724032', 'ETH'], ['15481740', 'ETH'], ['15481757', 'ETH'], ['15481724', 'ETH'], ['10307528', 'ETH'], ['15481757', 'ETH'], ['15481724', 'ETH'], ['15481740', 'ETH'], ['15379365', 'ETH'], ['11111', 'NOT'], ['9555269', 'NOT'], ['15379365', 'ETH']
]
unique_data = [list(x) for x in set(tuple(x) for x in testdata)]
```
-----------------------------------------------------------------------------------------------------------------------------------
2)
```
array = [['a','b'], ['a', 'b','c'], ['a']]
output = ['a','b','c']

result = set(x for l in array for x in l)
```
-----------------------------------------------------------------------------------------------------------------------------------
3)Flatten list of lists:

Given a list of lists l,

flat_list = [item for sublist in l for item in sublist]

or 

import itertools
list2d = [[1,2,3],[4,5,6], [7], [8,9]]
merged = list(itertools.chain(*list2d))

Create list of lists:


Create your list before your loop, else it will be created every loop.
```
>>> list1 = []
>>> for i in range(10) :
...   list1.append( range(i,10) )
...
>>> list1
[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9], [3, 4, 5, 6, 7, 8, 9], [4, 5, 6, 7, 8, 9], [5, 6, 7, 8, 9], [6, 7, 8, 9], [7, 8, 9], [8, 9], [9]]

```

-----------------------------------------------------------------------------------------------------------------------------------
4)a="preeti"

p=list(a)

print(p)

['p','r','e','e','t','i']

-----------------------------------------------------------------------------------------------------------------------------------
A lot of times when dealing with iterators, we also get a need to keep a count of iterations

enumerate(iterable, start=0)

Parameters:
Iterable: any object that supports iteration
Start: the index value from which the counter is 
              to be started, by default it is 0 
```
>>> l1 = ["eat","sleep","repeat"]

>>> print(list(enumerate(l1)))
[(0, 'eat'), (1, 'sleep'), (2, 'repeat')]

>>> 
for ele in enumerate(l1): 
    print ele 

(0, 'eat')
(1, 'sleep')
(2, 'repeat')
```
-----------------------------------------------------------------------------------------------------------------------------------

Python — List Sorting, Keys & Lambdas: https://medium.com/@johngrant/python-list-sorting-keys-lambdas-1903b2a4c949

```
lst = [('candy','30','100'), ('apple','10','200'), ('baby','20','300')]

lst.sort(key=lambda x:x[1])

print(lst)

It will print as following:

[('apple', '10', '200'), ('baby', '20', '300'), ('candy', '30', '100')]
```
 sort() — A method that modifies the list in-place
 sorted() — A built-in function that builds a new sorted list from an iterable

In Python, anonymous function is a function that is defined without a name.

While normal functions are defined using the def keyword, in Python anonymous functions are defined using the lambda keyword.
Syntax of Lambda Function in python

lambda arguments: expression

Lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned. 

Lambda functions are used along with built-in functions like filter(), map() etc.

The filter() function in Python takes in a function and a list as arguments.

The function is called with all the items in the list and a new list is returned which contains items for which the function evaluats to True.
```
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)

[4, 6, 8, 12]
```
-----------------------------------------------------------------------------------------------------------------------------------

Convert all strings in a list to int


Use the map function (in Python 2.x):
```
results = map(int, results)

In Python 3, you will need to convert the result from map to a list:

results = list(map(int, results))
```


-----------------------------------------------------------------------------------------------------------------------------------

The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.This function is defined in “functools” module.

Working : 

    At first step, first two elements of sequence are picked and the result is obtained.
    Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
    This process continues till no more elements are left in the container.
    The final returned result is returned and printed on console.

```
from functools import reduce # only in Python 3

def do_sum(x1, x2): return x1 + x2

print(reduce(do_sum, [1, 2, 3, 4]))

This reduce()  call perform the following operation:

(((1 + 2) + 3) + 4) => 10
```

-----------------------------------------------------------------------------------------------------------------------------------
creating a dictionary of lists

defaultdict:

```
>>> from collections import defaultdict
>>> d = defaultdict(list)
>>> a = ['1', '2']
>>> for i in a:
...   for j in range(int(i), int(i) + 2):
...     d[j].append(i)
...
>>> d
defaultdict(<type 'list'>, {1: ['1'], 2: ['1', '2'], 3: ['2']})
>>> d.items()
[(1, ['1']), (2, ['1', '2']), (3, ['2'])]

```

-----------------------------------------------------------------------------------------------------------------------------------

To find index of particular value in list
```
def migratoryBirds(arr):
    bird_freq = [0, 0, 0, 0, 0, 0]
    for i in range(len(arr)):
        bird_freq[arr[i]] += 1
return bird_freq.index(max(bird_freq))
```

-----------------------------------------------------------------------------------------------------------------------------------
Any

Returns true if any of the items is True. It returns False if empty or all are false. Any can be thought of as a sequence of OR operations on the provided iterables.
It short circuit the execution i.e. stop the execution as soon as the result is known.

All

Returns true if all of the items are True (or if the iterable is empty). All can be thought of as a sequence of AND operations on the provided iterables. It also short circuit the execution i.e. stop the execution as soon as the result is known.

-----------------------------------------------------------------------------------------------------------------------------------
How do I initialize a dictionary of empty lists in Python?
```
p={i:[] for i in 'abcdefghijklmnopqrstuvwxyz'}

data = {k: [] for k in range(2)}

from collections import defaultdict
data = defaultdict(list)

d = {k : v for k in blah blah blah}
```
-----------------------------------------------------------------------------------------------------------------------------------
Create list of tuples in list:
```>>> x = [1, 2, 3]
>>> y = [4, 5, 6]
>>> zipped = zip(x, y)
>>> zipped
[(1, 4), (2, 5), (3, 6)]
```
In Python 3:
```
z = list(zip(x,y))
```
In Python 2:
```
z = zip(x,y)
```
-----------------------------------------------------------------------------------------------------------------------------------
To take 2-3 integer inputs in single in python:

```
a,b=map(int, raw_input().split())
```
-----------------------------------------------------------------------------------------------------------------------------------
Exponential notation in python:

let's see with examples:
```
10e9+7 -------------10000000009+7
```
number in exponential form is float by default,to use it as integer we need to typecast it.

-----------------------------------------------------------------------------------------------------------------------------------
from collections import deque
deque.pop()----pop from right
deque.popleft()----pop from left
deque.append()-----push from right
deque.appendleft()--push form left side

-----------------------------------------------------------------------------------------------------------------------------------







    


