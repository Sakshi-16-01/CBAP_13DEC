#Topic: Frozen Sets
#-----------------------------
'''

The frozenset() function returns an immutable frozenset object 
initialized with elements from the given iterable. Frozen set 
is just an immutable version of a Python set object. 
While elements of a set can be modified at any time, 
elements of the frozen set remain the same after creation.
'''

fzs1 = frozenset([1, 2, 3])
fzs1
type(fzs1)

fzs2 = frozenset([2, 3, 4])
fzs2
b = set([2, 3, 4])

fzs2.add(b)

fzs1.union(fzs2) #all numbers

fzs1
fzs2
fzs1.intersection(fzs2)  #common


#Sets may only contain immutable (hashable) values, and thus may not contain other sets, in which case frozensets can be useful. Consider the following example:
a = set([1, 2, 3])
b = set([2, 3, 4])
a.add(b)
a.add(frozenset(b))
a
#--
# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')
fSet = frozenset(vowels)

st = set(vowels)

print('The frozen set is:', fSet)

#used in dictionary # random dictionary
person = {"name": "John", "age": 23, "sex": "male"}
fSet = frozenset(person)
print('The frozen set is:', fSet)
#Like normal sets, frozenset can also perform different operations like union, intersection, etc.
#links
#https://www.python-course.eu/python3_sets_frozensets.php
