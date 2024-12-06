import google.generativeai as genai
import os
from dotenv import load_dotenv
import services

load_dotenv()

def get_gemini_data(data):
    prompt = f"""
    Berikut adalah data kesehatan pengguna:
    - Berat badan: {data['berat_badan']} kg
    - Tinggi badan: {data['tinggi_badan']} cm
    - Usia: {data['usia']} tahun
    - Jenis kelamin: {data['jenis_kelamin']}
    - Durasi tidur: {services.calculate_durasi_tidur(data['tidur_mulai'], data['tidur_selesai'])} jam
    - Tingkat aktivitas: {services.calculate_tdee(services.calculate_bmr(
        data["berat_badan"], data["tinggi_badan"], data["usia"], data["jenis_kelamin"]
    ),data['aktivitas'])} (faktor aktivitas)

    Berdasarkan data ini:
    1. Prediksi risiko kesehatan seperti obesitas, diabetes, atau tekanan darah tinggi dan masalah kesehatan lainnya, jelaskan selengkap mungkin.
    2. Identifikasi kebiasaan tidak sehat, seperti pola tidur yang kurang.
    3. Berikan saran perubahan kebiasaan kecil yang dapat berdampak besar.

    Tampilkan analisis lengkap dan detail.
    """
    genai.configure(api_key=os.getenv("API_KEY"))
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Terjadi kesalahan saat memproses data dengan AI: {str(e)}"
