"""

Lab_01

1. Introduction / Overview
2. Types: int, float, str, bool, tuple(mutable)
   - Samples Programs: types strings, tuples
3. Controls (if/loops)
   - Samples Programs: control
4. Functions (Pure)
   - Sample Programs: functions (functional)
5. Iteration v's Recursive

"""


#one line
"""
mulit line
"""

##########
# variables

#immutable types - stateless, values cannot be changed
intNum = 10
floatNum = 1.5
string = "string"
bool1 = True
tuple1 = (1,2,3,5,6,7,5,4) #finite list

print( type(intNum), type(floatNum ), type(string), type(bool1), sep='****' )

#can set one type to another (dynamic typing)
string = intNum

#list mutable - has [] instead of tuples ()
list1 = [1,2,3,4,5,7]

#Can have tuples/lists with different type
tuple2 = (1, "string", 4)


##########
#display
x = 'sample string'
print("This is a string" + str(x), end='\n', sep='*****')
print("This is a string ", x )
print("This is a string {0}".format(x))


##########
#input
name = input("Please enter your name:")
age = int(input("Please enter your age:"))


print(name.__contains__("Ka"))


##########
#if statements

if age > 17 and age < 65 :
    print("Adult")
elif age == 17 :
    print ("student")
else :
    print("child")

	
##########
#loops (remember loops are not part of functional programming!

for c in name :
    print(c)

for num in range(1, 11) :
    print(num)


for num in range(1, 11, 2) :  #increment = 2
    print(num)

myList = [11, 22, 33, 44, 55, 6, 7, 8, 9]
for index, item in enumerate(myList) :
    print( index, item, sep='****')


##########
#functions
def print_list( l ) :
    for a in l:
        print(a)
    return    #Functional programming functions must return something! They can only act on input deep copy

print_list( [1,2,3,4,5,6,7] ) 



#iterate  - don't iterate in functional programming, you use recursive function calls

x = 0
for a in range(1,11):
    x = x + a   #x+=a
print(x)   #55


# versus recursive
def sumRange(start, end, acc):
    if start > end :
        return acc
    return sumRange( start+1, end, acc + start )


print( sumRange( 1, 10, 0 ) )  #55