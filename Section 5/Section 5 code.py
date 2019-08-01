print("")
print("Lets talk about: if, elif & else")
print("")

print("In python control flow syntax makes use of colons and indentation (whitespace).")
print("This indentation system is crucial to Python and is what sets it apart from other programming languages")
print("")

# Syntax of an if/else statement

"""
if some_condition:
    # execute some code
else:
    # do something else
"""

# Syntax of an if/else statement with multiple other conditions

"""
if some_condition:
    # execute some code
elif some_other_condition:
    # do something else
else:
    # do something else
"""

x = 2
if x == 2:
    print("It is True that x == 2")
else:
    print("It is False that x == 2")

print("")
print("Lets talk about: For Loops")
print("")
# Syntax of a for loop

"""
my_iterable = [1,2,3]
for item_name in my_iterable
    print(item_name)
    
Output
>>1
>>2
>>3
"""

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(mylist)
print("")

print("This is running a for loop printing ")
for num in mylist:
    print(num)

print("")
for num in mylist:
    # Check for even
    if num % 2 == 0:
        print(f"Even Number = {num}")
    else:
        print(f"Odd Number = {num}")
print("")

list_sum = 0

# This will add all the numbers in index order from mylist
for i in mylist:
    list_sum = list_sum + i
    print(list_sum)
print("")
print(list_sum)

print("")
mystr = 'Hello World'
# This will print every letting in mystring since it is a string
for i in mystr:
    print(i)
print("")
print(mystr)

tup = (1, 2, 3)
print("")
for item in tup:
    print(item)
print(tup)
print("")

mylist = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(mylist)

for i in mylist:
    print(i)
print("")

# This is tuple unpacking: using two temp variables
for (a, b) in mylist:
    print(a)
    print(b)
print("")

# This is the same algorithm as above, without ()
for a, b in mylist:
    print(a)
    print(b)
print("")

mylist = [(1, 2, 3), (5, 6, 7), (8, 9, 10)]
print(mylist)

for x, y, z in mylist:
    print(x)
    print(y)
    print(z)
print("")

# This is a dictionary
d = {'k1': 1, 'k2': 2, 'k3': 3}
print(d)

# When running a loop, printing dictionary you'll only get the keys and not there values
for i in d:
    print(i)
print("")

# To get the items from a dictionary you have to use variable.items command
for i in d.items():
    print(i)
print("")

# You can use the same temp variable as tuple unpacking for dictionary as long as you use variable.items command
for key, value in d.items():
    print(key)
    print(value)
print("")

print("")
print("Lets talk about: While Loops")
print("")
print("While loops will continue to execute a block of code while some condition is remain True.")
print("")

print("Syntax of a while loop")
print("while some_boolean_condition:")
print("     do something")
print("else:")
print("     do something different")
print("")
print("Be vary careful as this could result in infinite loop.")
print("")

x = 0
while x < 5:
    print(f"The current value of x = {x}")
    x = x + 1
else:
    print(f"X is not < than 5, x = {x}")
    # You could also use "x +=1" instead of x = x + 1
print("")

print("")
print("Lets talk about: break, continue, pass")
print("")

print("break: Breaks out of the current closest enclosing loop.")
print("continue: Goes to the top of the closest enclosing loop.")
print("pass: Does nothing at all.")
print("")

print("Lets start with pass")
print("Pass can be used to create a place holder to go back to without causing error. (See code")
print("")
# if the bellow code did not have the pass in the loop, it would have cause an error.
x = [1, 2, 3]
for i in x:
    # comment
    pass

print("Continue in a loop")
# continue is comparable to a skip
mystr = "sammy"
print(mystr)
print("Run loop with continue over a")

for i in mystr:
    if i == 'a':
        continue
    print(i)
print("")

print("Break in for loop")
# break stops the loop you are in
mystr = "sammy"
print(mystr)
print("Run loop with break over a")

