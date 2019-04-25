"""
Lab_03
--------
1. Review
   - Lab_01, Lab_02
2. List Comprehension
   - Sample Programs: comprehensions
"""

# Expression oriented functions of Python provides are map, reduce, filter: and list comprehensions
# Python's way of implementing a notation for sets (as used my mathematicians)


# List comprehensions are a powerful alternative (complete substitute) to lambda, filter, map and reduce - more concise
# Basically a filter (which is optional) followed by a map


# Used as a way to define and create lists (dics, and sets) in Python - allows sequences to be built from other sequences
# Note: list comprehensions are the de-facto standard in python for iteration 


def capitalize_all(t) :
	res = []
	for s in t :
		res.append(s.capitalize())
	return res

print( capitalize_all("my name is karen") )


#can write this more concisely using list comprehensions
def capitalize_all_2(t) :
	return [s.capitalize() for s in t]
       
print( capitalize_all_2("my name is karen") )


#can also be optionaly used for filtering as well
def only_upper(t) :
       return [s for s in t if s.isupper()]

print(only_upper("My Name Is Karen"))   #['M', 'N', 'I', 'K']


"""
Breakdown of parts:

1. Bracket operators indicate we are constructing a new list
2. a_list => an input sequence
3. e => a Variable representing members of the input sequence
4. e**2 => an Output Expression producing elements of the output list from members of the Input Sequence (that satisfy the predicate)
5. if isinstance(e, int) => an Optional Predicate expression => your filter
"""

a_list = [1, '4', 9, 'a', 0, 4]

sqr_ints = [ e**2 for e in a_list if isinstance(e, int) ]  #if type(e) is int

print(sqr_ints)  # [ 1, 81, 0, 16 ]


# Using map and filter
print( list( map(lambda e: e**2, filter(lambda e: isinstance(e, int), a_list)) ) )
# two calls to lambda => expensive
# Also the input sequence is traversed through twice and an intermediate list is produced by filter



"""
Set Comprehensions
"""
names = [ 'Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'J', 'Bob' ]
setComp = { name[0].upper() + name[1:].lower() for name in names if len(name) > 1 }  #{ 'Bob', 'John', 'Alice' }
print( setComp )


"""
Dictionary Comprehensions
"""
mcase = {'a':10, 'b': 34, 'A': 7, 'Z':3}
mcase_frequency = { k.lower() : mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0) for k in mcase.keys() }
print(mcase_frequency)   # {'a': 17, 'b': 34, 'z': 3}


