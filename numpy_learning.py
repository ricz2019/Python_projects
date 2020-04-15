import numpy as np

arr = np.arange(24).reshape(2, 3, 4)
print(arr)
print(type(arr))
print(arr.shape)
print(arr.ndim)

np.random.seed(444)
x = np.random.choice([False, True], size=100000)
print(len(x))
print(x)

def count_transitions(x) -> int:
	count = 0
	for i, j in zip(x[:-1], x[1:]):
		if j and not i:
			count += 1
	return count

#print(count_transitions.__annotations__['x'])

print(count_transitions(x))

np.count_nonzero(x[:-1] < x[1:])

"""from timeit import timeit
setup = 'from __main__ import count_transitions, x; import numpy as np'
num = 1000
t1 = timeit('count_transitions(x)', setup=setup, number=num)
t2 = timeit('np.count_nonzero(x[:-1] < x[1:])', setup=setup, number=num)
print('Speed difference: {:0.1f}x'.format(t1 / t2))

n = 10
t3 = timeit(f'x = [i**2 for i in range({n})]')
t4 = timeit(f'x = np.arange({n})**2', setup='import numpy as np')
print('Speed difference: {:0.1f}x'.format(t3 / t4))
"""


a = np.array([(1,2,3,4),(3,4,5,6)])
for x in range(len(a[0])):
	print(a[:,x])

a=np.linspace(1,3,10)
print(a)

a=np.array([(1,2,3),(3,4,5,)])
print(np.sqrt(a))
print(np.std(a))
print(a.sum(axis=0))

import matplotlib.pyplot as plt
x= np.arange(0,3*np.pi,0.1)
y=np.sin(x)
plt.plot(x,y)
plt.show()