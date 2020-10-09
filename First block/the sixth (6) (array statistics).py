import numpy as np
from scipy import stats

array = np.random.randint(0, 101, 100)
#array = list(map(int, input().split()))
print(array)
print(f"min - {min(array)}, max - {max(array)} ")
print(f"average - {np.average(array)}")
print(f"std - {np.std(array)}")
print(f"Fifth central moment - {stats.moment(array, 5)}")
print(f"Среднее вышеуказанных чисел - {np.average(np.array([np.min(array), np.max(array), np.average(array), np.std(array), stats.moment(array, 5)]))}")
