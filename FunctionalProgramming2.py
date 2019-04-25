"""
Lab_02
--------
1. Lists - Keeps order, simply list of values
   - Sample Programs: lists1, list2
2. Dictionaries - Not ordered, associates key with every value
   - Sample Programs: dictionaries
3. Map
   - Sample Programs: map
4. Filter
   - Sample Programs: filter
5. Reduce
   - Sample Programs: reduce
"""

       
# Functional programming is all about expressions
# An expression-oriented programming language is a programming language where every (or nearly every) construction is an expression and thus yields a value.

"""
Expression oriented functions of Python provides are:

1. map(aFunction, aSequence)
2. filter(aFunction, aSequence)
3. reduce(aFunction, aSequence)
4. lambda
5. list comprehension (covered next lab)
"""

#####
# map
#####
# common things we do with list and other sequences is applying an operation to each item and collect the result
items = [1,2,3,4,5]
sqd = []
for x in items:
     sqd.append(x ** 2)

print(sqd)  #[1, 4, 9, 16, 25]

# So the map(aFunction, aSequence) function applies a passed-in function to each item in an iterable object and returns an iterator (prev list) containing all the function call results.
# Basically equivalent to for loop (faster)

def sqr(x) :
    return x ** 2

sqd = list(map(sqr, items))   # The function is applied to each item in the list, collected and returns values (as a iterator)
print (sqd)  #[1, 4, 9, 16, 25]


########
# lamdba
########
# The lambda operator or lambda function is a way to create small anonymous functions, i.e. functions without a name.
# These functions are throw-away functions, i.e. they are just needed where they have been created
# Lambda functions are mainly used in combination with the functions filter(), map() and reduce()
# syntax: "lambda argument_list: expression"
           # argument_list => comma separated list
           # expression => arithmethic expression using these arguments
sum = lambda x, y : x + y  
print(sum(2,3))  #5


################
# More Maps.....
################
# Because map expects a function, lambda routinely appears (as we don't need to define a function)

sqd = list(map((lambda x: x ** 2), items))
print (sqd)  #[1, 4, 9, 16, 25]


# Map can be applied to more than one list
# If you pass in 3 lists, your function must have 3 parameters
# Python3 will only iterate length of shortest list (if lists are different lengths)
items_2 = [1,2,3,4,5]
sqd = list(map((lambda x, y: x ** 2 + y ** 2), items, items_2))   # expects N-argument function of N sequences 
print (sqd)  #[2, 8, 18, 32, 50]


# While we still use lamda as a aFunction, we can have a list of functions as aSequence 
def cube(x):
    return (x**3)

funcs = [sqr, cube]

value = list( map(lambda x: x(10), funcs) )    #same as -> value = list( map(lambda x: x(10), [sqr, cube]) )
print(value)   # [100, 1000]

for r in range(5):
    value = list( map(lambda x: x(r), funcs) )
    print(value)
"""
[0, 0]
[1, 1]
[4, 8]
[9, 27]
[16, 64]
"""


########
# filter 
########
# filter(aFunction, aSequence)
# filter extracts each element in the sequence for which the function returns True
# selects some of the elements, and filters out the rest (based on the function)

# for loop way
fil_list = []
for x in range(-5, 5):
    if x < 0:
        fil_list.append(x)
print( fil_list)  #[-5, -4, -3, -2, -1]


# using filter
fil_list = list( filter( (lambda x: x < 0), range(-5,5) ) )
print( fil_list )  #[-5, -4, -3, -2, -1]




########
# reduce 
########
from functools import reduce

# reduce(aFunction, aSequence)
# returns a single value, by combining the items and returning a single value
# At each step, reduce passes the current result/return, along with the next item from the list, to the passed-in function (walks through the items)
# By default, the first item in the sequence initialized the starting value.


# for loop way
result = items[0]
for x in items[1:] :
    result = result * x
print(result)  #[120]


# using reduce
def product(x,y):
    return x * y
result = reduce(product, [1,2,3,4,5])
print(result)  #[120]


# using reduce and lambda
result = reduce( (lambda x, y: x * y), [1, 2, 3, 4,5])
print(result)  #[120]

# def reduce(function, iterable, initializer=None):
# reduce also allows an optional third argument placed at end to serve as an initialiser and default result when the sequence is empty.
result = reduce( (lambda x, y: x * y), [1, 2, 3, 4,5], 1)
print(result)  #[120]
