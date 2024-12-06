import services

def get_health_summary(data):

    bmr = services.calculate_bmr(
        data["berat_badan"], data["tinggi_badan"], data["usia"], data["jenis_kelamin"]
    )
    tdee = services.calculate_tdee(bmr, data["aktivitas"])
    rekomendasi_air = services.calculate_rekomendasi_air(data["berat_badan"])
    durasi_tidur = services.calculate_durasi_tidur(data["tidur_mulai"], data["tidur_selesai"])
    bmi = data["berat_badan"] / ((data["tinggi_badan"] / 100) ** 2)

    return {
        "BMI": f"{bmi:.2f} kg/m²",
        "Basal Metabolic Rate (BMR)": f"{bmr:.2f} kcal/hari",
        "Total Daily Energy Expenditure (TDEE)": f"{tdee:.2f} kcal/hari",
        "Air Minum": f"{data['air_minum']}/{rekomendasi_air:.2f} ml",
        "Durasi Tidur": f"{durasi_tidur:.2f} jam",
    }
