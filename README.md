Panduan Singkat Google Colab

Apa itu Google Colab?
[Google Colab](https://colab.research.google.com/) adalah layanan gratis dari Google yang memungkinkan kita menulis dan menjalankan kode Python langsung di browser.  
Colab sangat populer di kalangan pelajar, peneliti, dan developer karena menyediakan akses ke GPU/TPU gratis, sehingga cocok untuk pembelajaran mesin, analisis data, maupun eksperimen kode Python lainnya.

---

Fitur Utama dari Google Colab
- Mampu menjalankan kode Python tanpa perlu install di komputer.
- Mendukung GPU/TPU gratis untuk komputasi cepat.
- Bisa mengakses file dari Google Drive dengan mudah.
- Mendukung berbagi notebook layaknya Google Docs.
- Bisa menginstal library tambahan dengan "pip install".

---

Cara Menggunakan Google Colab
1. Buka [Google Colab](https://colab.research.google.com/).  
2. Login dengan akun Google.  
3. Klik File → New Notebook untuk membuat notebook baru.  
4. Ketik kode Python pada cell dan jalankan dengan menekan tombol ▶️.  

---

Contoh Kode di Colab
# Cek versi Python
import sys
print(sys.version)

# Cek ketersediaan GPU
import torch
print("GPU tersedia:", torch.cuda.is_available())
