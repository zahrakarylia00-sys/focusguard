# 👁 FocusGuard v2 — Hosting Version
### Deteksi Distraksi Belajar | Siap Deploy ke Railway/Render

---

## 📁 Struktur Folder

```
focusguard_v2/
├── app.py               ← Flask server (ringan, tanpa OpenCV)
├── requirements.txt     ← flask, qrcode, gunicorn
├── Procfile             ← perintah start untuk hosting
├── railway.json         ← konfigurasi Railway
├── templates/
│   ├── index.html       ← Halaman utama + QR
│   ├── detect.html      ← Deteksi (MediaPipe WASM di browser)
│   └── result.html      ← Laporan hasil sesi
└── README.md
```

---

## 🚀 Cara Deploy ke Railway (Gratis)

### 1. Buat akun Railway
Buka: https://railway.app → daftar pakai GitHub

### 2. Install Git (jika belum)
Download: https://git-scm.com/download/win

### 3. Upload ke GitHub dulu
```bash
cd C:\focusguard_v2

git init
git add .
git commit -m "FocusGuard v2"
```
Buat repo baru di GitHub → lalu:
```bash
git remote add origin https://github.com/username/focusguard.git
git push -u origin main
```

### 4. Deploy di Railway
- Buka railway.app → New Project → Deploy from GitHub
- Pilih repo focusguard → Deploy
- Tunggu ±2 menit → dapat link publik

### 5. Update BASE_URL di app.py
```python
# Ganti baris ini:
BASE_URL = "http://localhost:5000"

# Jadi (sesuaikan link Railway kamu):
BASE_URL = "https://focusguard.up.railway.app"
```
Lalu push ulang ke GitHub → Railway auto-deploy.

---

## 💻 Cara Jalankan Lokal (Testing)

```bash
cd C:\focusguard_v2
.\venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
Buka: http://localhost:5000

---

## ✅ Fitur

- Deteksi wajah di **browser** (MediaPipe WASM) — tidak membebani server
- Face mesh / jaringan wajah tampil di kamera
- Beep seram saat distraksi
- Laporan sesi + QR Code
- Bisa diakses 200+ orang sekaligus
- Gratis di Railway

---

## ⚠️ Catatan Penting

Browser **harus** mengizinkan akses kamera.
Untuk HP, gunakan **Chrome** atau **Safari**.
Hosting Railway gratis = **500 jam/bulan** (cukup untuk demo/tugas).
