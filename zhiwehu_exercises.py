# https://github.com/zhiwehu/Python-programming-exercises/blob/master/100%2B%20Python%20challenging%20programming%20exercises.txt
# Question 1
# Level 1

# Question:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
x = [str(num) for num in range(2000, 3200+1) if (num % 7 == 0) and (num % 5 != 0)]

print(', '.join(x))

# Question 2
# Level 1

# Question:
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320
def fac(n):
	if n == 1:
		return 1
	return n*fac(n-1)

print(fac(8))

# Question 3
# Level 1

# Que#stion:
# With a given integral number n, write a program to generate a dictionary that 
# contains (i, i*i) such that is an integral number between 1 and n (both included). 
# and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
n = 8
x = {i: i*i for i in range(1, n+1)}
print(x)

# Question 4
# Level 1

# Question:
# Write a program which accepts a sequence of comma-separated numbers from 
# console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
xin = "34,67,55,33,12,98"#input("Enter your nubers: ")
res = xin.split(',')
res_tup = tuple(res)
print(res)
print(res_tup)

# Question 5
# Level 1

# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
class in_and_out:
	def __init__(self):
		self.s = ""

	def get_string(self):
		self.s = (input("Enter a string: "))

	def print_string(self):
		print(self.s.upper())

x = in_and_out()
#x.get_string()
x.print_string()

# Question 6
# Level 2

# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
C = 50
H = 30
D = "18,22,24"#input("Enter the numbers: ")

x = D.split(",")

for h in x:
	print(((2*C*int(h))/H)**.5)

# Question 7
# Level 2

# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

X,Y = 3,5

arr = [[i*j for j in range(Y)] for i in range(X)]
print(arr)
 
# Question 8
# Level 2

# Question:
# Write a program that accepts a comma separated sequence of words as 
# input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
words_in = "without,hello,bag,world"
x = words_in.split(',')
x.sort()
print(', '.join(x))

# Question 9
# Level 2

# Question£º
# Write a program that accepts sequence of lines as input and prints the lines 
# after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

sentences = ["Hello world", "Practice makes perfect"]
for x in sentences:
	print(x.upper())

# Question 10
# Level 2

# Question:
# Write a program that accepts a sequence of whitespace separated words as input and 
# prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
words_in = "hello world and practice makes perfect and hello world again"
x = words_in.split()
x = list(set(x))
x.sort()
print(' '.join(x))

# Question 11
# Level 2

# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers 
# as its input and then check whether they are divisible by 5 or not. The numbers that 
# are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.
nums_in = "0100,0011,0101,1010,1001,1100,1110,1111"
x = nums_in.split(',')
y = [int(i, base=2) for i in x if int(i, base=2)%5 == 0]
nums_out = []
for j in y :
	# nums_out.append(f"{j:b}".rjust(4, '0'))
	nums_out.append(f"{j:b}".zfill(4))
print(nums_out)

# Question 12
# Level 2

# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) 
# such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.
res = []
for x in range(1000, 3001):
	y = list(str(x))
	all_even = True
	for digit in y:
		if int(digit) % 2 != 0:
			all_even = False
			break
	if all_even:
		res.append(str(x))
print(','.join(res))

# Question 13
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

words_in ="hello world! 123"
counts = {"LETTERS": 0, "DIGITS": 0}
for x in list(words_in):
	if x.isalpha():
		counts["LETTERS"] += 1
	else:
		x.isnumeric()
		counts["DIGITS"] += 1

print(f"LETTERS {counts['LETTERS']}")
print(f"DIGITS {counts['DIGITS']}")

# Question 14
# Level 2

# Question:
# Write a program that accepts a sentence and calculate the number of 
# upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
words_in = "Hello World!"
d = {"UPPER CASE":0,"LOWER CASE":0}
for x in words_in:
	if x.isalnum():
		if x.isupper():
			d["UPPER CASE"] += 1
		else:
			d["LOWER CASE"] += 1
print(f"UPPER CASE {d['UPPER CASE']}")
print(f"LOWER CASE {d['LOWER CASE']}")

# Question 15
# Level 2

# Question:
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
digit_in = "9"
x_in = int(digit_in)

def n_digits(n,x):
	if n == 0:
		return x
	return n_digits(n-1, x)*10 + x

res = [n_digits(i, x_in) for i in range(4)]

print(sum(res))

# Question 16
# Level 2

# Question:
# Use a list comprehension to square each odd number in a list. 
# The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,3,5,7,9
nums_in = "1,2,3,4,5,6,7,8,9"
a = nums_in.split(",")
res = [x for x in a if int(x)%2 != 0]
print(','.join(res))

# Question 17
# Level 2

# Question:
# Write a program that computes the net amount of a bank account based a transaction 
# log from console input. The transaction log format is shown as following:
# D 100
# W 200

# D means deposit while W means withdrawal.
# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100
# Then, the output should be:
# 500
class account():
	def __init__(self, B = 0):
		self.balance =  B

	def make_D(self, D_amount):
		self.balance += D_amount

	def make_W(self, W_amount):
		self.balance -= W_amount

