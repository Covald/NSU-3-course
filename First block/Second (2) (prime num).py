import math
print([2] + [x for x in range(3, int(input("Input N - "))+1, 2)
             if all(x % i for i in range(3, int(math.sqrt(x)) + 1, 2))])
