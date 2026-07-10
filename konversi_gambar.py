from PIL import Image
import numpy as np

# Membaca gambar
gambar = Image.open("GUNUNG.jpg")

# Mengubah gambar menjadi array 3 dimensi
array_gambar = np.array(gambar)

# Menampilkan informasi gambar
print("Ukuran gambar :", gambar.size)
print("Jumlah dimensi :", array_gambar.ndim)
print("Bentuk array :", array_gambar.shape)
print("Tipe data :", array_gambar.dtype)

# Menampilkan isi array
print("\nArray 3 Dimensi:")
print(array_gambar)