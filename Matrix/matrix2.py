import numpy as np

# matrix numpy
a = np.array([(1, 2), 
              (3, 4)])
b = np.ones([2, 2])

print("matrix a:")
print(a)
print("matrix b:")
print(b)

# perkalian matrix (panjang baris harus sama dengan panjang kolom untuk perkalian matrix)
c1 = np.dot(a, b) # jika tidak menggunakan np.dot menjadi perkalian array biasa
c2 = a.dot(b)
print("hasil perkalian:")
print(c1)
print(c2)