a = account()
a.make_D(300)
a.make_D(300)
a.make_W(200)
a.make_D(100)
print(a.balance)

# Question 18
# Level 3

# Question:
# A website requires the users to input username and password to register. 
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords 
# and will check them according to the above criteria. Passwords that match 
# the criteria are to be printed, each separated by a comma.
# Example
# If the following passwords are given as input to the program:
# ABd1234@1,a F1#,2w3E*,2We3345
# Then, the output of the program should be:
# ABd1234@1
import re

test = "ABd1234@1,a F1#,2w3E*,2We3345"

class passwd_validate():
	def __init__(self):
		self.max_pass = 12
		self.min_pass = 6
		self.passwd = ""

	def validate_pass(self, passwd):
		x = list(passwd)
		
		if len(x) >= self.min_pass and len(x) <= self.max_pass:
			if ( re.search("[A-Z]", passwd) and
				 re.search("[a-z]", passwd) and
				 re.search("[0-9]", passwd) and
				 re.search("[@#$]", passwd)):

				self.passwd = passwd
				return True
			else:
				return False	
		else:
			return False

test_str = test.split(",")
res = []
for pass_in in test_str:
	v = passwd_validate()
	if v.validate_pass(pass_in):
		res.append(v.passwd)

print(','.join(res))		

# Question 19
# Level 3

# Question:
# You are required to write a program to sort the (name, age, height) 
# tuples by ascending order where name is string, age and height are numbers. 
# The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), 
# ('Json', '21', '85'), ('Tom', '19', '80')]
from operator import itemgetter, attrgetter

list_in = ['Tom,19,80', 'Johnson,20,90','Jony,17,90','Jony,16,91','Json,21,85']
# list_in.sort()
res = []
for x in list_in:
	res.append(tuple(x.split(",")))
print(res)
test = sorted(res, key = itemgetter(0,1,2))

print(test)

# Question 20
# Level 3

# Question:
# Define a class with a generator which can iterate the numbers, 
# which are divisible by 7, between a given range 0 and n.

def putNumbers(n):
    for j in range(n+1):
        if j%7==0:
            yield j
x= []
for i in putNumbers(100):
	x.append(i)
print(x)

# Question 21
# Level 3

# Question£º
# A robot moves in a plane starting from the original point (0,0). The 
# robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The 
# trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# ¡­
# The numbers after the direction are steps. Please write a program to 
# compute the distance from current position after a sequence of movement 
# and original point. If the distance is a float, then just print the nearest integer.
# Example:
# If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2
import math
class cordinates:
	def __init__(self,xx,yy):
		self.x = xx
		self.y = yy
	def up(self,n):
		self.y += n
	def down(self,n):
		self.y -= n
	def left(self,n):
		self.x -= n
	def right(self,n):
		self.x += n
a=cordinates(0,0)
moves_in = ["UP 5","DOWN 3","LEFT 3","RIGHT 2"]
for moves in moves_in:
	m = moves.split()
	if   m[0]=="UP":
		a.up(int(m[1]))
	elif m[0]=="DOWN":
		a.down(int(m[1]))
	elif m[0]=="LEFT":
		a.left(int(m[1]))
	elif m[0]=="RIGHT":
		a.right(int(m[1]))
distance = round(math.sqrt((a.x)**2+(a.y)**2))
print(a.x, a.y, distance)

# Question 22
# Level 3

# Question:
# Write a program to compute the frequency of the words from the input. 
# The output should output after sorting the key alphanumerically. 
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be:
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1
words = "1 1 New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."
res = sorted(words.split(),key=str.lower)
freq = dict()

for x in res:
	if x not in freq:
		freq.update({x : 1})
	else:
		freq[x] += 1

for key,value in freq.items():
	print(key, ":", value)

# Question 23
# level 1

# Question:
#     Write a method which can calculate square value of number
def squares(x):
	"""Return a number which is the square value of 

	the input number
	"""
	return x**2
for i in range(5):
	print(squares(i))

# Question 24
# Level 1

# Question:
#     Python has many built-in functions, and if you do not know how 
#     to use it, you can read document online or find some books. But 
#     Python has a built-in document function for every built-in functions.
#     Please write a program to print some Python built-in functions 
#     documents, such as abs(), int(), raw_input()
#     And add document for your own function
def display_docstring(x):
	print(x.__doc__)
display_docstring(int())
print("\t",abs.__doc__)
print("\t\t",input.__doc__)
print(squares.__doc__)

# Question 25
# Level 1

# Question:
#     Define a class, which have a class parameter and have a same instance parameter.
class person:
	name = "person"
	def __init__(self, name=None):
		self.name = name
Richard = person("Richard")
print(person.name, Richard.name)
Kevin = person()
Kevin.name = "Kevin"
print(person.name, Kevin.name)

# Question:

# Write a program to solve a classic ancient Chinese puzzle: 
# We count 35 heads and 94 legs among the chickens and rabbits in 
# a farm. How many rabbits and how many chickens do we have?
total_heads = 35
total_legs = 94
def solve(heads,legs):
	for chickens in range(1,heads+1):
		rabbits = heads - chickens
		if 2*chickens+4*rabbits == legs:
			return chickens,rabbits
	return 0
