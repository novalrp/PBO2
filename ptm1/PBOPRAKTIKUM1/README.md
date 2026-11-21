# Praktikum PBO 1 - Pertemuan 1
## GUI Dasar Python + Flask

Project ini digunakan untuk belajar:
- Class dan Object
- Attribute dan Method
- Flask route
- Form/request
- Jinja2 template
- Static CSS

## STRUKTUR FOLDER (PENTING)

Setelah ZIP diekstrak, struktur harus seperti ini:

```text
Project_PBO_TI350_Pertemuan_1_GUI_Dasar/
├── app.py
├── requirements.txt
├── run.bat
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

**Jangan memindahkan `index.html` keluar dari folder `templates`.**
Folder `templates` harus berada satu tingkat dengan `app.py`.

## Cara menjalankan di Windows DISARANKAN MENGGUNAKAN GIT BASH

### 1. Buka folder project
Di VS Code pilih folder yang berisi file `app.py`.

### 2. Buat virtual environment

```powershell
python -m venv .venv
```

### 3. Aktifkan virtual environment

```powershell
.venv\Scripts\activate
```

Jika PowerShell memblokir aktivasi, gunakan Command Prompt atau jalankan:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

lalu:

```powershell
.venv\Scripts\activate
```

### 4. Install Flask

```powershell
pip install -r requirements.txt
```

### 5. Jalankan aplikasi

```powershell
python app.py
```

### 6. Buka browser

```text
http://127.0.0.1:5000/
```

## Cara menggunakan aplikasi

1. Isi NIM.
2. Isi Nama.
3. Isi Program Studi.
4. Klik **Simpan Data**.
5. Data tampil pada tabel.
6. Klik **Hapus** untuk menghapus data.

## Catatan pembelajaran

Data masih disimpan di memory, belum menggunakan database. Saat program dihentikan, data tambahan akan kembali ke kondisi awal.

## Jika muncul TemplateNotFound

Jika muncul:

```text
jinja2.exceptions.TemplateNotFound: index.html
```

periksa bahwa:

```text
app.py
templates/
└── index.html
```

berada pada folder project yang sama.

Jangan sampai menjadi:

```text
app.py
mnt/
└── data/
    └── .../
        └── templates/
            └── index.html
```

