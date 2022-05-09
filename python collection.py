# A Python program to show different
# ways to create Counter
from collections import Counter,OrderedDict,ChainMap,namedtuple,deque
import timeit


# With sequence of items
#print(Counter(['B','B','A','B','C','A','B',
		#	'B','A','C']))

# with dictionary
#print(Counter({'A':3, 'B':5, 'C':2}))

# with keyword arguments
#print(Counter(A=3, B=5, C=2))
'''senbon = Counter(['a','c','f','h'])
print(senbon)
'''

# A Python program to demonstrate working
# of OrderedDict

'''print("This is a Dict:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for key, value in d.items():
	print(key, value)

print("\nThis is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
	print(key, value)
'''

# A Python program to demonstrate working
# of OrderedDict

'''od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

print('Before Deleting')
for key, value in od.items():
    print(key, value)

# deleting element
od.pop('a')

# Re-inserting the same
od['a'] = 1

print('\nAfter re-inserting')
for key, value in od.items():
    print(key, value)

d={}
d['byakuya'] = 'senbonsakura'
d['ichigo'] = 'getsugatensho'
d['abarai renji'] = 'rugit zabimaru'


print('Normal dict before deleting')

for i,j in d.items():
    print(i,j)


d.pop('byakuya')

d['byakuya' ] = 'mouf'

print('\n Normal dict afer deleting')
for i,j in d.items():
    print(i,j)'''

# Python program to demonstrate
# ChainMap
'''d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Defining the chainmap
c = ChainMap(d1, d2, d3)

print(c.maps)
print(list(c.keys()))'''


# Python code to demonstrate namedtuple()

# Declaring namedtuple()
'''Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)
'''

# Python code to demonstrate deque




# Declaring deque
queue = deque(['name', 'age', 'DOB'])

c = ['name', 'age', 'DOB']

print(queue)

b=timeit

c.pop(0)

a = timeit-bdbprint(a)

d = timeit

queue.pop(0)

e = timeit-d
print(e)


