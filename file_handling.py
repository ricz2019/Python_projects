#Convert a number to a string, the content of which depends on the number's factors.

import os

#my_dir = "C:\\Users\\Kevin\\Documents\\Python Scripts"
#
#def print_directory_contents(s_path):
#	
#	subdirs_in_path = (entry for entry in os.scandir(s_path))
#
#	for item in subdirs_in_path:
#		if item.is_dir():
#			print(f"The child directory is: {item.name}")
#			print_directory_contents(os.path.join(s_path, item))
#		else:
#			print('\t' + item.name)
#	
#	for i in range(10):
#		print(i)	
#
#
#print_directory_contents(my_dir) 

def f(x,l=[]):
	
	print(l, id(l))
	for i in range(x):
		l.append(i*i)
	print(l, id(l))
f(2)
f(3,[3,2,1])
f(3)	

def f(*args,**kwargs): print(args, kwargs)
l = [1,2,3]
t = (4,5,6)
d = {'a':7,'b':8,'c':9}
f()
f(1,2,3) # (1, 2, 3) {}
f(1,2,3,"groovy") # (1, 2, 3, 'groovy') {}
f(a=1,b=2,c=3) # () {'a': 1, 'c': 3, 'b': 2}
f(a=1,b=2,c=3,zzz="hi") # () {'a': 1, 'c': 3, 'b': 2, 'zzz': 'hi'}
f(1,2,3,a=1,b=2,c=3) # (1, 2, 3) {'a': 1, 'c': 3, 'b': 2}
f(*l,**d) # (1, 2, 3) {'a': 7, 'c': 9, 'b': 8}
f(*t,**d) # (4, 5, 6) {'a': 7, 'c': 9, 'b': 8}
f(1,2,*t) # (1, 2, 4, 5, 6) {}
f(q="winning",**d) # () {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
f(1,2,*t,q="winning",**d) # (1, 2, 4, 5, 6) {'a': 7, 'q': 'winning', 'c': 9,


class A(object):
	def go(self):
		print("go A go!")
	def stop(self):
		print("stop A stop!")
	def pause(self):
		raise Exception("Not Implemented")
class B(A):
	def go(self):
		super(B, self).go()
		print("go B go!")
class C(A):
	def go(self):
		super(C, self).go()
		print("go C go!")
	def stop(self):
		super(C, self).stop()
		print("stop C stop!")
class D(B,C):
	def go(self):
		super(D, self).go()
		print("go D go!")
	def stop(self):
		super(D, self).stop()
		print("stop D stop!")
	def pause(self):
		print("wait D wait!")
class E(B,C): pass

a=A()
b=B()
c=C()
d=D()
e=E()

a.go()
b.go()
c.go()
d.go()
e.go()
a.stop()
b.stop()
c.stop()
d.stop()
e.stop()

import array as arr
My_Array=arr.array('i',[1,2,3,4])
My_list=[1,'abc',1.20]
print(My_Array)
print(My_list)

import random
for _ in range(10):
	x = random.randrange(2, 20)
	print(x)
for _ in range(10):
	y = random.uniform(2, 20)
	print(y)
a = 'e'
b = 'r'
print(a is b)
print(a is not b)


#Bubble sort
a=[32,5,3,6,7,54,87]
def bs(a):
	for x in range(len(a)-1):
		for y in range(len(a)-1 - x):
			if a[y] > a[y+1]:
				a[y], a[y+1] = a[y+1], a[y]
	return a 

print(bs(a))

my_dir = "C:\\Users\\Kevin\\Documents\\Python Scripts"

def print_directory_contents(s_path):
	
	subdirs_in_path = (entry for entry in os.scandir(s_path))

	for item in subdirs_in_path:
		if item.is_dir():
			print(f"The child directory is: {item.name}")
			print_directory_contents(os.path.join(s_path, item))
		else:
			print('\t' + item.name)


print_directory_contents(my_dir) 

print()

import glob
glob.glob(".*.txt")

for dirpath, dirnames, files in os.walk('.'):
    print(f'Found directory: {dirpath}    {dirnames}')
    for file_name in files:
        print(file_name)
