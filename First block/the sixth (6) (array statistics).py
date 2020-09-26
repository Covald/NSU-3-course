import numpy as np
from scipy import stats

array = np.random.randint(0, 100, 10)

print(array)
print(f"min - {min(array)}, max - {max(array)} ")
print(f"average - {np.average(array)}")
print(f"std - {np.std(array)}")
print(f"xui - {stats.moment(array, 5)}")
