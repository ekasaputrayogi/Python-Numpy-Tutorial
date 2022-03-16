import numpy as np

# membuat array matrix
e = np.array ([(1,2,3), (4,5,6)])

# matrix dengan nilai 0
f = np.zeros((5,4)) # matrix 0 5x4

# matrix dengan nilai 1
g = np.ones((3,3)) # matrix 1 3x3

# matrix identitas
h1 = np.identity((3)) # matrix identitas 3x3
h2 = np.eye(3) # matrix identitas 3x3

print("e: ",e)
print("f: ",f)
print("g: ",g)
print("h1: ",h1)
print("h2: ",h2)