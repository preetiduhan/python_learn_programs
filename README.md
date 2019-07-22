# Daily Learnings:

1)testdata =[ ['9034968', 'ETH'], ['14160113', 'ETH'], ['9034968', 'ETH'], ['11111', 'NOT'], ['9555269', 'NOT'], ['15724032', 'ETH'], ['15481740', 'ETH'], ['15481757', 'ETH'], ['15481724', 'ETH'], ['10307528', 'ETH'], ['15481757', 'ETH'], ['15481724', 'ETH'], ['15481740', 'ETH'], ['15379365', 'ETH'], ['11111', 'NOT'], ['9555269', 'NOT'], ['15379365', 'ETH']
]
unique_data = [list(x) for x in set(tuple(x) for x in testdata)]

-----------------------------------------------------------------------------------------------------------------------------------
2)

array = [['a','b'], ['a', 'b','c'], ['a']]
output = ['a','b','c']

result = set(x for l in array for x in l)

-----------------------------------------------------------------------------------------------------------------------------------
3)Flatten list of lists:

Given a list of lists l,

flat_list = [item for sublist in l for item in sublist]

or 

import itertools
list2d = [[1,2,3],[4,5,6], [7], [8,9]]
merged = list(itertools.chain(*list2d))

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

>>> l1 = ["eat","sleep","repeat"]

>>> print(list(enumerate(l1)))
[(0, 'eat'), (1, 'sleep'), (2, 'repeat')]

>>> 
for ele in enumerate(l1): 
    print ele 

(0, 'eat')
(1, 'sleep')
(2, 'repeat')

-----------------------------------------------------------------------------------------------------------------------------------

Python — List Sorting, Keys & Lambdas: https://medium.com/@johngrant/python-list-sorting-keys-lambdas-1903b2a4c949

lst = [('candy','30','100'), ('apple','10','200'), ('baby','20','300')]

lst.sort(key=lambda x:x[1])

print(lst)

It will print as following:

[('apple', '10', '200'), ('baby', '20', '300'), ('candy', '30', '100')]

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

my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)

[4, 6, 8, 12]

-----------------------------------------------------------------------------------------------------------------------------------

 

-----------------------------------------------------------------------------------------------------------------------------------

    


