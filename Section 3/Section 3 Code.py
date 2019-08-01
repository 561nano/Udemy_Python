x = 7 / 4
print(x)
x = 7 // 4  # Floor Division, floor means = truncates the decimal without rounding, and returns an integer result.
print(x)

x = 7 % 4  # Returns the remainder of division
print(f"The remainder of 7/3 is {x}")

x = 2 ** 3  # ** = to the power (2^3)
print(f"2 to the power of 3 = {x}")

x = 100 ** 0.5 # number ** 0.5 = square root
print(x)

# Matrix are like arrays
# They consist of sever list stacked

x = [1, 2, 3]
y = [5, 1, 5]
z = [3, 2, 9]

matrix1 = [x, y, z]
print(f"This is a matrix {matrix1}")
print("")

print(f"This is how to inVision a matrix!\n{x}\n{y}\n{z}\n")

# Build a list comprehension by deconstructing a for loop within a []
first_col = [row[0] for row in matrix1]

print(first_col)

# Strings in python are immutable: cannot be changed once declared.

x = (0, 1, 2, 3)  # Tuple, immutable: cannot be changed once declared.
y = [0, 1, 2, 3]  # List, they are not immutable (they can change) List are like arrays with can hold at the same time (str, int, etc)
z = {0: "This is that", 1: "What am i doing", 2: "Lets see", 3: "Please work"}  # Dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
zz = {0, 1, 2, 3}  # set is an unordered collection data type that is iterable, mutable, and has no duplicate elements.

print(type(x), type(y), type(z), type(zz))

print("Hello World")

# \n prints to the next line
print("Hello \nWorld")

# \t tab --->
print("Hello \tWorld")

# len() provides the length of a string
print(len("Hello World"))

mystring = "Hello World"
print(mystring)

print('I wrote %s programs today.' % 3.75)  # %s formats to string
print('I wrote %d programs today.' % 3.75)  # %d formats to integer without rounding
print('Floating point numbers: %5.2f' % (
    13.149))  # Floating point numbers use the format %5.2f. Here, 5 would be the minimum number of characters the string should contain; these may be padded with whitespace if the entire number does not have this many digits. Next to this, .2f stands for how many numbers to show past the decimal point.

# Slice
print(mystring[0])

print(mystring[-1])

myst = "abcdefghijk"
print(myst[2:])
print(myst[:3])
print(myst[3:6])
print(myst[1:3])
print(myst[::2])
print(myst[1::3])
print(myst[::-1])  # To reverse a string

name = "Sam"
name = "P" + name[1:] + " "
print(name)
print(name * 10)

print(name.upper())
print(name.lower())

x = "Hi this is a string"
print(x.split())
print(x.split("i"))

# .format() method
# String here {} then also {}'.format('something1', 'something2')

print("This is a string {}".format("Inserted"))
print("The {2}{1}{0}".format("Fox.", "Brown ", "Quick "))
print("The {q}{b}{f}".format(f='fox.', b="brown ", q="quick "))

result = 100 / 777
print("The result was {} ".format(result))
print("The result was {r} ".format(r=result))
print("The result was {r:1.3f} ".format(r=result))
print("The result was {r:1.5f} ".format(r=result))

name = "Christian"
age = 24
print(
    "Hello, his name is {} and is {} years old".format(name, age))  # old way of doing it in python (String formatting)
print(f"Hello, his name is {name} and is {age} years old")  # new way of doing it in python (String formatting)

my_list = [1, 2, 3]
print(my_list)

my_list = ["String", 100, 23.1]
print(my_list)

print(len(my_list))

my_list = ["One", "Two", "Three"]
print(my_list)

print(my_list[0])
print(my_list[1:])

list2 = ["Four", "Five"]

print(my_list + list2)
mewlist = my_list + list2

mewlist[0] = "ONE ALL CAPS"
print(mewlist)

mewlist.append("Six")  # Append adds an item to a list
mewlist.append("Seven")
print(mewlist)

mewlist.pop()  # Pop removes the last item in the list if you do not defined the index, if index is defined you'll remove that item from the list
print(mewlist)
pop_item = mewlist.pop()
print(mewlist)
print(pop_item)

print(mewlist.pop(0))  # This presents what is being removed and next time it is called it will be removed
print(mewlist)
print("")

new_list = ['a', 'e', 'x', 'b', 'c', ]
num_list = ['4', '1', '8', '3']

print(new_list)
print(num_list)
print("")

new_list.sort()  # This sorts the list A - Z
num_list.sort()  # This sorts the list 1 - 100...

print(new_list)
print(num_list)

new_list.reverse()  # This reverse the list Z - A
num_list.reverse()  # This reverse the list 100 - 1...

print(new_list)
print(num_list)
print("")

