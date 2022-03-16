import numpy as np

a = np.array ([
               (1, 2, 3),
               (4, 5, 6)
               ])

print("matrix a: ", a.shape)
print(a)

# transpos matrix
print ("transpos matrix dari a:")
print(a.transpose()) # atau
print(np.transpose(a)) # atau
print(a.T)

print("matrix a: ", a.shape)
print(a) # matrix a tidak berubah

# flatten vektor, vektor baris
print("flatten matrix a:")
print(a.ravel())

# reshape matrix
print("reshape matrix a:")
print(a.reshape(3,2))

# resize matrix
print("resize matrix a:")
a.resize(3,2)
print(a)
print("matrix a: ", a.shape)
print(a) # matrix a berubah