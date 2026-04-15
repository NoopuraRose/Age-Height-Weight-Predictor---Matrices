import numpy as np 

x = np.array([
    [1,18,150],
    [1,20,160],
    [1,22,165],
    [1,25,170],
    [1,28,175],
    [1,30,180]
])

y = np.array([
    [45],
    [50],
    [55],
    [65],
    [70],
    [75]
])

theta = np.linalg.inv((x.T) @ x) @ (x.T @ y)

print(theta)