cat << 'EOF' > README.md
# 🧠 CEREBRO V11: NEURAL APEX (FINAL EDITION)

![Version](https://img.shields.io/badge/version-11.0.0--Apex-red)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)

Cerebro V11 adalah Neural Vulnerability Interceptor tercanggih yang menggabungkan kekuatan **Man-in-the-Middle (MitM)** dengan **Kecerdasan Buatan (AI)** lokal melalui Ollama. Alat ini dirancang khusus untuk Bug Hunter profesional yang membutuhkan presisi tinggi dalam mendeteksi Blind SQLi dan bypass WAF.

---

## 🚀 Fitur Utama (The Arsenal)

- ☣️ **GOD MODE:** Menjalankan Standard, Expert (Blind), dan AI Singularity secara simultan dalam satu klik.
- 🤖 **Neural AI Mutation:** Integrasi dengan **Ollama (Llama3)** untuk menciptakan payload bypass WAF yang unik dan tidak terprediksi.
- 🕵️ **Neural Anomaly Detection:** Algoritma deteksi cerdas yang menganalisis perubahan respon server hingga sensitivitas **5%**.
- 🛠️ **Interactive Intercept:** Traffic tidak langsung di-scan; Cerebro akan menahan koneksi dan menunggu perintah (Command) Anda.
- 📊 **Auto-Generated Reports:** Menghasilkan laporan bukti kerentanan dalam format HTML profesional di folder `/reports`.

---

## 🛠️ Instalasi & Setup

### 1. Prasyarat Sistem
Pastikan Anda sudah menginstall:
- **Python 3.10 atau lebih baru**
- **Ollama** (Unduh di [ollama.com](https://ollama.com))

### 2. Instalasi Lingkungan (Virtual Environment)
# Clone repository
```bash
git clone [https://github.com/ShadowRoot32/Cerebro-Apex.git](https://github.com/ShadowRoot32/Cerebro-Apex.git)
cd Cerebro-Apex
```

# Buat & Aktifkan Virtual Env
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows
```

# Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Konfigurasi AI (Ollama)
Cerebro membutuhkan model Llama3 untuk melakukan mutasi payload cerdas secara lokal
```bash
ollama pull llama3
ollama serve
```

### 🌐 Konfigurasi Proxy & Sertifikat SSL
Agar Cerebro dapat membaca traffic HTTPS, Anda wajib melakukan langkah ini:
Jalankan Cerebro: 
```bash
mitmdump -q -s main.py
```

Atur Proxy Browser: Gunakan extension (seperti FoxyProxy) dan arahkan ke 127.0.0.1 port 8080.

Install CA Certificate:

Buka browser yang sudah ter-proxy, akses: http://mitm.it
Pilih platform Anda (Windows/Android/iOS) dan download filenya.
PENTING: Install file tersebut ke dalam folder "Trusted Root Certification Authorities" pada sistem operasi Anda.

### ☣️ Cara Penggunaan (Workflow)
Jalankan script utama: ```python3 main.py``` (atau ```mitmdump -q -s main.py```).

Lakukan browsing pada target (Scope).

Cerebro akan memberikan notifikasi "LOCK ON" saat mendeteksi parameter atau path ID.

Pilih Level Serangan:

1 Standard: Scan cepat untuk bug yang terlihat jelas (Error-based).

2 Expert: Untuk Blind SQLi yang sulit dideteksi melalui analisis anomali.

3 Singularity: Mutasi payload menggunakan AI Llama3 untuk bypass WAF.

4 GOD MODE: Kombinasi maut semua teknik di atas.

Cek folder reports/ untuk melihat temuan bug dalam format HTML yang gahar.

### ⚠️ Disclaimer
Alat ini dibuat untuk tujuan pendidikan dan pengujian keamanan yang sah. Penulis tidak bertanggung jawab atas penyalahgunaan atau kerusakan yang disebabkan oleh alat ini. Gunakan dengan bijak dan etis.

Developed by ShadowRoot32 EOF
