# 🎵 Audio Compression Assignment - ADPCM & MP3

## 🎧 Introduction

This is a course project for *Multimedia Data Compression and Coding*.  
We recorded a 3–4 minute audio, analyzed its spectrum using MATLAB, compressed it using **ADPCM** and **MP3**, compared the quality using **PSNR**, and blended it with a MIDI track to create a jazz-style remix.  
The project includes all source code, processed audio files, visualizations, and a detailed report.

---

## 🚀 Features

- Audio recording with speaker info (name, student ID, task)
- Spectrum analysis using MATLAB
- Audio compression with ADPCM (custom) and MP3 (LAME encoder)
- PSNR comparison: original vs ADPCM, original vs MP3
- MIDI music generation and jazz remix
- Full technical report and group contributions

---

## 🛠 Tech Stack

- `MATLAB`: Signal spectrum analysis & PSNR computation  
- `Python`: Audio processing (optional for ADPCM)  
- `C`: MP3 compression using LAME library  
- `FFmpeg`: For format conversion and playback testing  
- `GitHub`: Version control and collaboration  
- `Markdown`: Documentation & reporting  

---

## 📁 Folder Structure
```plaintext
|-- 1_show_spectrum/         # Visualizes the frequency spectrum of the original audio
|-- 2_adpcm_compression/     # Compresses audio using the ADPCM codec
|-- 3_psnr_analysis/         # Calculates PSNR between original, ADPCM, and MP3 files
|-- 4_mix_midi_jazz_song/    # Mixes a jazz track from the generated MIDI file
|-- MIDI_Jazz_Generation/    # Automatically generates a MIDI file using Python
|   └── jazz.py              # Python script for generating random jazz melodies
|-- input/                   # Contains original input audio files
|-- output/                  # Stores compressed files, spectrum plots, and PSNR results
```

---

## 🧪 How to Run

1. Install dependencies (LAME, MATLAB toolboxes, FFmpeg).
2. Compile and run the MP3 compression using provided C code.
3. Run MATLAB scripts to analyze spectrum and compute PSNR.
4. Open and play files in `audio/` and `midi/` for review.

---

## 📦 Deliverables

- ✅ Full Report + Appendix (PDF/DOCX)
- ✅ Input & Output Audio Files (WAV, MP3, ADPCM, MIDI)
- ✅ Spectrum Charts & PSNR Tables
- ✅ Source Code (MATLAB, C, Python)
- ✅ Video Presentation (5–7 mins)
- ✅ README.md with all project info

---

## 📬 Contact

For any issues or questions, feel free to reach out to group members via the report or presentation.


