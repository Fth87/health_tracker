from datetime import datetime, timedelta


def calculate_time_difference(start_time, end_time):
    try:
        waktu_mulai = datetime.strptime(start_time, "%H:%M")
        waktu_selesai = datetime.strptime(end_time, "%H:%M")
        if waktu_selesai < waktu_mulai:
            waktu_selesai += timedelta(days=1)
        return (waktu_selesai - waktu_mulai).seconds / 3600
    except ValueError:
        raise ValueError("Format waktu harus HH:MM (contoh: 22:00).")
