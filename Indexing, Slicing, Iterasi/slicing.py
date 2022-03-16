import numpy as np

# array dengan 10 index
a = np.arange(10)**2
print("a: ", a)
# slicing
print("elemen dari 1-6: ", a[0:6]) # start - end
print("elemen 4 sampai akhir", a[3:])
print( "elemen dari awal sampi ke 4", a[:4])