# Dict are objects retrieved by key name, unordered and can not be sorted
# List are objects retrieved by location, Ordered sequence can be indexed or sliced
print("Lets talk about Dict")
my_dict = {"key1": "Value1", "key2": "Value2", "key3": "Value3"}
print(my_dict)
print(my_dict["key1"])

price_lookup = {"apple": 2.99, "Orange": 1.29, "Milk": 5.89}
x = price_lookup["Milk"]
print(
    f"The price of milk is ${x}")  # you cannot lookup a dict in a print(f" the price of milk is ${price_lookup["Milk"]}")

d = {"k1": 123, "k2": [0, 1, 2], "k3": {"insidekey1": 100, "insidekey2": 200}}
print(d["k3"]["insidekey2"])  # This is grabbing a dict in a dict

e = {"k1": ["a", "b", "c"]}
print(e["k1"][2].upper())  # Grabs the ditc 'e' index of 2 and makes it upper case

e["k3"] = "d"  # This added a 'Key' to dict e
print(e["k3"])

e["k1"] = "REPLACED VALUE"  # This replace a value in dict 'e'
print(e)

print(d.keys())  # Prints all keys in dict 'd'
print(d.values())  # Prints all values in dict 'd'
print(d.items())  # Prints all items in dict 'd'
print("")

print("Lets talk about Tuaple")
t = (1, 1, 2, 3)  # Tuaple are immutable and cannot change, they are great for data integrity
print(t)
print(t.count(1))  # count the number of times '1' is in the tuple
print(t.index(1))  # returns the first index (position) '1' found in the tuple

# t[0] = "New"     This statement is trying to change the tuple, but it will spit out an error
print("")

# sets is only concerned with unique elements! We can cast a list with multiple repeat elements to a set to get the
# unique elements sets look like dict without keys
print("Lets talk about set()")
x = set()
x.add(1)  # add to set with the add() method
print(x)
x.add(2)
print(x)
x.add(3)
print(x)
x.add(2)  # This is already in the set and will not add it to set
print(x)

list1 = [1, 1, 2, 2, 3, 4, 5, 6, 1, 1]
print(set(list1))
print(len(set(list1)))  # Prints the length of set of list1
print("")

print("Lets talk about Booleans")
# Booleans must be capitalized
x = 1 > 2  # False
y = 1 < 2  # True
print(f"{x} is the statement that 1>2")
print(f"{y} is the statement that 1<2")
print("")

print("Lets talk about txt files")

# This is opening the document called myfile.txt that is in the same directory as this file
myfile = open("myfile.txt")
# Alternative way ro open file or in a different file path use
# print("C:\\Users\\chris\\OneDrive\\Documents\\Complete-Python-3-Bootcamp-master\\Section 3\\myfile.txt")

print("Successfully open myfile.text")
print("")

"""
For Windows you need to use double \ so python doesn't treat the second \ as an escape character, a file path is in the form:

myfile = open("C:\\Users\\YourUserName\\Home\\Folder\\myfile.txt")

For MacOS and Linux you use slashes in the opposite direction:

myfile = open("/Users/YouUserName/Folder/myfile.txt")

"""

# when you get [Errno 2] This is a common error code. They are two reason for this error
# Reason 1: Wrong File Name
# Reason 2: Didn't provide the correct file path

# This will provide a string of text from the txt file (The whole txt file will be read)
print(myfile.read())
print("")

# This will go back to the beginning of the document
myfile.seek(0)

# This will provide a list (The whole text file will be read)
print(myfile.readlines())
myfile.seek(0)
myfile.close()
print("")

# This will not need to variable.close()
with open("myfile.txt") as my_new_file:
    contents_of_txt_file = my_new_file.read()
    print(contents_of_txt_file)
    print("")

with open("myfile.txt") as my_new_file:
    contents_of_txt_file = my_new_file.readlines()
    print(contents_of_txt_file)
    print("")

# mode is = to the method of opening a document (This is a set of permissions)
# "r" = read
# "w" = write (This will over write files or create new!)
# "a" = append only (will add on to files)
# "r+" = read and write
# "w+" = is writting and reading (Overwrites existing files or creates a new file!)

with open("myfile.txt", mode="r") as myfile:
    contents_of_txt_file = myfile.read()
    print(contents_of_txt_file)
    print("")

# This will create a new file in the same directory
with open("a_new_txt_file_created_by_python.txt", mode="w+") as f:
    f.write("This was written by python.\nThis is really cool!")

# This will create a new file in the directory you point it to (in this example to desktop)
with open("C:\\Users\\chris\\Desktop\\a_new_txt_file_created_by_python.txt", mode="w+") as f:
    f.write("This was written by python.\nThis is really cool!")


# print("")

# print("Lets talk about ")

# print("")
