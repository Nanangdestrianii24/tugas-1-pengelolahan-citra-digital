# Tugas 1 - Konversi Gambar ke Array 3 Dimensi

## Nama
Waode Nanang Destriani

## Deskripsi
Program Python untuk mengonversi gambar menjadi array 3 dimensi menggunakan library Pillow dan NumPy.

## Cara Menjalankan

Install library:

```bash
pip install numpy pillow
```

Jalankan program:

```bash
python konversi_gambar.py
```

Program akan menampilkan:
- Ukuran gambar
- Jumlah dimensi
- Bentuk array
- Tipe data
- Array RGB 3 dimensi

# Tugas 2

## 1. Fungsi `Image.open()` pada kelas `PIL.Image`

```python
from PIL import Image

gambar = Image.open("GUNUNG.jpg")
```

`Image.open("GUNUNG.jpg")` adalah fungsi dari library Pillow (PIL) yang digunakan untuk membuka atau membaca file gambar bernama **GUNUNG.jpg**. Hasil dari fungsi tersebut disimpan ke dalam variabel `gambar` sebagai objek bertipe `PIL.Image.Image`.

Objek ini menyimpan informasi gambar, seperti ukuran gambar, mode warna (RGB), format gambar, dan data piksel. Dengan fungsi ini, gambar dapat dibaca sehingga siap diproses lebih lanjut.

---

## 2. Mengapa harus menggunakan `np.array()`? Mengapa tidak menggunakan kelas `PIL.Image` saja?

```python
import numpy as np

array_gambar = np.array(gambar)
```

Objek yang dihasilkan oleh `Image.open()` masih bertipe `PIL.Image.Image`. Objek tersebut dapat digunakan untuk membuka, menampilkan, atau menyimpan gambar, tetapi belum berbentuk array numerik yang mudah diolah.

Fungsi `np.array()` digunakan untuk mengubah objek gambar menjadi array NumPy tiga dimensi yang berisi nilai RGB setiap piksel.

Contoh bentuk array hasil konversi:

```python
(465, 620, 3)
```

Keterangan:
- **465** = tinggi gambar
- **620** = lebar gambar
- **3** = kanal warna RGB (Red, Green, Blue)

Dengan mengubah gambar menjadi array NumPy, data piksel dapat diproses menggunakan berbagai operasi pengolahan citra, seperti perhitungan nilai piksel, filtering, segmentasi, dan analisis gambar.

### Kesimpulan

- `Image.open()` digunakan untuk membuka atau membaca file gambar.
- `np.array()` digunakan untuk mengubah objek gambar menjadi array 3 dimensi sehingga data piksel dapat diproses menggunakan NumPy.
