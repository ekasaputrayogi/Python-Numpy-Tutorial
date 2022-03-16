import numpy as np

a = np.array ([1, 2, 3, 4]) # array menggunakan numpy
b = [1, 2, 3, 4] # list tanpa menggunakan python

print("a: ",a)
print ("b: ",b)

a = a + 1 # seluruh komponen array pada numpy akan ditambah 1
b = b + [1] # python akan menambahkan angka 1 pada list terakhir

print("a: ",a)
print("b: ",b)