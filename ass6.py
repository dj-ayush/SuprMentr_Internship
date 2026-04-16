# NumPy Speed Test

import time
import numpy as np

# Create 1 million numbers
size = 1000000

# Python list
py_list = list(range(size))

start = time.time()
py_result = [x * 2 for x in py_list]
end = time.time()

print("Python list time:", end - start)

# NumPy array
np_array = np.arange(size)

start = time.time()
np_result = np_array * 2
end = time.time()

print("NumPy array time:", end - start)