
#!/usr/bin/env python3
"""
Speech-to-Text + Language Detection (Tkinter version)
----------------------------------------------------
Versi ini menggantikan PySimpleGUI dengan Tkinter agar gratis dan tanpa watermark.

Fitur:
- Memilih ukuran model Whisper
- Memilih file audio
- Melakukan transkripsi (Speech-to-Text)
- Deteksi bahasa menggunakan langdetect
- Status progres muncul di bagian bawah

Cara pakai:
    python stt_lang_app_tk.py

Dependensi:
    pip install faster-whisper librosa soundfile langdetect numpy tqdm
"""

import os
import threading
import traceback
import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext, messagebox

import numpy as np
import soundfile as sf
import librosa
from langdetect import detect_langs, DetectorFactory

# --- Deterministik untuk langdetect ---
DetectorFactory.seed = 0

# --- Import WhisperModel ---
try:
    from faster_whisper import WhisperModel
except Exception:
    WhisperModel = None


# ==========================================================
# UTILITAS
# ==========================================================
def load_audio(path, sr=16000, mono=True):
    """Membaca file audio dan melakukan resampling bila perlu."""
    try:
        data, file_sr = sf.read(path)
        if data.ndim > 1 and mono:
            data = np.mean(data, axis=1)
        if file_sr != sr:
            data = librosa.resample(data.astype(np.float32), orig_sr=file_sr, target_sr=sr)
        return data, sr
    except Exception:
        data = librosa.load(path, sr=sr, mono=mono)[0]
        return data, sr


def transcribe_file(model, audio_path, language=None, task="transcribe", beam_size=5):
    """Melakukan transkripsi audio menggunakan model Whisper."""
    audio, sr = load_audio(audio_path, sr=16000, mono=True)
    audio = audio.astype("float32")
    segments, info = model.transcribe(audio, beam_size=beam_size, language=language, task=task)
    text = " ".join([s.text for s in segments])
    return text, info


def detect_languages_on_text(text, top_n=3):
    """Mendeteksi bahasa pada teks hasil transkripsi."""
    try:
        langs = detect_langs(text)
        return langs[:top_n]
    except Exception:
        return []


# ==========================================================
# KELAS GUI
# ==========================================================
class STTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("STT + Language Detection (Tkinter)")
        self.root.geometry("800x600")

        self.model_instance = None
        self.model_lock = threading.Lock()

        # --- Frame Atas: Pilih model & file ---
        top_frame = ttk.Frame(root, padding=10)
        top_frame.pack(fill=tk.X)

        ttk.Label(top_frame, text="Model size (Whisper):").grid(row=0, column=0, sticky="w")
        self.model_var = tk.StringVar(value="small")
        self.model_menu = ttk.Combobox(top_frame, textvariable=self.model_var,
                                       values=["tiny", "base", "small", "medium", "large-v1", "large-v2"], width=12)
        self.model_menu.grid(row=0, column=1, padx=5)
        ttk.Button(top_frame, text="Load Model", command=self.load_model_thread).grid(row=0, column=2, padx=5)

        ttk.Label(top_frame, text="Audio file:").grid(row=1, column=0, sticky="w", pady=5)
        self.file_path_var = tk.StringVar()
        ttk.Entry(top_frame, textvariable=self.file_path_var, width=60).grid(row=1, column=1, padx=5)
        ttk.Button(top_frame, text="Browse", command=self.browse_file).grid(row=1, column=2, padx=5)

        # --- Beam size slider ---
        beam_frame = ttk.Frame(root, padding=10)
        beam_frame.pack(fill=tk.X)
        ttk.Label(beam_frame, text="Beam size (1–10):").pack(side=tk.LEFT)
        self.beam_var = tk.IntVar(value=5)
        self.beam_slider = ttk.Scale(beam_frame, from_=1, to=10, variable=self.beam_var, orient="horizontal")
        self.beam_slider.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10)

        # --- Tombol transkripsi ---
        btn_frame = ttk.Frame(root, padding=10)
        btn_frame.pack()
        ttk.Button(btn_frame, text="Transcribe", command=self.transcribe_thread).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Exit", command=root.destroy).pack(side=tk.LEFT, padx=5)

        # --- Output Transkripsi ---
        ttk.Label(root, text="Transcription:").pack(anchor="w", padx=10)
        self.output_text = scrolledtext.ScrolledText(root, height=10, wrap=tk.WORD)
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # --- Output Deteksi Bahasa ---
        ttk.Label(root, text="Detected Languages:").pack(anchor="w", padx=10)
        self.lang_text = scrolledtext.ScrolledText(root, height=5, wrap=tk.WORD)
        self.lang_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # --- Status bar ---
        self.status_var = tk.StringVar(value="Ready.")
        self.status_bar = ttk.Label(root, textvariable=self.status_var, relief=tk.SUNKEN, anchor="w")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    # ======================================================
    # EVENT HANDLERS
    # ======================================================
    def set_status(self, msg):
        self.status_var.set(msg)
        self.root.update_idletasks()

    def browse_file(self):
        filetypes = [("Audio files", "*.wav *.mp3 *.flac *.m4a *.ogg")]
        filename = filedialog.askopenfilename(title="Choose Audio File", filetypes=filetypes)
        if filename:
            self.file_path_var.set(filename)

    def load_model_thread(self):
        threading.Thread(target=self._load_model, daemon=True).start()

    def _load_model(self):
        size = self.model_var.get()
        try:
            self.set_status(f"Loading model '{size}'... Please wait.")
            m = WhisperModel(size, device="cpu", compute_type="int8")
            with self.model_lock:
                self.model_instance = m
            self.set_status(f"Model '{size}' loaded successfully.")
        except Exception as e:
            self.set_status("Failed to load model.")
            traceback.print_exc()
            messagebox.showerror("Error", f"Failed to load model: {e}")

    def transcribe_thread(self):
        threading.Thread(target=self._transcribe, daemon=True).start()

    def _transcribe(self):
        if self.model_instance is None:
            messagebox.showwarning("Warning", "Model not loaded yet.")
            return

        path = self.file_path_var.get()
        if not os.path.exists(path):
            messagebox.showwarning("Warning", "Please select a valid audio file.")
            return

        beam = int(self.beam_var.get())

        try:
            self.set_status("Transcribing audio...")
            self.output_text.delete("1.0", tk.END)
            self.lang_text.delete("1.0", tk.END)

            with self.model_lock:
                text, info = transcribe_file(self.model_instance, path, beam_size=beam)

            if not text.strip():
                self.output_text.insert(tk.END, "[No text detected]\n")
                self.set_status("Done (no text found).")
                return

            self.output_text.insert(tk.END, text.strip() + "\n")

            langs = detect_languages_on_text(text, top_n=5)
            out_langs = "\n".join([f"{l.lang}: {l.prob:.3f}" for l in langs])
            self.lang_text.insert(tk.END, out_langs)

            self.set_status("Transcription + language detection complete.")
        except Exception as e:
            traceback.print_exc()
            messagebox.showerror("Error", f"Error during transcription:\n{e}")
            self.set_status("Error during transcription.")


# ==========================================================
# MAIN
# ==========================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = STTApp(root)
    root.mainloop()

