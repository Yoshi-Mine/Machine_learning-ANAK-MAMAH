# 🧠 Machine Learning - ANAK MAMAH  
### 🎙️ Speech-to-Text + Language Detection (Desktop App)

Aplikasi ini adalah hasil kompilasi dari proyek **Speech-to-Text dan Language Detection** menggunakan model **Faster Whisper** serta antarmuka **Tkinter**, dikemas menjadi file `.exe` agar dapat dijalankan langsung di Windows tanpa instalasi Python.

---

## ✨ Fitur Utama

- 🎧 **Speech-to-Text (STT):** Mengubah ucapan dari file audio menjadi teks secara otomatis.
- 🌍 **Deteksi Bahasa Otomatis:** Mengidentifikasi bahasa teks hasil transkripsi menggunakan `langdetect`.
- ⚙️ **Pilihan Model Whisper:** `tiny`, `base`, `small`, `medium`, `large-v1`, `large-v2`.
- 🧩 **Antarmuka Grafis (GUI):** Dibangun dengan **Tkinter**, gratis dan tanpa watermark.
- 📊 **Pengaturan Beam Size:** Mengatur tingkat akurasi decoding.
- 💬 **Status Progres Real-time:** Menampilkan status pemrosesan di bagian bawah aplikasi.

---

## 📦 Struktur Proyek

```
📁 Machine_learning-ANAK-MAMAH
├── dist/
│   └── stt_lang_app_tk.exe        # Aplikasi hasil build (.exe)
├── stt_lang_app_tk.py             # Kode sumber utama
├── README.md                      # Dokumentasi proyek ini
└── requirements.txt (opsional)    # Dependensi Python
```

---

## 🚀 Cara Menjalankan Aplikasi

### 🔹 Versi Windows (.exe)
1. Unduh file:
   ```
   dist/stt_lang_app_tk.exe
   ```
2. Jalankan langsung dengan klik dua kali.
3. Pilih model, pilih file audio (`.wav`, `.mp3`, `.flac`, `.m4a`, `.ogg`), lalu tekan **Transcribe**.
4. Hasil teks dan bahasa akan muncul di jendela utama.

---

## 🧠 Versi Python (Kode Sumber)

Jika ingin menjalankan langsung dari Python:

### 1️⃣ Instal dependensi
```bash
pip install faster-whisper librosa soundfile langdetect numpy tqdm
```

### 2️⃣ Jalankan aplikasi
```bash
python stt_lang_app_tk.py
```

---

## 🧰 Teknologi yang Digunakan

| Komponen | Keterangan |
|-----------|------------|
| **Bahasa** | Python 3.8+ |
| **GUI** | Tkinter |
| **Model AI** | Faster Whisper |
| **Audio Processing** | librosa, soundfile |
| **Language Detection** | langdetect |
| **Packaging** | PyInstaller (membuat `.exe`) |
| **Version Control** | Git + Git LFS (untuk file besar) |

---

## ⚠️ Catatan Penting

- File `.exe` ini berukuran besar (>500 MB) karena sudah termasuk model dan dependensi Python.
- GitHub menggunakan **Git LFS (Large File Storage)** untuk menyimpan file besar.
- Saat pertama kali menjalankan, model Whisper mungkin memerlukan waktu pemuatan awal.

---

## 📚 Contoh Tampilan Aplikasi

```
+--------------------------------------------------------------+
| Model size: [ small ▼ ]  [Load Model]                        |
| Audio file: [ example.wav                        ] [Browse]  |
| Beam size: [====|-----]  (5)                                 |
| [Transcribe] [Exit]                                          |
|--------------------------------------------------------------|
| Transcription:                                               |
|  -> "Ini contoh hasil transkripsi audio Anda..."             |
|--------------------------------------------------------------|
| Detected Languages:                                          |
|  -> id: 0.98                                                 |
|--------------------------------------------------------------|
| Status: Transcription complete.                              |
+--------------------------------------------------------------+
```

---

## 🔧 Rencana Pengembangan
- 🎤 Menambahkan fitur rekam langsung dari mikrofon  
- 💾 Menyimpan hasil transkripsi ke `.txt` atau `.json`  
- 🌐 Menambahkan fitur terjemahan otomatis  
- ⚡ Optimalisasi model agar berjalan lebih cepat di CPU  

---

## 🧾 Lisensi
Proyek ini dilisensikan di bawah [MIT License](LICENSE).  
Kamu bebas menggunakan, memodifikasi, dan mendistribusikannya untuk tujuan riset maupun pribadi.

---

## ❤️ Kontributor
**Yoshi-Mine**  
> _“Transform your voice into text — and understand the language behind it.”_
