import unittest
from unittest.mock import patch
from io import StringIO
import services
from datetime import datetime
import views


class TestHealthServices(unittest.TestCase):

    def test_calculate_bmr(self):
        self.assertEqual(services.calculate_bmr(70, 175, 25, "laki-laki"), 1730)
        self.assertEqual(services.calculate_bmr(60, 165, 30, "perempuan"), 1387)
        with self.assertRaises(ValueError):
            services.calculate_bmr(60, 165, 30, "invalid")

    def test_calculate_tdee(self):
        self.assertEqual(services.calculate_tdee(1766.25, 3), 2738)

    def test_calculate_rekomendasi_air(self):
        self.assertEqual(services.calculate_rekomendasi_air(70), 70 * 35)

    def test_calculate_durasi_tidur(self):
        self.assertEqual(services.calculate_durasi_tidur("22:00", "06:00"), 8.0)
        with self.assertRaises(ValueError):
            services.calculate_durasi_tidur("", "")
            
class TestGetUserData(unittest.TestCase):
    @patch("builtins.input", side_effect=[
        "70",          # Berat badan
        "170",         # Tinggi badan
        "25",          # Usia
        "laki-laki",   # Jenis kelamin
        "3",           # Tingkat aktivitas
        "2000",        # Air minum
        "22:00",       # Waktu tidur mulai
        "06:00"        # Waktu tidur selesai
    ])
    @patch("sys.stdout", new_callable=StringIO)
    def test_get_user_data_valid(self, mock_stdout, mock_input):
        data = views.get_user_data()
        self.assertEqual(data["berat_badan"], 70.0)
        self.assertEqual(data["tinggi_badan"], 170.0)
        self.assertEqual(data["usia"], 25)
        self.assertEqual(data["jenis_kelamin"], "laki-laki")
        self.assertEqual(data["aktivitas"], 3)
        self.assertEqual(data["air_minum"], 2000.0)
        self.assertEqual(data["tidur_mulai"], "22:00")
        self.assertEqual(data["tidur_selesai"], "06:00")