for i in mystr:
    if i == 'a':
        break
    print(i)
print("")


print("break in while loop")
x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
print("")

print("")
print("Lets talk about: Useful Operators")
print("")

print("Range Operator")
print("Range syntax = range(start, stop, step size)")
print("For Example:")
print("")
print("for i in range(10, 0, -1):")
print("    print(i)")
print("")
print("This will print the count down of 10 - 0")
for i in range(10, 0, -1):
    print(i)
print("")


print("If you want create a list using the range operator use the list()")
print('This is called a "Generator"')
print("The below is an example of a generator (See code on how to make it)")
print("")

x = list(range(10, 0, -1))
print(x)
print("")

print("Enumerate")
print("")

print("For Example: Without Enumerate")
print("index_count = 0")
print('word = "abcde"')
print("for i in word:")
print('    print(f"At index {index_count} the letter is {i}")')
print("    index_count += 1")
print("Output is the below")

index_count = 0
word = "abcde"
for i in word:
    print(f"At index {index_count} the letter is {i}")
    index_count += 1

print("Enumerate will not need a index_variable/counter")
print("")
print("For Example: With enumerate")
print("for i in enumerate(word):")
print("    print(i)")
print("")
print("Output is the below")

for i in enumerate(word):
    print(i)
print("")

print("This enumerate operator will provide tuples with both the item and the index with less code.")
print("Since this is a tuple, you can unpack it.\n")
print("For Example: Tuple unpacking\n")
print("for index, letter in enumerate(word):")
print("    print(index)")
print("    print(letter)")
print("    print('')")
print("Output is the below\n")

for index, letter in enumerate(word):
    print(index)
    print(f"{letter}\n")
print("")

print("Zip")
print("")
print("Zip will merge list [] together")
print("For Example: Zip\n")
print("my_list1 = [1, 2, 3]")
print('my_list2 = ["a", "b", "c"]')
print("")
print("for i in zip(my_list1, my_list2):")
print("    print(i)\n")
print("Output is the below\n")
my_list1 = [1, 2, 3]
my_list2 = ["a", "b", "c"]

for i in zip(my_list1, my_list2):
    print(i)

print("")
print("If you were to zip and print the zip, it'll only give you memory location: See below for example")
x = zip(my_list1, my_list2)
print(f"{x}\n")

print("In order to get zip in a list, you have to surround zip() with list(): See below for example")
print('x = list(zip(my_list1, my_list2))')
print("Output is the below")

x = list(zip(my_list1, my_list2))
print(f"{x}\n")

print("If the lists are not the len(), it would only pair up to minimum len() of the list (No Error will be provided)")
print("")

print("To quickly check if something (x), you can use the below code")
print("")
print("print('x' in ['x', 'y', 'z'])")
print("Output is the below:\n")
print('x' in ['x', 'y', 'z'])
print("")

print("Minimum & Maximum")
print("Min and max is very simple to figure out, just use min() and max()")
print("For Example: Min & Max\n")

mylist1 = [1, 2, 3, 4, 5]
x = min(mylist1)
y = max(mylist1)

print("mylist1 = [1, 2, 3, 4, 5]")
print("x = min(mylist1)")
print("y = max(mylist1)")
print("print(x,y)\n")
print("Output is the below:\n")
print(f'The minimum = {x}')
print(f'The maximum = {y}')
print("")

print("Random")
print("To randimize x,y,z. You have to import random and specify the type of random")
print("Syntax Import = from Library import module: See below for random shuffle")
print("from random import shuffle\n")
print("For Example: Random Shuffle\n")

from random import shuffle
mylist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = shuffle(mylist1)

print("mylist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]")
print("x = shuffle(mylist1)\n")
print("Output is the below:")
print(mylist1)
print("")

from random import randint
x = randint(0,100)
print(x)


result = input("Can you type")
print(result)


"""

print("")
print("Lets talk about: ")
print("")


"""