res = solve(total_heads,total_legs)
print(res)


# Question:

# Please write a program which prints all permutations of [1,2,3]
def permutations(n):
	if n ==1:
		return 1
	return n*permutations(n-1)
lst1 = [1,2,3]
for i in lst1:
	print(permutations(i))


l1 = [1,2,3]
l2 = []
for v in l1:
    l2.insert(0,v)
print(l2)

def fun(x):
    global y
    y = x * x
    return y
    
fun(2)
print(y)

def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return
    
# Question:

# Please write a program which count and print the numbers of each character in a string input by console.

# Example:
# If the following string is given as input to the program:

# abcdefgabc

# Then, the output of the program should be:

# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1
str_in = "abcdefgabc"
s = list(str_in)
res = {}
for x in s:
	# if x not in res:
	# 	res.update({x:1})
	# else:
	# 	res[x] +=1

	res[x]= res.get(x,0)+1

for y in res.items():
	print(y[0],',',y[1])

# Question:

# Define a class Person and its two child classes: Male and Female. All 
# classes have a method "getGender" which can print "Male" for Male class and 
# "Female" for Female class.
class Person:
	def __init__(self):
		pass
	def get_gender(self):
		pass
class Male(Person):
	def __init__(self):
		pass
	def get_gender(self):
		print("Male")
class Female(Person):
	def __init__(self):
		pass
	def get_gender(self):
		print("Female")

a=Male()
a.get_gender()
b= Female()
b.get_gender()

# Question:

# By using list comprehension, please write a program to print 
# the list after removing the value 24 in [12,24,35,24,88,120,155].

# Hints:
# Use list's remove method to delete a value.

x = [12,24,35,24,88,120,155]
y = [i for i in x if i != 24]
print(y)

# Question:

# By using list comprehension, please write a program to print the 
# list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
x = [12,24,35,70,88,120,155]
for y in enumerate(x):
	print(y)
x = [x for (i,x) in enumerate(x) if i not in (0,4,5)]
# x = x[1:4]+x[6:]
print(x)

# By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.
x = [[[0 for col in range(8)] for row in range(5)] for k in range(3)]
print(x)

# By using list comprehension, please write a program to print the list 
# after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
x = [12,24,35,70,88,120,155]
x = [x for (i,x) in enumerate(x) if i not in (0,2,4,6)]
print(x)

# By using list comprehension, please write a program to print the list after 
# removing delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
a = [12,24,35,70,88,120,155]
b = [n for n in a if n%5 != 0 and n%7 != 0]
print(b)

# Please write a program to generate all sentences where subject 
# is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].
subjects = ["I", "You"]
verbs    = ["Play", "Love"]
objects  = ["Hockey","Football"]

res = []
for x in subjects:
	for y in verbs:
		for z in objects:
			res.append(x+' '+y+' '+z)
print(res)

from timeit import Timer
t = Timer("for i in range(100):1+1")
# print(t.timeit())


# import zlib
# s = 'hello world!hello world!hello world!hello world!'
# t = zlib.compress(s)
# # print(t)
# print(zlib.decompress(t))
import random
print("all random stuff below: ")
# Please generate a random float where the value is between 10 and 100 using Python math module.
print(random.random()*100)
# Please generate a random float where the value is between 5 and 95 using Python math module.
print(random.random()*100-5)
# Please write a program to output a random even number between 0 and 10 inclusive 
# using random module and list comprehension.
print(random.choice([i for i in range(11) if i%2==0]))
# Please write a program to output a random number, which is divisible 
# by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.
print(random.choices([i for i in range(201) if i%5==0 and i%7==0]))
# Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
print(random.sample(range(100), 5))
# Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
print(random.sample([i for i in range(100,201) if i%2==0], 5))
# Please write a program to randomly generate a list with 5 numbers, which are 
# divisible by 5 and 7 , between 1 and 1000 inclusive.
print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5))
# Please write a program to randomly print a integer number between 7 and 15 inclusive.
print(random.randrange(7,16))
# Please write a program to shuffle and print the list [3,6,7,8].
from random import shuffle
li = [3,6,7,8]
shuffle(li)
print( li)

# Note that while initial has a default value, you can also specify 
# required keyword-only arguments using this syntax:
def join(*iterables, joiner):
    if not iterables:
        return
    yield from iterables[0]
    for iterable in iterables[1:]:
        yield joiner
        yield from iterable

x = list(join([1, 2, 3], [4, 5], [6, 7], joiner=0))
print(x)

# Python allows functions to capture any keyword arguments provided
#  to them using the ** operator when defining the function:

def format_attributes(**attributes):
    """Return a string of comma-separated key-value pairs."""
    return ", ".join(
        f"{param}: {value}"
        for param, value in attributes.items()
    )

x = format_attributes(name="Trey", website="http://treyhunner.com", color="purple")
print(x)

items = {'name': "Trey", 'website': "http://treyhunner.com", 'color': "purple"}
x=format_attributes(**items)
print(x)
