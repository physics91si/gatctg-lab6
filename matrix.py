import numpy as np
import matplotlib.pyplot as plt

arr = np.zeros((9,9))

#arr - np.matrix('1 1 1 0 0 0 0 0 0; 1 1 1 0 0 0 0 0 0; 1 1 1 0 0 0 0 0 0; 1 1 1 0 0 0 0 0 0; 1 1 1 0 0 0 0 0 0; 1 1 1 0 0 0 0 0 0; 1 1 1 0 0 0 0 0 0; 1 1 1 0 0 0 0 0 0; 1 1 1 1 1 1 1 1 1')

ys = (0,0,0,0,0,0,0,0,0)
xs = (0, 1, 2, 3, 4, 5, 6, 7, 8)

arr[xs, ys] = 1

ys = (1,1,1,1,1,1,1,1,1)
xs = (0, 1, 2, 3, 4, 5, 6, 7, 8)

arr[xs, ys] = 1

ys = (2,2,2,2,2,2,2,2,2,8)
xs = (0, 1, 2, 3, 4, 5, 6, 7,8,8)

arr[xs, ys] = 1

xs = (4,7,1)
ys = (5,7,8)

arr[xs, ys] = 1

print(arr) 

plt.spy(arr)
plt.show()
