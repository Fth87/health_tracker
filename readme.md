# Tracker Kesehatan

Kodingan ini adalah tracker kesehatan yang menggunakan **AI** untuk memberikan saran kesehatan, lalu menghitung berbagai parameter kesehatan seperti **BMI**, **BMR**, **TDEE**, **rekomendasi air minum**, **durasi tidur**, dan **menganalisis data kesehatan**.

## Fitur Utama

1. **Perhitungan Parameter Kesehatan**:
   - **BMI (Body Mass Index)**: Menghitung indeks massa tubuh pengguna.
   - **BMR (Basal Metabolic Rate)**: Menentukan kebutuhan kalori dasar per hari.
   - **TDEE (Total Daily Energy Expenditure)**: Estimasi total energi yang dibutuhkan berdasarkan tingkat aktivitas.
   - **Rekomendasi Air Minum**: Menghitung kebutuhan air harian berdasarkan berat badan.
   - **Durasi Tidur**: Menganalisis pola tidur pengguna.

2. **Analisis Kesehatan dengan AI**:
   - generate saran dari AI untuk memprediksi risiko kesehatan.
   - Memberikan saran kebiasaan untuk meningkatkan kesehatan.

## Instalasi

### Requirements

Pastikan sudah punya:
- Python 3
- package Python:
  - `google.generativeai`
  - `dotenv`
- API Key dari https://aistudio.google.com/app/apikey

### Langkah untuk menjalankan aplikasi ini

1. **Clone repositori**:
```bash
git clone https://github.com/Fth87/health_tracker.git
cd health-tracker
```
2. **Buat file .env untuk menyimpan API Key**:
```plaintext
API_KEY=your_google_api_key
```
3. **Install package yang dibutuhkan**:
```bash
pip install -r requirements.txt
```
4. **Jalankan aplikasi**:
```bash
python main.py
```

## Cara Penggunaan
1. **Jalankan aplikasi menggunakan perintah di atas.**
2. **Masukkan data yang diminta:**
    - Berat badan (kg)
    - Tinggi badan (cm)
    - Usia (tahun)
    - Jenis kelamin (laki-laki/perempuan)
    - Tingkat aktivitas (pilih dari daftar)
    - Jumlah air yang diminum (ml)
    - Waktu mulai dan selesai tidur
3. **Aplikasi akan memproses data Anda dan menampilkan hasil perhitungan serta analisis AI.**
    
## Struktur File
``` bash
.
├── controllers
│   ├── __init__.py
│   ├── health_controller.py                
├── models/
│   ├── __init__.py
├── repositories/
│   ├── __init__.py
├── services/                 
│   ├── __init__.py
│   ├── AI_data_service.py
│   ├── calculation_service.py
│   └── health_service.py
├─ tests/                    
│   ├── __init__.py
│   └── test.py
├── utils/
│   ├── __init__.py
│   ├── ai_client.py
│   └── time_utils.py
├── views/                    
│   ├── __init__.py
│   ├── activity_view.py
│   ├── input_view.py
│   ├── loading_view.py
│   ├── output_view.py
│   └── welcome_view.py
├── .env
├── .gitignore
├── main.py                   
├── README.md
└── requirements.txt

```

## Function
- `calculate_bmr` : Menghitung BMR berdasarkan berat badan, tinggi badan, usia, dan jenis kelamin.
- `calculate_tdee`: Menghitung TDEE berdasarkan BMR dan tingkat aktivitas.
- `calculate_rekomendasi_air` : Menghitung rekomendasi kebutuhan air harian.
- `calculate_durasi_tidur` : Menghitung durasi tidur berdasarkan waktu mulai dan selesai.
- `get_gemini_data` : Mengirimkan data ke AI untuk analisis kesehatan.
- `get_summary` : Menggabungkan semua hasil perhitungan menjadi satu ringkasan.
- `get_input` : Mengumpulkan input dari pengguna.
- `loading_indicator` : Menampilkan loading selama proses fetch data dari AI.

## Unit Test
```bash
python -m unittest discover -s tests -p "test.py"
```
