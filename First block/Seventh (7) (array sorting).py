import random

import numpy
import string


def buildblock(size):
    return ''.join(random.choice(string.ascii_letters) for i in range(size))


array_int = numpy.random.randint(0, 101, 10)

array_complex = numpy.array([complex(random.random() * 100, random.random() * 100) for i in range(10)])
array_string = [buildblock(random.randint(1, 10)) for i in range(10)]
tuple_string = tuple(array_string)
print(f"Array of int {array_int}")
print(f"Sorted array_int by increase - {sorted(array_int)}")
print(f"Array of int {array_complex}")
print(f"Sorted by abs - {sorted(array_complex, key=abs)}")
print(f"Sorted by real part - {sorted(array_complex, key=lambda x: x.real)}")
print(f"list of string - {array_string}")
print(f"Sorted by length - {sorted(array_string, key=len)}")
print(f"tuple of string - {tuple_string}")
print(f"sorted by lekcika - {sorted(tuple_string)}")
print(f"Sorted by len - {sorted(tuple_string, key=len)}")
