import utils

def calculate_bmr(berat_badan, tinggi_badan, usia, jenis_kelamin):
    if jenis_kelamin == "laki-laki":
        return round(66 + (13.7 * berat_badan) + (5 * tinggi_badan) - (6.8 * usia))
    elif jenis_kelamin == "perempuan":
        return round(655 + (9.6 * berat_badan) + (1.8 * tinggi_badan) - (4.7 * usia))
    else:
        raise ValueError("Jenis kelamin harus 'laki-laki' atau 'perempuan'.")

def calculate_tdee(bmr, aktivitas_faktor):
    aktivitas_faktor_data = [1.2, 1.375, 1.55, 1.725, 1.9]
    return round(bmr * aktivitas_faktor_data[int(aktivitas_faktor)-1])

def calculate_rekomendasi_air(berat_badan):
    return berat_badan * 35

def calculate_durasi_tidur(tidur_mulai, tidur_selesai):
    return utils.calculate_time_difference(tidur_mulai, tidur_selesai)
