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

# Tugas 3

## 1. Penjelasan Kanal R, G, dan B

Model warna RGB terdiri dari tiga kanal warna, yaitu:

- **R (Red)** merupakan kanal yang menyimpan intensitas warna merah.
- **G (Green)** merupakan kanal yang menyimpan intensitas warna hijau.
- **B (Blue)** merupakan kanal yang menyimpan intensitas warna biru.

Setiap piksel pada gambar digital direpresentasikan oleh tiga nilai tersebut. Masing-masing kanal memiliki rentang nilai **0–255**, di mana:

- 0 menunjukkan tidak ada intensitas warna.
- 255 menunjukkan intensitas warna maksimum.

Sebagai contoh:

```python
[120, 80, 200]
```

Artinya:

- R = 120
- G = 80
- B = 200

Kombinasi ketiga nilai tersebut menghasilkan satu warna tertentu pada sebuah piksel. Seluruh gambar merupakan kumpulan jutaan piksel yang masing-masing memiliki nilai RGB.

---

## 2. Mengapa Menggunakan Model RGB?

Model RGB digunakan karena merupakan model warna standar pada perangkat digital seperti monitor, laptop, kamera digital, dan smartphone. Library Pillow (PIL) secara default membaca gambar berwarna dalam mode RGB sehingga setiap piksel memiliki tiga komponen warna, yaitu Red, Green, dan Blue.

Penggunaan model RGB memberikan beberapa keuntungan, yaitu:

- sesuai dengan standar tampilan pada perangkat digital;
- mudah direpresentasikan dalam bentuk array tiga dimensi menggunakan NumPy;
- memudahkan proses pengolahan citra seperti membaca nilai piksel, segmentasi, filtering, deteksi objek, serta analisis warna;
- didukung oleh berbagai library pengolahan citra, seperti Pillow dan OpenCV.

Karena setiap piksel terdiri dari tiga kanal warna, gambar dapat dikonversi menjadi array tiga dimensi menggunakan:

```python
array_gambar = np.array(gambar)
```

Hasil konversi memiliki bentuk:

```python
(465, 620, 3)
```

yang berarti:

- 465 = tinggi gambar (piksel)
- 620 = lebar gambar (piksel)
- 3 = jumlah kanal warna (Red, Green, Blue)

---

## 3. Apakah Ada Alternatif Selain RGB?

Ya. Selain RGB terdapat beberapa model warna lain yang digunakan sesuai kebutuhan, antara lain:

### a. Grayscale
Model ini hanya memiliki satu kanal intensitas (tingkat keabuan), sehingga ukuran data lebih kecil dan sering digunakan pada pengolahan citra dasar.

### b. HSV (Hue, Saturation, Value)
Model HSV memisahkan informasi warna, tingkat kejenuhan, dan kecerahan sehingga lebih mudah digunakan untuk proses segmentasi atau pendeteksian objek berdasarkan warna.

### c. CMYK (Cyan, Magenta, Yellow, Key/Black)
Model warna ini digunakan pada dunia percetakan karena lebih sesuai dengan proses pencampuran tinta.

### d. YCbCr
Model ini memisahkan informasi luminansi (kecerahan) dan krominansi (warna), sehingga banyak digunakan pada kompresi gambar dan video, seperti format JPEG dan MPEG.

Meskipun terdapat berbagai model warna lain, RGB tetap menjadi model yang paling umum digunakan dalam pengolahan citra digital karena sesuai dengan cara perangkat digital menampilkan warna dan didukung oleh banyak library pemrograman.

---

## Kesimpulan

Model RGB terdiri dari tiga kanal warna, yaitu Red, Green, dan Blue. Setiap piksel pada gambar memiliki tiga nilai intensitas yang membentuk warna tertentu. Model RGB dipilih karena merupakan standar pada perangkat digital dan memudahkan proses pengolahan citra menggunakan library seperti Pillow dan NumPy. Selain RGB, terdapat model warna lain seperti Grayscale, HSV, CMYK, dan YCbCr yang digunakan sesuai dengan kebutuhan pengolahan gambar.
