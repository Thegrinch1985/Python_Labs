"""
Lab_04
--------
1. Higher-Order Functions
   - Sample Programs: functional and higher order
2. Closure
   - Sample Programs: closure
2. Currying
"""


# In functional programming, a function is a first-class citizen of the language
# Which basically means a function is just another value - it is on par with any other object

def i_am_a_function( my_arg ) :
    return my_arg

i_am_a_function_by_another_name = i_am_a_function

print(i_am_a_function(10))
print(i_am_a_function)

print(i_am_a_function_by_another_name(11))
print(i_am_a_function_by_another_name)

# Since functions are just values, we can pass them as parameters
# Higher order functions, are functions which take a function as a parameter, or returns a function (or both)

print(i_am_a_function_by_another_name(i_am_a_function))



#########
# closure
#########

# Nested functions => functions that can be defined within the scope of another function
# A nested function has access to the environment in which it was defined
# you use inner functions to protect them from anything happening outside of the function (hidden from global scope)

def outer(a) :
    def inner(b) :  # hidden from outer code
        return b + 1
    return inner(a)

print( outer(10) )


# Therefore, can return an inner function that remembers the state of the outer function, even after the outer function has completed execution
# This is a closure
# A closure simply causes the inner function to remember the state of its environment when called.
# Beginners often think that a closure is the inner function, when it’s really caused by the inner function. The closure “closes” the local variable on the stack and this stays around after the the stack creation has finished executing.


def has_permission(page):  #factory function
    def inner(username):
        if username == 'Admin':
            return "'{0}' does have access to {1}.".format(username, page)
        else:
            return "'{0}' does NOT have access to {1}.".format(username, page)
    return inner


current_user = has_permission('Admin Area')
print(current_user('Admin')) # when ever you call the newly created current_user, it will always see it's own private snapshot that includes page=Admin Area

random_user = has_permission('Admin Area')
print(random_user('Not Admin'))

# A closure is a function’s scope that’s kept alive by a reference to that function.
# Closures work because the variables are immutable, i.e. they cannot change values from the time they were closed over to the time the returned function is called.




##########
# currying
##########

# A Curried Function is a function that only takes a single parameter at a time.
# Use higher-order functions to convert a function that takes multiple arguments into a chain of functions that each take a single argument.
# More specifically, given a function f(x, y), we can define a function g such that g(x)(y) is equivalent to f(x, y).
# Here, g is a higher-order function that takes in a single argument x and returns another function that takes in a single argument y. This transformation is called currying.

def curried_pow(x):
 def inner(y):
     return pow(x, y)
 return inner

print(curried_pow(2)(3))


