import views

def get_user_data():
    while True:
        try:
            berat_badan = float(input("Berat badan (kg): "))
            tinggi_badan = float(input("Tinggi badan (cm): "))
            usia = int(input("Usia (tahun): "))
            jenis_kelamin = (
                input("Jenis kelamin (laki-laki/perempuan): ").strip().lower()
            )
            if jenis_kelamin not in ["laki-laki", "perempuan"]:
                raise ValueError("Masukkan jenis kelamin yang valid!")
            break
        except ValueError as e:
            print(f"Input tidak valid: {e}. Silakan coba lagi.\n")

    views.display_activity_options()

    while True:
        try:
            aktivitas = int(input("Pilih tingkat aktivitas Anda (1-5): "))
            if aktivitas < 1 or aktivitas > 5:
                raise ValueError("Pilih angka antara 1 hingga 5!")
            break
        except ValueError as e:
            print(f"Input tidak valid: {e}. Silakan coba lagi.\n")

    while True:
        try:
            air_minum = float(input("Sudah minum berapa ml hari ini? (ml): "))
            break
        except ValueError:
            print("Masukkan jumlah air dalam angka yang valid.")

    tidur_mulai = input("Waktu mulai tidur tadi malam (HH:MM): ")
    tidur_selesai = input("Waktu selesai tidur (HH:MM): ")

    return {
        "berat_badan": berat_badan,
        "tinggi_badan": tinggi_badan,
        "usia": usia,
        "jenis_kelamin": jenis_kelamin,
        "aktivitas": aktivitas,
        "air_minum": air_minum,
        "tidur_mulai": tidur_mulai,
        "tidur_selesai": tidur_selesai,
    }
