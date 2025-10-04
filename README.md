# PCD-Splitting-Image

Program Pengolahan Citra Digital (PCD) untuk memisahkan channel warna RGB dan CMY dari gambar digital.

## 📋 Deskripsi Project

Aplikasi ini merupakan implementasi GUI menggunakan PyQt6 untuk melakukan operasi pengolahan citra digital, khususnya untuk:

-   Menyalin gambar asli
-   Memisahkan channel Red (R) dari gambar
-   Memisahkan channel Green (G) dari gambar
-   Memisahkan channel Blue (B) dari gambar
-   Memisahkan channel Cyan (C) dari gambar
-   Memisahkan channel Magenta (M) dari gambar
-   Memisahkan channel Yellow (Y) dari gambar

## 👥 Kelompok F

**Kelas:** Pengolahan Citra Digital - C

**Anggota:**

1. I Kadek Rai Pramana (2105551094)
2. Ni Putu Adnya Puspita Dewi (2105551099)
3. Gusti Ngurah Satya Bagus Partama (2105551100)
4. Dyah Putri Maheswari (2105551102)

## 🛠️ Teknologi yang Digunakan

-   **Python 3.x**
-   **PyQt6** - Framework GUI
-   **PIL (Python Imaging Library)** - Pengolahan gambar
-   **io** - Input/Output operations

## 📦 Instalasi

1. Clone repository ini:

```bash
git clone https://github.com/rai-pramana/PCD-Splitting-Image.git
cd PCD-Splitting-Image
```

2. Install dependencies yang diperlukan:

```bash
pip install PyQt6 Pillow
```

## 🚀 Cara Menjalankan

1. Jalankan file Python:

```bash
python "Tugas PCD C_Project Copy Gambar Kelompok F.py"
```

2. Interface aplikasi akan terbuka dengan berbagai tombol kontrol.

## 📖 Cara Penggunaan

1. **Pilih Gambar**: Klik tombol "Pilih Gambar" untuk memuat gambar dari komputer
2. **Proses Channel**: Pilih salah satu tombol berikut untuk memproses gambar:
    - **Proses R**: Menampilkan hanya channel Red
    - **Proses G**: Menampilkan hanya channel Green
    - **Proses B**: Menampilkan hanya channel Blue
    - **Proses C**: Menampilkan channel Cyan (Green + Blue)
    - **Proses M**: Menampilkan channel Magenta (Red + Blue)
    - **Proses Y**: Menampilkan channel Yellow (Red + Green)
    - **Copy**: Menyalin gambar asli
3. **Save Hasil**: Klik "Save Hasil Gambar" untuk menyimpan hasil pemrosesan

## ✨ Fitur Utama

-   **Interface GUI yang user-friendly** dengan PyQt6
-   **Preview gambar real-time** sebelum dan sesudah pemrosesan
-   **Support multiple format gambar** (JPG, PNG, JPEG)
-   **Resize otomatis** gambar untuk tampilan optimal
-   **Error handling** untuk input yang tidak valid
-   **Save functionality** untuk menyimpan hasil pemrosesan

## 🎯 Konsep PCD yang Diimplementasikan

### RGB Color Model

-   **Red Channel**: Memisahkan komponen merah dari gambar
-   **Green Channel**: Memisahkan komponen hijau dari gambar
-   **Blue Channel**: Memisahkan komponen biru dari gambar

### CMY Color Model

-   **Cyan (C)**: Kombinasi Green + Blue channels
-   **Magenta (M)**: Kombinasi Red + Blue channels
-   **Yellow (Y)**: Kombinasi Red + Green channels

## 📁 Struktur File

```
PCD-Splitting-Image/
├── README.md
├── Tugas PCD C_Project Copy Gambar Kelompok F.py
└── (gambar hasil akan disimpan di direktori yang dipilih user)
```

## 🔧 Fungsi Utama dalam Kode

-   `resize_image()`: Mengubah ukuran gambar untuk tampilan
-   `pixmap_from_cv_image()`: Konversi format gambar untuk Qt
-   `choose_source_image()`: Memilih gambar input
-   `process_image_*()`: Fungsi pemrosesan untuk setiap channel
-   `save_as_file()`: Menyimpan hasil pemrosesan

## 📝 Catatan

-   Aplikasi ini mendukung format gambar JPG, PNG, dan JPEG
-   Gambar akan di-resize otomatis untuk tampilan (max 800x500 pixels)
-   Pastikan file gambar yang dipilih valid dan dapat dibaca

## 🤝 Kontribusi

Project ini dibuat sebagai tugas mata kuliah Pengolahan Citra Digital. Kontribusi dan saran perbaikan sangat diterima.

## 📄 Lisensi

Project ini dibuat untuk tujuan akademik sebagai tugas kuliah.
