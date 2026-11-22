"""Data profil untuk halaman portofolio.

Ganti isi PROFIL dengan data Anda sendiri. Seluruh halaman ikut berubah
karena template hanya membaca data dari sini.
"""

PROFIL = {
    'nama': 'Noval Rizky Pratama',
    'inisial': 'NRP',
    'peran': ['Web Developer', 'Python Enthusiast', 'UI Tinkerer'],  # teks mesin ketik
    'tagline': 'Membangun aplikasi web yang rapi, cepat, dan nyaman dipakai.',
    'tentang': [
        'Saya mahasiswa Teknik Informatika yang senang mengubah ide menjadi aplikasi web yang benar-benar dipakai. Fokus saya ada di Python, Flask, dan antarmuka yang bersih.',
        'Di luar kelas, saya mengerjakan proyek kecil, aktif di komunitas belajar, dan membiasakan diri menulis kode yang mudah dibaca orang lain.',
    ],
    'info': [
        ('Lokasi', 'Indonesia'),
        ('Email', 'noval@example.com'),
        ('Status', 'Terbuka untuk magang dan proyek'),
    ],
    'email': 'noval@example.com',
    'statistik': [
        {'angka': 12, 'label': 'Proyek selesai'},
        {'angka': 3, 'label': 'Tahun belajar'},
        {'angka': 8, 'label': 'Sertifikat'},
        {'angka': 5, 'label': 'Kolaborasi tim'},
    ],
    'skill': [
        {'nama': 'Python', 'nilai': 90},
        {'nama': 'Flask', 'nilai': 85},
        {'nama': 'HTML dan CSS', 'nilai': 88},
        {'nama': 'JavaScript', 'nilai': 72},
        {'nama': 'SQL', 'nilai': 70},
        {'nama': 'Git', 'nilai': 78},
    ],
    'teknologi': ['Python', 'Flask', 'Jinja2', 'HTML', 'CSS', 'JavaScript', 'SQLite', 'Git'],
    'proyek': [
        {'judul': 'Kalkulator Hub', 'deskripsi': 'Aplikasi web berisi kalkulator operator, simulasi cicilan, dan BMI.',
         'tag': 'Web', 'ikon': '//', 'hue': 232, 'tautan': '#'},
        {'judul': 'Dashboard Nilai', 'deskripsi': 'Visualisasi nilai kelas lengkap dengan grafik dan ringkasan statistik.',
         'tag': 'Data', 'ikon': 'Σ', 'hue': 14, 'tautan': '#'},
        {'judul': 'Katalog UMKM', 'deskripsi': 'Etalase produk usaha kecil dengan pencarian dan halaman detail.',
         'tag': 'Web', 'ikon': '</>', 'hue': 160, 'tautan': '#'},
        {'judul': 'Pengingat Belajar', 'deskripsi': 'Aplikasi web progresif untuk jadwal belajar yang bisa dipasang di ponsel.',
         'tag': 'Mobile', 'ikon': '{ }', 'hue': 285, 'tautan': '#'},
        {'judul': 'Rekap Absensi', 'deskripsi': 'Skrip Python yang merapikan data kehadiran menjadi laporan mingguan.',
         'tag': 'Data', 'ikon': '#', 'hue': 38, 'tautan': '#'},
        {'judul': 'Blog Komunitas', 'deskripsi': 'Blog sederhana dengan penulis, kategori, dan komentar.',
         'tag': 'Web', 'ikon': 'Aa', 'hue': 200, 'tautan': '#'},
    ],
    'pengalaman': [
        {'periode': '2025 sampai sekarang', 'posisi': 'Asisten Praktikum Pemrograman Web',
         'tempat': 'Laboratorium Komputer Kampus',
         'uraian': 'Membimbing mahasiswa membangun aplikasi Flask dan menyusun modul latihan.'},
        {'periode': '2024', 'posisi': 'Magang Web Developer',
         'tempat': 'Studio Digital Lokal',
         'uraian': 'Membuat halaman katalog dan formulir pemesanan untuk klien usaha kecil.'},
        {'periode': '2023', 'posisi': 'Anggota Komunitas Belajar Python',
         'tempat': 'Komunitas Mahasiswa',
         'uraian': 'Mengisi sesi berbagi tentang dasar Python dan pengenalan Flask.'},
    ],
    'sosial': [
        {'nama': 'GitHub', 'url': 'https://github.com/'},
        {'nama': 'LinkedIn', 'url': 'https://www.linkedin.com/'},
        {'nama': 'Instagram', 'url': 'https://www.instagram.com/'},
    ],
}
