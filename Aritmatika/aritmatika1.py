import numpy as np

# list tanpa numpy
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

# numpy array
anp = np.array([1, 2, 3, 4])
bnp = np.array([5, 6, 7, 8])

# penjumlahan
hasil = a + b # isi list digabungkan
hasilnp = anp + bnp # setiap komponen array dijumlahkan

# pengurangan
hasilnp = anp - bnp

# perkalian
hasilnp = anp * bnp

# pembagian
hasilnp = anp / bnp

# kuadrat
hasilnp = anp**2

print("hasil: ",hasil)
print("hasilnp: ",hasilnp)