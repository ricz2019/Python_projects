# https://treyhunner.com/2018/04/keyword-arguments-in-python/#Keyword-only_arguments_without_positional_arguments

from math import sqrt

def quadratic(a, b, c):
    x1 = -b / (2*a)
    x2 = sqrt(b**2 - 4*a*c) / (2*a)
    return (x1 + x2), (x1 - x2)
x = quadratic(31, 93, 62)
y = quadratic(a=31, b=93, c=62)
z = quadratic(b=93, a=31, c=62)
print(x)
print(y)
print(z)
help(quadratic)

# When we use keyword arguments:

# We can often leave out arguments that have default values
# We can rearrange arguments in a way that makes them most readable
# We call arguments by their names to make it more clear what they represent
# GzipFile(filename=None, mode=None, compresslevel=9, fileobj=None, mtime=None)
# |      At least one of fileobj and filename must be given a
# |      non-trivial value.
from gzip import GzipFile
def write_gzip_file(output_file, contents):
    with GzipFile(None, 'wt', 9, output_file) as gzip_out:
        gzip_out.write(contents)

def write_gzip_file(output_file, contents):
    with GzipFile(fileobj=output_file, mode='wt', compresslevel=9) as gzip_out:
        gzip_out.write(contents)
# help(GzipFile)

# The itertools.zip_longest function also accepts an optional fillvalue 
# attribute (which defaults to None) exclusively as a keyword argument:

from itertools import zip_longest
x = list(zip_longest([1, 2], [7, 8, 9], [4, 5], fillvalue=0))
print(x)

# The built-in print function accepts the optional sep, end, file, 
# and flush attributes as keyword-only arguments:
print('comma', 'separated', 'words', sep=', ')


# Note: If you haven’t seen that * syntax before, *numbers captures all positional 
# arguments given to the product function into a tuple which the numbers variable points to.
def product(*numbers, initial=1):
    total = initial
    for n in numbers:
        total *= n
    return total
x1 = product(4,4)
x2 = product(4, 4, initial=1)
x3 = product(4, 5, 2, initial=3)

print(x1, x2, x3)


# That joiner variable doesn’t have a default value, so it must be specified:
def join(*iterables, joiner):
    if not iterables:
        return
    yield from iterables[0]
    for iterable in iterables[1:]:
        yield joiner
        yield from iterable

x1 = list(join([1, 2, 3], [4, 5], [6, 7], joiner='0'))
x2 = list(join([1, 2, 3], [4, 5], [6, 7], joiner='filler'))
x3 = list(join([1, 2, 3], [4, 5], [6, 7], joiner='$'))
print(x1 ,x2, x3)

test = [[1, 2, 3], [4], [6, 7], [3,9,1]]
x4 = list(join(*test, joiner='$'))
# [1, 2, 3, '$', 4, '$', 6, 7, '$', 3, 9, 1]
print(x4)

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
help(format_attributes)

# Just like with unlimited positional arguments, these keyword arguments can 
# be required. Here’s a function with four required keyword-only arguments:
from random import choice, shuffle
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = UPPERCASE.lower()
DIGITS = "0123456789"
ALL = UPPERCASE + LOWERCASE + DIGITS

def random_password(*, upper, lower, digits, length):
    chars = [
        *(choice(UPPERCASE) for _ in range(upper)),
        *(choice(LOWERCASE) for _ in range(lower)),
        *(choice(DIGITS) for _ in range(digits)),
        *(choice(ALL) for _ in range(length-upper-lower-digits)),
    ]
    shuffle(chars)
    return "".join(chars)
x1=random_password(upper=1, lower=1, digits=1, length=8)
x2=random_password(upper=1, lower=1, digits=1, length=8)
print(x1)
print(x2)

