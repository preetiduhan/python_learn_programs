# Daily Learnings:

1)testdata =[ ['9034968', 'ETH'], ['14160113', 'ETH'], ['9034968', 'ETH'], ['11111', 'NOT'], ['9555269', 'NOT'], ['15724032', 'ETH'], ['15481740', 'ETH'], ['15481757', 'ETH'], ['15481724', 'ETH'], ['10307528', 'ETH'], ['15481757', 'ETH'], ['15481724', 'ETH'], ['15481740', 'ETH'], ['15379365', 'ETH'], ['11111', 'NOT'], ['9555269', 'NOT'], ['15379365', 'ETH']
]
unique_data = [list(x) for x in set(tuple(x) for x in testdata)]

2)

array = [['a','b'], ['a', 'b','c'], ['a']]
output = ['a','b','c']

result = set(x for l in array for x in l)

3)Flatten list of lists:

Given a list of lists l,

flat_list = [item for sublist in l for item in sublist]

or 

>>> import itertools
>>> list2d = [[1,2,3],[4,5,6], [7], [8,9]]
>>> merged = list(itertools.chain(*list2d))

4)

