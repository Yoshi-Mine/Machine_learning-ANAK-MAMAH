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

📁 Machine_learning-ANAK-MAMAH
├── dist/
│ └── stt_lang_app_tk.exe # Aplikasi hasil build (.exe)
├── stt_lang_app_tk.py # Kode sumber utama
└── README.md # Dokumentasi proyek ini


---

## 🚀 Cara Menjalankan Aplikasi

### 🔹 Versi Windows (.exe)
1. Unduh file:
dist/stt_lang_app_tk.exe
2. Jalankan langsung dengan klik dua kali.
3. Pilih model, pilih file audio (`.wav`, `.mp3`, `.flac`, `.m4a`, `.ogg`), lalu tekan **Transcribe**.
4. Hasil teks dan bahasa akan muncul di jendela utama.

---

## 🧠 Versi Python (Kode Sumber)

Jika ingin menjalankan langsung dari Python:

### 1️⃣ Instal dependensi
```bash
pip install faster-whisper librosa soundfile langdetect numpy tqdm
python stt_lang_app_tk.py
