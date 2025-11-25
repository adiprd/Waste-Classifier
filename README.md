# Waste Classification Web App

Klasifikasi Sampah Organik vs Daur Ulang Berbasis Deep Learning

Aplikasi ini adalah sistem klasifikasi gambar berbasis web menggunakan **Flask** dan **Keras/TensorFlow** untuk mengidentifikasi dua jenis sampah:

* **Organic**
* **Recyclable**

Model deep learning dilatih sebelumnya menggunakan CNN, dan aplikasi web menerima upload gambar, memprosesnya, lalu mengembalikan hasil prediksi beserta confidence dan rekomendasi pengolahan sampah.

---

## Fitur Utama

### 1. Klasifikasi Gambar secara Real-Time

Pengguna dapat mengunggah gambar sampah, dan sistem akan memberi label:

* Organic
* Recyclable

Serta menampilkan tingkat confidence model.

### 2. Rekomendasi Otomatis

Selain klasifikasi, aplikasi memberikan tips pengolahan sampah sesuai kategori:

**Organic**

* Bisa dijadikan kompos
* Bisa sebagai pakan Maggot BSF
* Cocok untuk lubang biopori

**Recyclable**

* Bisa dijual ke Bank Sampah
* Harus dibersihkan sebelum daur ulang
* Dapat dibuat kerajinan seperti Ecobrick

### 3. Model Deep Learning Load Sekali

Model diload saat aplikasi start untuk performa maksimum.

### 4. API Endpoint

* `GET /` → Halaman utama (upload UI)
* `POST /predict` → API prediksi, menerima file gambar dan mengembalikan JSON

---

## Struktur Proyek

```
├── app.py                        # Main Flask application
├── templates/
│   └── index.html                # UI untuk upload gambar
├── waste_classifier_model.h5     # Model CNN terlatih
├── static/                       # (opsional) CSS/JS
└── README.md
```

---

## Instalasi

### 1. Clone repository

```bash
git clone <repo-url>
cd <project-folder>
```

### 2. Install dependencies

```bash
pip install flask tensorflow pillow numpy
```

Atau:

```bash
pip install -r requirements.txt
```

### 3. Pastikan model tersedia

File:

```
waste_classifier_model.h5
```

harus berada dalam direktori root proyek.

---

## Menjalankan Aplikasi

```bash
python app.py
```

Default berjalan di:

```
http://127.0.0.1:5000/
```

---

## Cara Penggunaan

1. Buka halaman web
2. Upload gambar sampah
3. Tekan tombol “Predict”
4. Hasil label, confidence, dan tips akan muncul secara otomatis

Endpoint JSON (tanpa UI):

```bash
curl -X POST -F "file=@sampah.jpg" http://127.0.0.1:5000/predict
```

---

## Detail Proses Prediksi

1. Gambar diubah ke RGB
2. Di-resize ke 224×224
3. Dinormalisasi (0–1)
4. Model memprediksi output softmax
5. Output tertinggi → label final + confidence

---

## Contoh Output JSON

```json
{
  "label": "Recyclable",
  "confidence": "92.41%",
  "tips": [
    "Dapat dijual di Bank Sampah.",
    "Bersihkan dari sisa makanan sebelum dibuang.",
    "Bisa diubah menjadi kerajinan (Ecobrick)."
  ]
}
```

---

## Lisensi

Proyek ini bebas digunakan untuk edukasi, penelitian, prototipe aplikasi lingkungan, atau integrasi ke sistem daur ulang.

---
